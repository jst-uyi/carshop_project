from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Car(models.Model):
    FUEL_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('LPG', 'LPG'),
        ('CNG', 'CNG'),
    ]
    
    TRANSMISSION = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]
    
    OWNER_TYPE = [
        ('First', 'First Owner'),
        ('Second', 'Second Owner'),
    ]

    #serial_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    kilometers = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)
    transmission = models.CharField(max_length=10, choices=TRANSMISSION)
    owner_type = models.CharField(max_length=10, choices=OWNER_TYPE)
    mileage = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='staticfiles/car_images/', blank=True, null=True)  # For uploaded images

    @property
    def image_url(self):
        from django.templatetags.static import static
        if self.image and hasattr(self.image, 'url') and self.image.name:
            try:
                url = self.image.url
                if url:
                    return url
            except Exception:
                pass
        return static('cars/images/placeholder.png')

    def __str__(self):
        return self.name





class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    payment_id = models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        return f"Order #{self.id} - {self.car.name} for {self.user.username}"
    

class Order_summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.name}"  
    

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.car.name}"    
    

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.name} in cart for {self.user.username}"

    def get_total_price(self):
        return self.car.price * self.quantity
