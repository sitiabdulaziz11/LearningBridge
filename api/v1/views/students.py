# i want to do authentication for the student
"""This module defines all the paths for the user moijdule"""

from models.student_models import Student
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, session, make_response, abort
from datetime import datetime, timedelta
from flask import current_app
from flasgger.utils import swag_from
from flask_login import login_required, current_user
from api.v1.views.user_auth import require_user_class


@app_views.route("/students", methods=["POST"], strict_slashes=False)
@swag_from('documentation/student/create_student.yml', methods=['POST'])
@login_required
@require_user_class(['Teacher', 'Administrator'])
def create_student():
    """
    Create a new student
    """
    required_fields = [
        "firstname",
        "middlename",
        "lastname",
        "email",
        "password",
        "birth_date",
        "age",
        "gender",
        "address",
        "phone_no",
        "grade",
        "section"
    ]
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    student = Student(**data)
    student.save()
    return jsonify(student.to_dict()), 201


@app_views.route("/students", methods=["GET"], strict_slashes=False)
@swag_from('documentation/student/all_students.yml', methods=['GET'])
@login_required
@require_user_class(['Teacher', 'Administrator'])
def get_students():
    """
    Get all users
    """
    print('line 55')
    students = storage.all(Student)
    students = [user.to_dict() for user in students.values()]
    return make_response(jsonify(students), 200)


@app_views.route("/students/<student_id>", methods=["GET"],
                 strict_slashes=False)
@swag_from('documentation/student/get_student.yml', methods=['GET'])
@login_required
def get_student(student_id):
    """Retrieves a student"""
    student = storage.get(Student, student_id)
    if not student:
        abort(404)
    return make_response(jsonify(student.to_dict()), 200)


@app_views.route("/students/<student_id>", methods=["DELETE"],
                 strict_slashes=False)
@swag_from('documentation/student/delete_student.yml', methods=['DELETE'])
@login_required
@require_user_class("Administrator")
def delete_student(student_id):
    """
    Deletes a user Object
    """
    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    storage.delete(student)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route("/students/<student_id>", methods=["PUT"],
                 strict_slashes=False)
@swag_from('documentation/student/update_student.yml', methods=['PUT'])
@login_required
@require_user_class(['Teacher', 'Parent', 'Administrator'])
def update_student(student_id):
    """
    Updates a student
    """
    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ["id", "email", "created_at", "updated_at"]

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(student, key, value)
    storage.save()

    return make_response(jsonify(student.to_dict()), 200)
