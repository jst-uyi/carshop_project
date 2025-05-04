from django.db import models


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


    def __str__(self):
        return self.name


  