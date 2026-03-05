# Organization Management System

A Django REST Framework web application for managing organizations, departments, job positions, and employees. Built with Django 6, PostgreSQL, and deployed via Docker + Nginx.

## Features

- Full CRUD REST API for organizations, departments, job positions, and users
- Token-based authentication (read operations are public, write operations require auth)
- Role-based user model (Admin, Manager, Employee, Org Manager, Org Admin)
- Server-side rendered HTML pages for each resource
- Containerized deployment with Docker Compose and Nginx reverse proxy

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.2, Django REST Framework 3.16 |
| Database | PostgreSQL 16 |
| Auth | DRF Token Authentication |
| Server | Gunicorn + Nginx |
| Containerization | Docker, Docker Compose |
| Runtime | Python 3.12 |

## Project Structure

```
.
├── app/                    # Core application
│   ├── models/
│   │   ├── organization.py
│   │   ├── department.py
│   │   └── job_position.py
│   ├── views/              # DRF ViewSets
│   ├── serializers/        # DRF Serializers
│   ├── urls.py             # API router
│   └── page_urls.py        # HTML page routes
├── users/                  # Custom user app
│   ├── models.py           # Custom User model
│   ├── user_view.py        # User ViewSet
│   └── user_serializer.py
├── mysite/                 # Django project config
│   ├── settings.py
│   └── urls.py
├── templates/              # HTML templates
├── nginx/                  # Nginx config
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Data Models

### Organization
- `name` (unique) — organization name
- `description` — optional description
- `head_of_organization` — FK to User (CEO/head)
- `is_active` — active status

### Department
- `name` (unique) — department name
- `description` — responsibilities description
- `organization` — FK to Organization
- `head_of_department` — FK to User (manager)
- `is_active` — active status

### Job Position
- `title` (unique) — position title (e.g. Senior Developer, HR Coordinator)
- `description` — optional description
- `is_active` — availability status

### User (custom AbstractUser)
- `full_name`, `username`, `phone_number` (+998XXXXXXXXX format)
- `role` — one of: `ADMIN`, `MANAGER`, `EMPLOYEE`, `ORG_MANAGER`, `ORG_ADMIN`
- `department` — FK to Department
- `position` — FK to JobPosition
- `managed_organization` — FK to Organization (for admin roles)

## API Endpoints

All API endpoints are prefixed with `/api/`.

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | `/api/organization/` | No | List all organizations |
| GET | `/api/organization/{id}/` | No | Get organization detail |
| POST | `/api/organization/` | Yes | Create organization |
| PUT/PATCH | `/api/organization/{id}/` | Yes | Update organization |
| DELETE | `/api/organization/{id}/` | Yes | Delete organization |
| GET | `/api/departments/` | No | List all departments |
| GET | `/api/departments/{id}/` | No | Get department detail |
| POST | `/api/departments/` | Yes | Create department |
| PUT/PATCH | `/api/departments/{id}/` | Yes | Update department |
| DELETE | `/api/departments/{id}/` | Yes | Delete department |
| GET | `/api/jon-position/` | No | List all job positions |
| GET | `/api/jon-position/{id}/` | No | Get job position detail |
| POST | `/api/jon-position/` | Yes | Create job position |
| PUT/PATCH | `/api/jon-position/{id}/` | Yes | Update job position |
| DELETE | `/api/jon-position/{id}/` | Yes | Delete job position |
| GET | `/api/users/` | Yes | List all users |
| POST | `/api/users/` | Yes | Create user |
| PUT/PATCH | `/api/users/{id}/` | Yes | Update user |
| DELETE | `/api/users/{id}/` | Yes | Delete user |
| POST | `/api/auth/token/` | No | Obtain auth token |

### Authentication

Obtain a token by posting credentials:

```bash
curl -X POST http://localhost/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Use the token in subsequent requests:

```bash
curl -H "Authorization: Token <your_token>" http://localhost/api/organization/
```

## Web Pages

| URL | Description |
|-----|-------------|
| `/` | Home page |
| `/organizations/` | Organizations listing |
| `/departments/` | Departments listing |
| `/job-positions/` | Job positions listing |
| `/users/` | Users listing |

## Setup & Installation

### Prerequisites

- Docker and Docker Compose installed

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=cw_claude
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST_PORT=5432

NGINX_PORT=80
```

### Run with Docker Compose

```bash
# Clone the repository
git clone <repo-url>
cd 00016908

# Create .env file (see above)
cp .env.example .env  # edit as needed

# Build and start all services
docker compose up -d --build

# The app will be available at http://localhost (or the port set in NGINX_PORT)
```

On startup, the web container automatically runs:
1. `python manage.py migrate` — applies database migrations
2. `python manage.py collectstatic` — collects static files
3. Starts Gunicorn on port 8000 (proxied by Nginx)

### Run Locally (without Docker)

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables or create .env file

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### Create a Superuser (Docker)

```bash
docker compose exec web python manage.py createsuperuser
```

## Django Admin

The Django admin interface is available at `/admin/`. Log in with your superuser credentials to manage all models via the web UI.

## Docker Services

| Service | Description | Port |
|---------|-------------|------|
| `db` | PostgreSQL 16 database | `DB_HOST_PORT:5432` |
| `web` | Django + Gunicorn app | Internal 8000 |
| `nginx` | Nginx reverse proxy | `NGINX_PORT:80` |

## Dependencies

```
Django==6.0.2
djangorestframework==3.16.1
psycopg2-binary==2.9.11
gunicorn==23.0.0
python-dotenv>=1.0.0
asgiref==3.11.1
sqlparse==0.5.5
tzdata==2025.3
```
