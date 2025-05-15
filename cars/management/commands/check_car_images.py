from django.core.management.base import BaseCommand
from cars.models import Car
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Check which car images are missing from the media/car_images/ directory compared to the database.'

    def handle(self, *args, **options):
        missing = 0
        print('--- Checking Car Images ---')
        for car in Car.objects.all():
            if car.image and car.image.name:
                path = os.path.join(settings.MEDIA_ROOT, car.image.name)
                if not os.path.exists(path):
                    print(f'MISSING: {car.name} -> {car.image.name}')
                    missing += 1
        print(f'Total missing images: {missing}')
        if missing == 0:
            print('All car images are present.')
