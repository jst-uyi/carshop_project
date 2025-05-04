from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Car  
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def car_list(request):
    # Get filter parameters from the request
    search_query = request.GET.get('search', '')
    selected_car_name = request.GET.get('car_name', '')
    selected_fuel = request.GET.get('fuel_type', '')
    selected_owner = request.GET.get('owner_type', '')
    selected_location = request.GET.get('location', '')
    selected_year = request.GET.get('year', '')

    # Start with all cars
    cars = Car.objects.all()

    # Apply filters
    if search_query:
        cars = cars.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if selected_car_name:
        cars = cars.filter(name=selected_car_name)
    if selected_fuel:
        cars = cars.filter(fuel_type=selected_fuel)
    if selected_owner:
        cars = cars.filter(owner_type=selected_owner)
    if selected_location:
        cars = cars.filter(location=selected_location)
    if selected_year:
        cars = cars.filter(year=selected_year)

    # For dropdowns: get unique values
    car_names = Car.objects.values_list('name', flat=True).distinct().order_by('name')
    fuel_types = Car.objects.values_list('fuel_type', flat=True).distinct().order_by('fuel_type')
    owner_types = Car.objects.values_list('owner_type', flat=True).distinct().order_by('owner_type')
    locations = Car.objects.values_list('location', flat=True).distinct().order_by('location')
    years = Car.objects.values_list('year', flat=True).distinct().order_by('-year')

    context = {
        'cars': cars,
        'search_query': search_query,
        'car_names': car_names,
        'fuel_types': fuel_types,
        'owner_types': owner_types,
        'locations': locations,
        'years': years,
        'selected_car_name': selected_car_name,
        'selected_fuel': selected_fuel,
        'selected_owner': selected_owner,
        'selected_location': selected_location,
        'selected_year': selected_year,
    }
    return render(request, 'cars/car_list.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('car_list')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'cars/register.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('car_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'cars/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('car_list')

@login_required
def protected_view(request):
    return render(request, 'cars/protected.html')

def home_view(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'cars/about.html')

def blog(request):
    # Add blog post logic later
    return render(request, 'cars/blog.html', {'title': 'Blog'})


def careers(request):
    return render(request, 'cars/careers.html', {'title': 'Careers'})

def terms(request):
    return render(request, 'cars/terms.html', {'title': 'Terms of Use'})

def contact(request):
    if request.method == 'POST':
        # Add form handling logic later
        pass
    return render(request, 'cars/contact.html', {'title': 'Contact Us'})