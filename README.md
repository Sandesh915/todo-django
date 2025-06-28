Django Multi-User To-Do Application
A simple yet powerful multi-user to-do application built with Django that allows users to manage their personal tasks with user authentication and CRUD operations.
Features

User Authentication System

User registration and login
Secure password handling
Session management
User logout functionality


Personal Task Management

Create new tasks
View all personal tasks
Edit existing tasks
Delete tasks
Tasks are ordered by creation date (newest first)


Multi-User Support

Each user has their own private task list
User isolation - users can only see and manage their own tasks
Secure user-based data filtering


Responsive Web Interface

Clean and intuitive user interface
Real-time task updates
User-friendly forms for task management



Technology Stack

Backend: Django (Python)
Database: SQLite3 (default Django database)
Frontend: HTML templates
Authentication: Django's built-in authentication system

Project Structure
TODO_DJANGO/
├── todo/
│   ├── migrations/
│   ├── templates/
│   │   ├── edit_todo.html
│   │   ├── loginn.html
│   │   ├── signup.html
│   │   └── todo.html
│   ├── __init__.py
│   ├── admin.py
│   ├── asgi.py
│   ├── models.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
Installation and Setup
Prerequisites

Python 3.8 or higher
pip (Python package installer)

Step-by-Step Installation

Clone the repository
bashgit clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app

Create a virtual environment (recommended)
bashpython -m venv todo_env
source todo_env/bin/activate  # On Windows: todo_env\Scripts\activate

Install Django
bashpip install django

Apply database migrations
bashpython manage.py makemigrations
python manage.py migrate

Create a superuser (optional, for admin access)
bashpython manage.py createsuperuser

Run the development server
bashpython manage.py runserver

Access the application

Open your web browser and navigate to http://127.0.0.1:8000/
You'll be redirected to the login page



Usage
Getting Started

Sign Up: Create a new account by visiting the signup page
Log In: Use your credentials to log into the application
Manage Tasks:

Add new tasks using the task input form
Edit existing tasks by clicking the edit option
Delete tasks you no longer need


Log Out: Safely log out when you're done

URL Structure

/ - Redirects to signup page
/signup/ - User registration
/loginn/ - User login
/todopage/ - Main todo dashboard (requires login)
/edit_todo/<int:srno>/ - Edit specific task (requires login)
/delete_todo/<int:srno>/ - Delete specific task (requires login)
/signout/ - User logout

Database Schema
TODO Model
FieldTypeDescriptionsrnoAutoFieldPrimary key, auto-incrementedtitleCharFieldTask title (max 25 characters)dateDateTimeFieldAuto-generated timestampuserForeignKeyLinks task to specific user
Security Features

Authentication Required: All todo operations require user login
User Isolation: Users can only access their own tasks
CSRF Protection: Django's built-in CSRF protection
Secure Password Handling: Uses Django's authentication system
Session Management: Secure session handling

Development
Running in Development Mode
bashpython manage.py runserver
Making Database Changes
After modifying models.py:
bashpython manage.py makemigrations
python manage.py migrate
Accessing Django Admin

Create a superuser: python manage.py createsuperuser
Visit http://127.0.0.1:8000/admin/
Log in with superuser credentials

Contributing

Fork the repository
Create a feature branch (git checkout -b feature/new-feature)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/new-feature)
Create a Pull Request

Future Enhancements

Task categories and tags
Task priority levels
Due date functionality
Task sharing between users
Email notifications
REST API for mobile app integration
Task search and filtering
Dark mode theme

Support
If you encounter any issues or have questions, please:

Check the existing issues on GitHub
Create a new issue with detailed description
Include error messages and steps to reproduce

Acknowledgments

Django framework for providing robust web development tools
Django's built-in authentication system for secure user management
SQLite for providing a lightweight database solution


Note: This is a development version. For production deployment, consider:

Using PostgreSQL or MySQL instead of SQLite
Setting up proper environment variables
Configuring static files serving
Implementing proper logging
Adding comprehensive testing
