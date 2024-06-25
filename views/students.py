# i want to do authentication for the student
"""This module defines all the paths for the user moijdule"""
import jwt as pyjwt
from models.student_models import Student
from models import storage
from views import app_views, token_required, auth
from flask import jsonify, request, session
from datetime import datetime, timedelta
from flask import current_app


@app_views.route('/student', methods=['POST'], strict_slashes=False)
def create_student():
    """
    Create a new student
    ---
    tags:
      - Users
    summary: Create a new student
    requestBody:
      description: User object that needs to be added
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Student'
    responses:
      '201':
        description: User created
        content:
          application/json:
            schema:
      '400':
        description: Invalid input
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """
    required_fields = ['firstname', 'middilename', 'lastname', 'email',
                       'password', 'birth_date', 'image_file', 'phone_no',
                       'conduct',
                       'section']
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    student = Student(**data)
    student.save()
    return jsonify(student.to_dict()), 201
# user login


@auth.route('/login', methods=['POST'], strict_slashes=False)
def user_login():
    """
    User Login
    ---
    tags:
      - Users
    summary: User Login
    requestBody:
      description: User object that needs to be added
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/User'
    responses:
      '201':
        description: User logged in
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
      '400':
        description: Invalid input
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
    """
    secret_key = current_app.config['SECRET_KEY']
    print(secret_key)
    required_fields = ['email', 'password']
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing {', '.join(missing_fields)}"}), 400

    email, password = data['email'], data['password']
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    student = storage.get_by_email(Student, email)
    if not student:
        return jsonify({"error": "User not found or Invalid password"}), 400

    token_payload = {
        "user_name": student.firstname,
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = pyjwt.encode(token_payload, secret_key)
    session['logged_in'] = True
    return jsonify({"token": token})
    return jsonify({"error": "Error generating token"}), 500


@ app_views.route('/students', methods=['GET'], strict_slashes=False)
@token_required
def get_students():
    """
    Get all users
    ---
    tags:
      - Users
    operations:
      - httpMethod: GET
        summary: Retrieve all users
        responses:
          '200':
            description: List of all users
            content:
              application/json:
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/User'
    """
    if session.get('logged_in') is None or not session['logged_in']:
        return jsonify({"error": "Unauthorized"}), 401

    students = storage.all(Student)
    students = [user.to_dict() for user in students.values()]
    return jsonify(students), 200
