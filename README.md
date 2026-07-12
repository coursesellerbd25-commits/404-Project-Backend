# 404 Assessment Backend

Backend API for the **404 Assessment Project**, built with **Django, Django REST Framework, JWT Authentication, SQLite, and Cloudinary**.

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
https://four04-project-backend-1.onrender.com
```

Frontend:

```
https://404-project-frontend.vercel.app/
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

Implemented using Django Simple JWT.

Features:

- Email and password authentication
- JWT access token
- JWT refresh token
- Protected API routes
- Custom JWT serializer for email login
- Extended JWT lifetime for demo usage

JWT Configuration:

The default Django authentication system uses username-based login. 
For this project, Simple JWT was customized to authenticate users using email and password.

Configuration:

- Access token lifetime: 7 days
- Refresh token lifetime: 30 days

Example:

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}
```

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
- SQLite Database
- Cloudinary
- Pillow
- Django CORS Headers
- python-dotenv

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
├── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
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
Example fields:

title
status
priority
selected_date
due_date
tags
created_at
updated_at

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

## Account API

```
POST /api/login/
```

Login using email and password:

The backend accepts email instead of Django's default username authentication.

### Login

```json
{
    "email": "admin@gmail.com",
    "password": "MyAdmin123!"
}
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

# Development Environment

Example environment:

Python: 3.13
Node: 20+
Frontend: React + Vite
Backend: Django + Django REST Framework

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

CLOUDINARY_CLOUD_NAME=your_cloud_name

CLOUDINARY_API_KEY=your_api_key

CLOUDINARY_API_SECRET=your_api_secret
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

# Media Storage

Uploaded images are stored using Cloudinary.

The backend uses:

- django-cloudinary-storage
- Cloudinary API
- Environment variables for credentials

Uploaded images are automatically hosted through Cloudinary URLs instead of local media storage.

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
- Configure Cloudinary storage
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

## Cloudinary Migration

Initially images were stored locally. 
The storage system was migrated to Cloudinary to support production deployment and persistent image URLs.

## Email Based JWT Authentication

Customizing Simple JWT because Django default authentication uses username.

---

# Solutions

Solutions implemented:

- Django REST Framework generic views for reusable CRUD APIs
- Simple JWT for authentication
- Query parameters for dynamic filtering
- JSONField for polygon coordinate storage
- Separate applications for tasks and annotations
- Modular serializers and API services
- Integrated Cloudinary storage for uploaded images
- Customized Simple JWT authentication to support email login
- Configured extended JWT expiration for demo usability

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
SQLite
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
- API documentation with Swagger

---

# Author

**Sultana Jahan Tahmina**

Full Stack Web Developer

GitHub: https://github.com/coursesellerbd25-commits

LinkedIn: www.linkedin.com/in/sultana-jahan-tahmina-621aa2243

Portfolio: https://coursesellerbd25-commits.github.io/My-Portfolio-2025/

Email: sultanajahantahmina19@gmail.com