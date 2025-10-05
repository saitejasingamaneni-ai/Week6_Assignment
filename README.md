# Flask & Django Lab – Simple Web Applications

## Objectives
- Understand and implement basic routing, templating, and views in Flask and Django.
- Compare development workflows between a lightweight framework (Flask) and a full-featured framework (Django).
- Build and run basic web applications locally using each framework.

## Setup & Running Instructions

1. **Create and activate a virtual environment** (optional but recommended):
   
   python -m venv venv
   
   source venv/bin/activate   # Linux/macOS
   
   venv\Scripts\activate      # Windows PowerShell

   
**2. Install required packages:**

pip install Flask Django

Part 1: Flask – Simple Web Application
Project Structure:
flask_app/

  app.py
  
  templates/
    form.html
    hello.html
    
Run the Flask app:

cd flask_app

python app.py

Access in browser:

Home: http://127.0.0.1:5000/

Form: http://127.0.0.1:5000/greet

Implemented Features:

/ → Home route with "Welcome to Flask!"

/hello/<name> → Dynamic greeting using hello.html

/greet → Form to enter name and redirect to greeting

**Part 2: Django – Minimal Web Application**

i)Create project & app:

      django-admin startproject django_lab
      cd django_lab
      python manage.py startapp greetapp


ii)Configure:

      Add 'greetapp' to INSTALLED_APPS in django_lab/settings.py
      
      Add app URLs in django_lab/urls.py:
      
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', include('app.urls')),
      ]


iii)Migrate and create superuser:

      python manage.py makemigrations
      python manage.py migrate
      python manage.py createsuperuser


iv)Run the Django server:

      python manage.py runserver


v)Access in browser:

      Home: http://127.0.0.1:8000/
      
      Dynamic greeting: /greet/<name>/
      
      Messages list: /messages/
      
      Admin panel: /admin/ (login with superuser)

vi)Implemented Features:

      / → Home page with "Hello from Django!"
      
      /greet/<name>/ → Dynamic greeting using Django templates
      
      Message model with text field
      
      Registered model in admin and added entries
      
      /messages/ → View to list all messages





