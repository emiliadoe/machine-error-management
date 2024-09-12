# machine-error-management

This project was created to built a Machine Error Management System using Python and the Django framework. 
It allows users to manage a database of machines, their descriptions, and the error codes that have been encountered on these machines. The system also provides details on how to resolve these errors.

# Main components

- Backend: Database and API logic using Django
- Frontend:  Graphical User Interface built with Django so users can interact with the system

# Installation
Prerequisites: Python (version 3.x), Django (version 4.x or higher),relational database (SQLite is used by default)

# Setup
Clone the repository:
git clone https://github.com/your-repository/machine-error-management.git
cd machine-error-management

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate       # For Windows

Install the required dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Create a superuser to access the admin panel:
python manage.py createsuperuser

Run the Django development server:
python manage.py runserver

Access the app by opening a browser and navigating to:
http://localhost:8000



