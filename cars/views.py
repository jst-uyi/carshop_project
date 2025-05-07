from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Car, Order  
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse


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

@login_required(login_url='/login/')
def purchase_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user=request.user,
            car=car,
            total_price=car.price,
            status='pending'
        )
        
        # In a real app, you would integrate with a payment gateway here
        # For now, we'll simulate a successful payment
        order.status = 'completed'
        order.save()
        
        car.available = False
        car.save()
        
        messages.success(request, f"Congratulations! You've purchased the {car.name}")
        return redirect('order_confirmation', order_id=order.id)
    
    return render(request, 'cars/purchase.html', {'car': car})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cars/order_confirmation.html', {'order': order})