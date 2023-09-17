# To-Do-Django

This is a simple To-Do list application built with Django, a high-level Python web framework.
This app allows users to create, manage, and organize their tasks efficiently.

Features:

User Authentication--> Users can sign up, log in, and log out. User accounts ensure that each user's tasks are private and secure.

Task Management--> Users can create, update, delete, and mark tasks as complete. Tasks can have titles, descriptions, due dates, and priority levels.

Task Filtering--> Users can filter tasks by status (completed or not completed), due date, and priority level.

User-friendly Interface--> The app is designed with a clean and intuitive user interface to make task management straightforward.

Installation:

1) Clone this repository to your local machine: git clone https://github.com/your-username/todo-app-django.git
2) Navigate to the project directory: cd Django-todo
3) Create a virtual environment (optional but recommended): python -m venv venv
4) Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS and Linux: source venv/bin/activate
5) Install the project dependencies: pip install -r requirements.txt
6) Apply database migrations: python manage.py migrate
7) Create a superuser account: python manage.py createsuperuser
8) Start the development server: python manage.py runserver
9) Access the application in your web browser at "http://localhost:8000".

Usage
1. Open your web browser and go to http://localhost:8000.
2. Sign up for a new account or log in with your existing credentials.
3. Once logged in, you can start creating and managing your tasks.
