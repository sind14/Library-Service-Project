# Library Service Project

This is a Django REST API project for managing books, users, and borrowings in a library.

---

## Table of Contents

- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Custom Endpoints](#custom-endpoints)
- [Testing and Coverage](#testing-and-coverage)
- [Swagger / API Documentation](#swagger--api-documentation)

---

## Installation

Clone the repository:

```
git clone <repo-url>
cd Library-Service-Project
```

Create and activate a virtual environment:

```
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # Linux / Mac
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a ```.env``` file in the project root:

```
SECRET_KEY="your-secret-key"
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

---

## Running the Project

Apply migrations:

```
python manage.py migrate
```

Create a superuser

```
python manage.py createsuperuser
```

Run the development server:

```
python manage.py runserver
```

---

## API Endpoints

Books

| Method | URL              | Description          |
| ------ | ---------------- | -------------------- |
| GET    | /api/books/      | List all books       |
| POST   | /api/books/      | Create a new book    |
| GET    | /api/books/<id>/ | Retrieve book detail |

Users

| Method | URL              | Description          |
| ------ | ---------------- | -------------------- |
| GET    | /api/users/      | List all users       |
| POST   | /api/users/      | Create a new user    |
| GET    | /api/users/<id>/ | Retrieve user detail |

Borrowings

| Method | URL                   | Description                                  |
| ------ | --------------------- | -------------------------------------------- |
| GET    | /api/borrowings/      | List borrowings (user-specific if not staff) |
| POST   | /api/borrowings/      | Create borrowing for a book                  |
| GET    | /api/borrowings/<id>/ | Retrieve borrowing detail                    |

---

## Authentication

JWT authentication is used. Obtain a token using:

```
POST /api/token/
```

Request body:

```
{
    "username": "user@example.com",
    "password": "password123"
}
```

---

## Custom Endpoints

The Borrowings API has query parameters:

●```is_active=true``` → returns borrowings not yet returned

●```is_active=false``` → returns borrowings that are returned

Example:

```
GET /api/borrowings/?is_active=true
```

---

## Testing and Coverage

Run tests:

```
pytest
```

Check test coverage:

```
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```

All models, serializers, and views are fully tested.

---

## Swagger / API Documentation

Swagger UI is available at:

```
/api/docs/swagger/
```

Redoc UI is available at:

```
/api/docs/redoc/
```

Open these URLs in a browser while the server is running to explore endpoints, parameters, and request/response schemas.

---

## Notes

● Use ```.env``` for sensitive configuration like ```SECRET_KEY``` and ```DATABASE_URL```.

● Custom actions (like filtering borrowings by ```is_active```) are fully documented in Swagger.

● All tests and coverage reports ensure stable development.

---