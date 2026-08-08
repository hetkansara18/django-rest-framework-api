# 🚀 Django REST Framework (DRF) API

A backend RESTful API service developed using **Python, Django, and Django REST Framework (DRF)**.

## 🌟 Key Features
- **RESTful API Architecture:** Standardized API endpoints delivering formatted JSON responses.
- **Django REST Framework Integration:** Leverages DRF views, serializers, and status codes.
- **Database Integration:** Configured with PostgreSQL for database operations.

## 🛠️ Tech Stack
- **Backend:** Python, Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Tools:** Git, VS Code

## ⚙️ How to Run Locally

1. Clone the Repository
    ```bash
    git clone [https://github.com/hetkansara18/django-rest-framework-api.git](https://github.com/hetkansara18/django-rest-framework-api.git)
    cd Django_Rest_Framework

2. Set up Virtual Environment
    ```bash
    python -m venv env
    source env/Scripts/activate

3. Install Dependencies
    ```bash
    pip install -r requirements.txt

4. Database Configuration
Configure your PostgreSQL database credentials in django_restframework_main/settings.py:
    ```Python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'postgres',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

5. Run Migrations & Start Server
    ```bash
    python manage.py migrate
    python manage.py runserver