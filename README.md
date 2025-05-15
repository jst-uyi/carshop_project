# Django Car Shop

This is a full-stack Django web application for browsing and purchasing used cars.
It includes user and admin functionality, custom dashboards, and car management.


 **Features**

 User Features
1. Browse and search cars by Name,Fuel type, Owner type, Location, Years.
2. View detailed car information
3. Place orders for available cars

Admin Features
1. Admin login and custom dashboard
2. View stats like total cars, total users, revenue, and recent orders
3. Manage cars (add, update, delete) from a custom management interface
4. Manage users

**Technologies Used**

- Python 3.7
- Django 5.2.1
- SQLite (default database)
- Bootstrap 5 (for styling)
- Chart.js (for admin charts )

 **Installation**

1. Clone the repository or copy the project files into your development environment (e.g., VS Code or Codio).
   git clone https://github.com/jst-uyi/carshop_project.git

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

3. Install required packages:         
    ```bash
   pip install -r requirements.txt

4. Apply database migrations:
    ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Run development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000

   copy Codio box url to browser (e.g https://premiumframe-blocksalami.codio-box.uk)     

   
