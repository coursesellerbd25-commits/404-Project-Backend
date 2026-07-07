# 404 Assessment Backend

Backend API for the **404 Assessment Project**, built with **Django, Django REST Framework, JWT Authentication, and PostgreSQL/SQLite**.

The backend provides APIs for:

- User authentication
- Task management
- Kanban workflow
- Date-based filtering
- Image uploads
- Polygon annotation management

---

# Live API

Backend API:

```
(Add deployed backend URL here)
```

Frontend:

```
(Add deployed frontend URL here)
```

---

# Project Overview

This backend powers a full-stack productivity and annotation platform.

The system contains two main modules:

## Task Management

Users can:

- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Filter tasks by date
- Manage Kanban statuses

## Image Annotation

Users can:

- Upload images
- Store image information
- Create polygon annotations
- Retrieve annotations
- Delete annotations
- Persist annotation data after refresh

---

# Features

## Authentication

- JWT-based authentication
- Login endpoint
- Token refresh support
- Protected API routes

---

## Task API

Implemented using Django REST Framework.

Features:

- Task CRUD operations
- Status management

Example statuses:

```
todo
in_progress
done
```

- Priority levels
- Tags
- Due dates
- Date filtering

---

## Annotation API

Features:

- Image upload
- Image storage
- Polygon creation
- Polygon retrieval
- Polygon deletion

Polygon coordinates are stored as JSON:

Example:

```json
{
    "points": [
        [20,40],
        [90,40],
        [70,100]
    ]
}
```

---

# Tech Stack

## Backend

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL / SQLite
- Pillow
- Django CORS Headers

---

# Folder Structure

```
backend/
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── annotations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── media/
│   └── images/
│
├── requirements.txt
├── manage.py
└── README.md
```

---

# Database Models

## Task Model

Stores task information.

Example fields:

```
title
description
status
priority
tags
due_date
created_at
```

---

## Image Model

Stores uploaded images.

Fields:

```
image
filename
uploaded_at
```

---

## Polygon Model

Stores annotation coordinates.

Fields:

```
image
points
created_at
```

Relationship:

```
Image
 |
 └── Many Polygons
```

---

# API Endpoints

## Authentication

### Login

```
POST /api/login/
```

Response:

```json
{
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token"
}
```

---

### Refresh Token

```
POST /api/token/refresh/
```

---

# Task Endpoints

## Get Tasks

```
GET /api/tasks/
```

---

## Filter Tasks By Date

```
GET /api/tasks/?date=2026-07-10
```

---

## Create Task

```
POST /api/tasks/
```

---

## Update Task

```
PUT /api/tasks/<id>/
```

---

## Delete Task

```
DELETE /api/tasks/<id>/
```

---

# Annotation Endpoints

## Upload Image

```
POST /api/annotations/upload/
```

---

## Create Polygon

```
POST /api/annotations/polygon/
```

Example:

```json
{
    "image":1,
    "points":[
        [20,40],
        [90,40],
        [70,100]
    ]
}
```

---

## Get Polygon List

```
GET /api/annotations/polygon/list/?image=1
```

---

## Delete Polygon

```
DELETE /api/annotations/polygon/<id>/
```

---

# Installation

Clone repository:

```bash
git clone <backend-repository-url>
```

Move into backend:

```bash
cd backend
```

---

# Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create:

```
.env
```

Example:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_database_url

ALLOWED_HOSTS=localhost,127.0.0.1
```

---

# Database Setup

Run migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# Create Admin User

```bash
python manage.py createsuperuser
```

---

# Run Development Server

```bash
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# Media Configuration

Uploaded images are stored inside:

```
media/images/
```

During development:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

---

# Deployment

The backend can be deployed using:

- Render
- Railway
- AWS
- DigitalOcean

Production checklist:

- Set DEBUG=False
- Configure allowed hosts
- Configure database
- Configure media storage
- Add CORS allowed frontend domain
- Set environment variables

---

# Challenges

During development, the main challenges were:

## JWT Authentication

Managing secure login flow and protecting API endpoints.

## Kanban Synchronization

Keeping frontend drag-and-drop updates synchronized with backend data.

## Date Filtering

Implementing dynamic filtering through query parameters.

## Polygon Storage

Saving coordinate arrays efficiently.

## Image Handling

Managing image upload and serving uploaded files.

---

# Solutions

Solutions implemented:

- Django REST Framework generic views for reusable CRUD APIs
- Simple JWT for authentication
- Query parameters for dynamic filtering
- JSONField for polygon coordinate storage
- Separate applications for tasks and annotations
- Modular serializers and API services

---

# Package Versions

Main dependencies:

```
Python 3.x
Django
Django REST Framework
djangorestframework-simplejwt
django-cors-headers
Pillow
PostgreSQL
```

Exact versions are available in:

```
requirements.txt
```

---

# Security Considerations

Implemented:

- JWT authentication
- Protected API endpoints
- Environment variables
- CORS configuration
- Django validation

---

# Future Improvements

Possible enhancements:

- User-specific tasks
- Multiple annotation labels
- Polygon editing
- Annotation history
- Cloud image storage
- Automated tests
- API documentation with Swagger

---

# Author

**Sultana Jahan Tahmina**

Full Stack Web Developer

GitHub: https://github.com/coursesellerbd25-commits

LinkedIn: www.linkedin.com/in/sultana-jahan-tahmina-621aa2243

Portfolio: https://coursesellerbd25-commits.github.io/My-Portfolio-2025/

Email: sultanajahantahmina19@gmail.com