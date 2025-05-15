
                                  Django Solo Car Shop Application Report
1. Design
The car shop application was designed to facilitate the browsing and purchasing of cars by users through a user-friendly web interface. The system architecture includes user-facing views, admin management interfaces, and backend logic for order processing. The core models include:
•	Car: Stores details such as name, price, images, specifications, and availability.
•	Order: Represents a purchase made by a user, linked to car(s).
•	User: Handles authentication, with user roles (regular and admin).
•	OrderItem: Associates specific cars with orders, allowing for multiple-car purchases.
The UI design includes a homepage with car listings, a product detail page, a shopping cart, and an admin dashboard for tracking orders and revenue.

2. Development
The application was built using the Django web framework. Key features include:
•	Frontend: HTML, Bootstrap for responsive design, and Chart.js for visualizing sales data.
•	Backend: Django ORM for data modeling, with views handling logic for displaying cars, managing the shopping cart, processing orders, and filtering data for charts.
•	Security: Django’s built-in authentication ensures only authorized users can place orders or access admin features.

3. Implementation
Models were implemented to support car listings and purchase workflows. Dynamic views display products, process cart actions, and generate statistics for the admin dashboard. Revenue data is grouped by time periods (weekly, monthly, yearly) using Django's database functions and rendered as bar charts.
Key implementation tasks:
•	Set up car CRUD functionality.
•	Designed cart and checkout flows.
•	Created order and revenue analytics with filtering.
•	Built a custom admin dashboard.

4. Installation
To install and run the application:
1.	Clone the project repository.
2.	Create a virtual environment and install dependencies:
•	python -m venv venv
•	source .venv/bin/activate
•	pip install -r requirements.txt
3.	Apply migrations:
•	python manage.py migrate
4.	Start the development server:
•	python manage.py runserver 0.0.0.0:8000
Static and media files are served during development by setting appropriate configurations in settings.py.

5. Use
Users can:
•	Register and log in.
•	Browse available cars.
•	View car details with specifications and images.
•	Add cars to a cart and place orders.
Admins can:
•	Manage car listings.
•	Manage users.
•	View total sales, total users, total cars, and revenue charts.
•	Monitor recent orders and filter revenue trends.



