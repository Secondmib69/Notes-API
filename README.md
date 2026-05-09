# Note API

A Django REST Framework API for creating, managing, searching, and organizing personal notes with tags. The project includes JWT cookie authentication, user registration/login endpoints, pagination, filtering/search, and interactive OpenAPI documentation.

## Features

- User registration and authentication with `dj-rest-auth`, `django-allauth`, and Simple JWT
- Create, list, update, and delete notes
- Tags support with `django-taggit`
- Search notes by title, content, tag name, or username
- Ordering by created and updated dates
- Cursor pagination for notes and page-number pagination for users
- Staff users can view all notes and manage user records
- Swagger/OpenAPI docs powered by `drf-spectacular`
- Docker support for quick local setup

## Tech Stack

- Python 3.12
- Django 6
- Django REST Framework
- SQLite
- Simple JWT
- django-taggit
- drf-spectacular
- Docker

## Project Structure

```text
.
├── core/              # Django project settings and root URLs
├── note/              # Notes app: models, serializers, views, permissions, URLs
├── Dockerfile         # Container setup
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.12+
- pip
- Docker, optional

### Local Setup

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create an admin user, optional:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Running With Docker

Build and run the container:

```bash
docker build -t note-api .
docker run -p 8000:8000 note-api
```

The Docker command runs migrations automatically before starting the server.

## API Documentation

After starting the server, open:

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`

## Main Endpoints

### Notes

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/notes/` | List authenticated user's notes |
| `POST` | `/notes/` | Create a note |
| `GET` | `/notes/<id>/` | Retrieve one note |
| `PUT/PATCH` | `/notes/<id>/` | Update one note |
| `DELETE` | `/notes/<id>/` | Delete one note |

### Users

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/users/` | List users, staff/superuser restricted |
| `POST` | `/users/` | Create user, staff/superuser restricted |
| `GET` | `/users/<id>/` | Retrieve user details |
| `GET` | `/users/<id>/notes/` | List notes for a specific user |

### Authentication

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/auth/registration/` | Register a new account |
| `POST` | `/auth/login/` | Log in and receive JWT cookies |
| `POST` | `/auth/logout/` | Log out |
| `POST` | `/auth/password/reset/` | Request password reset |
| `POST` | `/auth/password/reset/confirm/<uidb64>/<token>/` | Confirm password reset |

## Example Note Payload

```json
{
  "title": "Meeting notes",
  "content": "Discuss project milestones and next steps.",
  "tags": ["work", "planning"]
}
```

## Query Parameters

The notes list supports search and ordering:

```text
/notes/?search=planning
/notes/?ordering=-created
/notes/?ordering=updated
```

## Development Notes

- The default database is SQLite.
- `db.sqlite3`, `.env`, virtual environments, cache files, and editor files are ignored by `.gitignore`.
- For production, move secrets such as `SECRET_KEY` into environment variables, set `DEBUG=False`, configure `ALLOWED_HOSTS`, and enable secure JWT cookies.

## License

No license has been added yet. Add one before publishing if you want to define how others can use this project.
