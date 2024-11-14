**Hostel Rental System with Django REST Framework**

This project is a rental platform for student looking to get hostels and also hostel owners looking to put their hostels up for rent. This is built using _Django REST Framework_. 
It allows users to create and search for hostels, and provides functionalities similar to the popular accommodation rental platform.

**Technologies Used**

1. Python 3.11
2. Django
3. Django REST Framework (DRF)

**Requirements**

1. Python 3.11 installed
2. Django installed

**Installation**

1. Clone this repository: git clone https://github.com/Abdul12majid/propulse_b.git
2. Navigate to the project directory: cd propulse_b
3. Create a virtual environment (recommended): pythom -m venv py_env
4. Activate virtual environment: source py_env/scripts/activate
5. Install project dependencies: pip install -r requirements.txt
6. Migrate the database (assuming using a database like PostgreSQL): python manage.py migrate   #sqlite was used for this, feel free to connect to a more standard database.
7. Create a superuser account (optional, for initial admin access): winpty python manage.py createsuperuser

**Usage**

1. Start the development server: python manage.py runserver
2. Access the API documentation at - http://127.0.0.1:8000/api/docs/ (not available yet)

**Features - ENDPOINTS ** 

{
    "All Hostels": "http://localhost:8000/all_hostels/", - *List all hostels
    "Available Hostels": "http://localhost:8000/available_hostels/", - *List available hostels
    "Create Hostel": "http://localhost:8000/create_hostel/", - *Create hostel
    "Send message": "http://localhost:8000/send_message/", - *Send message feature
    "Login user": "http://localhost:8000/user/login", - *Login user
    "Logout user": "http://localhost:8000/user/logout", - *Logout user
    "Register user": "http://localhost:8000/user/register" - *Register user
}

**Contact Me**
Reach out to me for the SECRET_KEY.
For any questions or feedback, feel free to reach out to Majid at yisaabdulmajid@gmail.com or open an issue on the GitHub repository.

   
