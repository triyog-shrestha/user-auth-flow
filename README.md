# Wsg

this is a small Django application for user registration, login, logout, and post management. Authenticated users can create posts, view the feed, and remove their own content when they have the required permission.

## Features

- User sign up and login
- Logout flow
- Create posts for authenticated users
- Delete posts with permission checks
- Simple responsive UI built with Django templates and Bootstrap

## Requirements

- Python 3
- Django
- `django-crispy-forms`

## Setup

1. Create and activate a virtual environment.
2. Install the project dependencies.
3. Run database migrations.
4. Start the development server.

Example commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install Django django-crispy-forms
python manage.py migrate
python manage.py runserver
```

## Project Structure

- `main/` contains the app logic, templates, static files, forms, and views.
- `website/` contains the Django project configuration.
- `manage.py` is the Django management entry point.

## Notes

- The SQLite database file is ignored by Git.
- Template styling lives in `main/static/main/styles.css`.
- Navigation and post actions are rendered in `main/templates/main/base.html` and `main/templates/main/home.html`.
