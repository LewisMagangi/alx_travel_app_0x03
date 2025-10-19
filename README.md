# ALX Travel App 0x02

A comprehensive Django-based travel listing platform with robust API documentation and database configuration.

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Learning Objectives](#-learning-objectives)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [API Documentation](#-api-documentation)
- [Database Setup](#️-database-setup)
- [Running the Application](#-running-the-application)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 About the Project

The **alx_travel_app_0x00** project is a real-world Django application that serves as the foundation for a travel listing platform. This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools to ensure API documentation and maintainable configurations.

The aim is to equip learners with industry-standard best practices for starting and managing Django-based projects efficiently. This milestone teaches you to set up a scalable backend, integrate MySQL for database management, and use Swagger for automated API documentation.

## 🎯 Learning Objectives

As a professional developer, this task will enable you to:

### Master Advanced Project Initialization

- Learn to bootstrap Django projects with modular, production-ready configurations
- Employ environment variable management for secure and scalable settings

### Integrate Key Developer Tools

- Set up and use Swagger (via drf-yasg) for API documentation
- Implement CORS headers and MySQL configurations for robust API interactions

### Collaborate Effectively Using Git

- Structure your projects for team collaboration with a version-controlled setup

### Adopt Industry Best Practices

- Follow best practices in managing dependencies, database configurations, and application structure

## ✨ Features

- **Django REST Framework**: Full-featured REST API capabilities
- **Swagger Documentation**: Automatic API documentation at `/swagger/`
- **MySQL Database**: Robust database configuration with environment variables
- **CORS Support**: Cross-Origin Resource Sharing for frontend integration
- **Celery Integration**: Ready for background task processing
- **Environment Management**: Secure configuration using django-environ
- **Modular Structure**: Organized app structure for scalability

## 🛠 Technology Stack

- **Backend Framework**: Django 4.2+
- **API Framework**: Django REST Framework
- **Database**: MySQL with PyMySQL adapter
- **Documentation**: drf-yasg (Swagger/OpenAPI)
- **Task Queue**: Celery with RabbitMQ
- **Environment Management**: django-environ
- **CORS Handling**: django-cors-headers

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- MySQL Server
- Git
- Virtual environment tool (venv, virtualenv, or conda)

### Knowledge Requirements

- Familiarity with Django and Django REST Framework
- Knowledge of MySQL and database management
- Understanding of version control using Git
- Basic grasp of environment variable management

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/LewisMagangi/alx_travel_app.git
   cd alx_travel_app
   ```

2. **Create and activate virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Create environment file**

   ```bash
   cp .env.example .env
   ```

2. **Configure environment variables**
   Edit the `.env` file with your specific configurations:

   ```env
   # Django Settings
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Database Configuration
   DB_NAME=alx_travel_app
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306

   # Email Configuration (Optional)
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password

   # Celery Configuration
   CELERY_BROKER_URL=pyamqp://guest@localhost//
   CELERY_RESULT_BACKEND=rpc://
   ```

## 📚 API Documentation

The API documentation is automatically generated using Swagger and is available at:

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`
- **JSON Schema**: `http://localhost:8000/swagger.json`

### Key Features of API Documentation

- Interactive API testing interface
- Automatic schema generation
- Request/response examples
- Authentication documentation
- Model schemas

## 🗄️ Database Setup

1. **Create MySQL database**

   ```sql
   CREATE DATABASE alx_travel_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

4. **Load initial data (if available)**

   ```bash
   python manage.py loaddata fixtures/initial_data.json
   ```

## 🚀 Running the Application

1. **Start the development server**

   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Main application: `http://localhost:8000/`
   - Admin interface: `http://localhost:8000/admin/`
   - API documentation: `http://localhost:8000/swagger/`

3. **Start Celery worker (for background tasks)**

   ```bash
   celery -A alx_travel_app worker --loglevel=info
   ```

4. **Start Celery beat (for scheduled tasks)**

   ```bash

   celery -A alx_travel_app beat --loglevel=info
   ```

## 📁 Project Structure

``` text
alx_travel_app/
├── alx_travel_app/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── listing/                 # Listings app
│   ├── migrations/          # Database migrations
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Data models
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   ├── urls.py              # App URL configuration
│   └── tests.py             # Unit tests
├── static/                  # Static files
├── media/                   # Media files
├── templates/               # HTML templates
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables example
├── .gitignore               # Git ignore rules
├── manage.py                # Django management script
└── README.md                # Project documentation
```

## 🔧 Key Configuration Files

### Dependencies (requirements.txt)

``` text
django>=4.2.0,<5.0.0
djangorestframework>=3.14.0
django-cors-headers>=4.0.0
django-environ>=0.10.0
drf-yasg>=1.21.0
PyMySQL>=1.0.0
celery>=5.2.0
redis>=4.5.0
```

### Environment Variables (.env)

- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode setting
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`: Database credentials
- `CELERY_BROKER_URL`: Celery broker URL

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test listing

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Set up static file serving
- [ ] Configure database for production
- [ ] Set up proper logging
- [ ] Configure Celery with production broker
- [ ] Set up monitoring and error tracking

### Environment-Specific Settings

Create separate settings files for different environments:

- `settings/development.py`
- `settings/staging.py`
- `settings/production.py`

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards

- Follow PEP 8 style guide
- Write comprehensive tests
- Update documentation for new features
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [documentation](README.md)
2. Search existing [issues](https://github.com/LewisMagangi/alx_travel_app/issues)
3. Create a new issue with detailed description
4. Contact the development team

## 🏗️ Roadmap

- [ ] User authentication and authorization
- [ ] Listing management functionality
- [ ] Search and filtering capabilities
- [ ] Payment integration
- [ ] Email notifications
- [ ] Mobile API optimization
- [ ] Performance monitoring
- [ ] Automated testing pipeline

## 👨‍💻 Authors

- **Lewis Magangi** - *Initial work* - [LewisMagangi](https://github.com/LewisMagangi)

## 🙏 Acknowledgments

- ALX Software Engineering Program
- Django and DRF communities
- All contributors and testers

---

For more information about the ALX Software Engineering Program, visit [ALX](https://www.alxafrica.com/).
