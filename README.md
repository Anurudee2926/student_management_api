# Student Management API

A RESTful API built with **Python, FastAPI, SQLAlchemy, and PostgreSQL** to manage student records. The project demonstrates backend development fundamentals, database integration, request handling, and CRUD operations.

## Features

- **Create students** — add a new student record.
- **Retrieve students** — fetch student records by ID.
- **Update students** — modify existing student information.
- **Delete students** — remove student records.
- **Database integration** — persist student records in PostgreSQL using SQLAlchemy.
- **API documentation** — explore and test endpoints using FastAPI's interactive Swagger UI.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Git and GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | Retrieve student records |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PATCH | `/students/{student_id}` | Update a student's information |
| DELETE | `/students/{student_id}` | Delete a student |

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or newer
- PostgreSQL
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Anurudee2926/student_management_api.git
cd student_management_api
```

### 2. Create and activate a virtual environment

On Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Install the packages required by the project. If a `requirements.txt` file is available, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the project's dependencies individually based on the imports in the code.

### 4. Configure PostgreSQL

Create a PostgreSQL database named `student_management_db` and configure a database connection for your local environment.

**Security note:** Keep database credentials private. Do not publish real passwords or other secrets in your source code or GitHub repository.

### 5. Run the application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The API should be available at:

`http://127.0.0.1:8000`

### 6. Explore the API

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

Use Swagger UI to test the available endpoints and create, retrieve, update, or delete student records.

## Project Structure

```text
student_management_api/
├── main.py
├── database.py
├── models/
│   └── student.py
├── routers/
│   └── students.py
├── schema/
├── service/
├── mystudent.html
└── README.md
```

The folders and files serve these purposes:

- `main.py` — initializes the FastAPI application and registers the student router.
- `database.py` — configures the SQLAlchemy database connection and session management.
- `models/student.py` — defines the Student database model.
- `routers/students.py` — contains the student API endpoints.
- `schema/` — contains request and data validation schemas.
- `service/` — contains service-layer logic where applicable.
- `mystudent.html` — contains the project's HTML page.

## What I Learned

Through this project, I practised:

- Building RESTful APIs with FastAPI.
- Implementing create, read, update, and delete operations.
- Connecting a Python application to PostgreSQL.
- Using SQLAlchemy ORM to work with database records.
- Validating request data and handling API errors.
- Testing endpoints using interactive API documentation.
- Managing and publishing code with Git and GitHub.

## Future Improvements

- Add automated tests for API endpoints.
- Improve configuration using environment variables.
- Add authentication and authorization.
- Improve error handling and input validation.
- Containerize the application with Docker.

## Author

**Nurudeen Ashiat**

GitHub: [@Anurudee2926](https://github.com/Anurudee2926)
