# Student Result Management System - Backend

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Student Result Management System is a backend API designed to manage student results, allowing parents to view their children's academic performance and teachers to upload and manage student results. The API supports user authentication, CRUD operations for students, teachers, and results, and relationship management between parents, students, and teachers.

## Features

- User Authentication (Registration, Login)
- Role-based Access Control (Parent, Teacher)
- CRUD Operations for Students
- CRUD Operations for Teachers
- CRUD Operations for Results
- Relationship Management between Parents and Students
- Relationship Management between Teachers and Students
- Secure API Endpoints with JWT Authentication

## Technologies Used

- Python
- Flask
- SQLAlchemy
- MySQL
- Flask-Migrate

## Setup and Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/student-result-management-backend.git
    cd student-result-management-backend
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following environment variables:

    ```env
    LB_USER=database_user
    LB_PWD=database_user_password
    LB_HOST=database_host
    LB_DB=database
    ```

5. **Run the application:**

    ```sh
    python3 -m api.v1.app
    ```

## API Documentation

### User Authentication

- **Register a new user**

    ```http
    POST /auth/register
    ```

    Request Body:

    ```json
    {
        "username": "user123",
        "password": "password",
        "role": "parent"  // or "teacher"
    }
    ```

- **Login a user**

    ```http
    POST /auth/login
    ```

    Request Body:

    ```json
    {
        "username": "user123",
        "password": "password"
    }
    ```

- **Protected route example**

    ```http
    GET /protected
    ```

    Headers:

    ```http
    Authorization: Bearer <JWT_TOKEN>
    ```

### Student Management

- **Create a new student**

    ```http
    POST /students
    ```

    Request Body:

    ```json
    {
        "name": "John Doe",
        "age": 12,
        "class": "6A"
    }
    ```

- **Get all students**

    ```http
    GET /students
    ```

- **Get a student by ID**

    ```http
    GET /students/:id
    ```

- **Update a student by ID**

    ```http
    PUT /students/:id
    ```

    Request Body:

    ```json
    {
        "name": "John Doe",
        "age": 13,
        "class": "7A"
    }
    ```

- **Delete a student by ID**

    ```http
    DELETE /students/:id
    ```

### Teacher Management

- **Create a new teacher**

    ```http
    POST /teachers
    ```

    Request Body:

    ```json
    {
        "name": "Jane Smith",
        "subject": "Mathematics"
    }
    ```

- **Get all teachers**

    ```http
    GET /teachers
    ```

- **Get a teacher by ID**

    ```http
    GET /teachers/:id
    ```

- **Update a teacher by ID**

    ```http
    PUT /teachers/:id
    ```

    Request Body:

    ```json
    {
        "name": "Jane Smith",
        "subject": "Physics"
    }
    ```

- **Delete a teacher by ID**

    ```http
    DELETE /teachers/:id
    ```

### Result Management

- **Create a new result**

    ```http
    POST /results
    ```

    Request Body:

    ```json
    {
        "student_id": 1,
        "subject": "Mathematics",
        "score": 95
    }
    ```

- **Get results for a student**

    ```http
    GET /students/:student_id/results
    ```

- **Update a result by ID**

    ```http
    PUT /results/:id
    ```

    Request Body:

    ```json
    {
        "subject": "Mathematics",
        "score": 97
    }
    ```

- **Delete a result by ID**

    ```http
    DELETE /results/:id
    ```

### Relationship Management

- **Link a parent to a student**

    ```http
    POST /parents/:parent_id/students/:student_id
    ```

- **Unlink a parent from a student**

    ```http
    DELETE /parents/:parent_id/students/:student_id
    ```

- **Link a teacher to a student**

    ```http
    POST /teachers/:teacher_id/students/:student_id
    ```

- **Unlink a teacher from a student**

    ```http
    DELETE /teachers/:teacher_id/students/:student_id
    ```

## Deployment

1. **Set up a production database and update the `DATABASE_URL` in your environment variables.**

2. **Ensure all environment variables are set for production.**

3. **Build and run the application using a production server (e.g., Gunicorn):**

    ```sh
    gunicorn -w 4 api.v1.app:app
    ```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
