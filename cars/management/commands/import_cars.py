import csv
from django.core.management.base import BaseCommand
from cars.models import Car

class Command(BaseCommand):
    help = 'Imports cars from CSV file'

    #def add_arguments(self, parser):
        #parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        with open('data/cars.csv', 'r', encoding='ISO-8859-1') as file:
            reader = csv.DictReader(file)
            print(reader.fieldnames[0])
            reader.fieldnames[0] = 'serial_number'
            print(reader.fieldnames[0])
            # Check if the required columns are present in the CSV
            # If not, raise an error
            required_columns = [
                'name', 'location', 'year', 'kilometers', 'fuel_type',
                'transmission', 'owner_type', 'mileage', 'engine', 'power', 'seats', 'price'
            ]
            missing_columns = [col for col in required_columns if col not in reader.fieldnames]
            if missing_columns:
                raise ValueError(f'Missing columns in CSV: {", ".join(missing_columns)}')
            for row in reader:
                    try:
                        Car.objects.create(
                            #serial_number=row['serial_number'],
                            name=row['name'],
                            location=row['location'],
                            year=row['year'],
                            kilometers=row['kilometers'],
                            fuel_type=row['fuel_type'],
                            transmission=row['transmission'],
                            owner_type=row['owner_type'],
                            mileage=row['mileage'].strip(),
                            engine=row['engine'],
                            power=row['power'],
                            seats=row['seats'],
                            price=row['price'],
                            
                        )
                    except Exception as e:
                         print(f"Error importing row {row}, Error: {e}")   
        self.stdout.write(self.style.SUCCESS('Successfully imported cars!'))
