!/usr/bin/env python3
""" objects that handle all default RestFul API actions for Reviews """
from models.student import Student
from models.parent import Parent
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from api.views.utils import token_required, require_user_class


@app_views.route('/parents/<parent_id>/students', methods=['GET'],
                 strict_slashes=False)
@token_required
def get_students(parent_id, user):
    """
    Retrieves the list of all Student objects of a Parent
    """
    parent = storage.get(Parent, parent_id)

    if not parent:
        abort(404)

    students = [student.to_dict() for student in parent.students]

    return make_response(jsonify(students), 200)


@app_views.route('/parents/<parent_id>/students', methods=['POST'],
                 strict_slashes=False)
@token_required
@require_user_class("Administrator")
def post_student(parent_id, user):
    """
    Creates a Student object and link it to a Parent
    """
    parent = storage.get(Parent, parent_id)

    if not parent:
        abort(404)

    required_fields = ['firstname', 'middlename', 'lastname', 'email',
                       'password', 'birth_date']
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    data['parent_id'] = parent_id

    student = Student(**data)
    student.save()

    return make_response(jsonify(student.to_dict()), 201)
