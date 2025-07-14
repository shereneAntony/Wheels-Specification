# Wheels-Specification

# Setup instructions:
- Create Virtual environment and activate it.
- Install dependcies needed.
- Create your project and create your app inside it.
- In settings.py file do the following settings:
           >Add database details,
           >Add your app name in installed apps.
           >Do necessary settings for cors-headers, rest frameworks.
  
# Tech Stack:
- Backend Framework: Django 5.2 + Django REST Framework
- Database: MySQL
- API Testing: Postman
- Language: Python 3.11+
- Filtering: django-filter

# List of implemented API's:
1) POST method:
   Adds a new wheel specification entry with validation for required fields and date format.
3) GET method with filter:
   Retrieves all wheel specifications or filters them based on:
  - form_number
  - submitted_by
  - submitted_date


