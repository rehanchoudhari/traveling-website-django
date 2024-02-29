# Django Traveling Website Project

This project is a traveling website application built using Django.

## Requirements

- Python 3.x
- Django (see requirements.txt)

## Setting up the Environment

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rehanchoudhari/traveling-website-django.git


- Create a virtual environment (optional but recommended):

   ```bash
   cd traveling-website-django
   python3 -m venv venv


## Activate the virtual environment:

- On Linux/macOS:

   ```bash
   source venv/bin/activate

- On Windows (Command Prompt):

   ```bash
   .\venv\Scripts\activate

- On Windows (PowerShell):
- 
   ```bash
   .\venv\Scripts\Activate.ps1

- Install dependencies:
- 
   ```bash
   pip install -r requirements.txt


## Database Setup

- Apply migrations:

   ```bash
   python manage.py migrate

- Create a superuser account:
   ```bash
   python manage.py createsuperuser

- Running the Development Server
   ```bash
   python manage.py runserver

The development server will be accessible at http://127.0.0.1:8000/.


Accessing the Admin Panel
Visit http://127.0.0.1:8000/admin/.
Log in with the superuser credentials created earlier.

Usage
Visit http://127.0.0.1:8000/ to access the traveling website.



