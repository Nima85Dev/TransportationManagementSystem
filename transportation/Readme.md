1-Transportation Management System
    A web-based Transportation Management System built with Django. The system allows authenticated users to manage couriers, customers, transports, and deliveries. It includes user registration, profile editing, and password management features.

2- Project Overview
    The goal of this project is to optimize logistics for transportation. It offers features for managing user accounts as well as essential functions including scheduling transports, controlling delivery staff, monitoring delivery results, and keeping track of customers.

3- Features
    3.1- User Authentication (accounts app)
            User registration with profile image, gender, and initial credit
            Login/logout functionality
            Profile view and edit
            Password change
            CAPTCHA validation on registration

    3.2- Affairs Management (affairs app)
            Courier Management
            List, add, update, and delete couriers
            Customer Management
            List, add, update, and delete customers
            Transport Management
            Manage transportation records with source/destination, courier, vehicle, and customer info
            Delivery Tracking
            Track success of deliveries and assign couriers

    3.3- Access Control
            Login required for all CRUD operations
            Public access limited to registration and login views

4- Technologies Used
        Backend: Python 3, Django 5
        Database: SQLite (default, can be replaced)
        Frontend: HTML templates (Django template engine)
        Forms: Django Forms with validation
        Security: Django Auth system, CAPTCHA (via django-simple-captcha)

5- Installation Instructions
        Install all the dependencies in the Requirements.txt (pip install -r requirements.txt)