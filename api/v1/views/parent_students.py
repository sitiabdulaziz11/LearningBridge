#!/usr/bin/env python3
"""objects that handle RestFul API actions for Parent - Students"""
from models.student_models import Student
from models.parent_models import Parent
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from api.v1.views.utils import token_required, require_user_class
from flasgger.utils import swag_from


@app_views.route("/parents/<parent_id>/students", methods=["GET"],
                 strict_slashes=False)
@swag_from('documentation/parent_students/get_parent_students.yml',
           methods=['GET'])
@token_required
@require_user_class("Parent")
def get_parent_students(parent_id, user):
    """
    Retrieves the list of all Student objects of a Parent
    """
    students = [student.to_dict() for student in user.students]
    return make_response(jsonify(students), 200)


@app_views.route(
    "/parents/<parent_id>/students/<student_id>", methods=["POST"],
    strict_slashes=False
)
@swag_from('documentation/parent_students/link_parent_student.yml',
           methods=['POST'])
@token_required
@require_user_class("Administrator")
def link_parent_student(parent_id, student_id, user):
    """
    Links a Student object to a Parent
    """
    parent = storage.get(Parent, parent_id)

    if not parent:
        abort(404)

    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    if student in parent.students:
        return make_response(jsonify(student.to_dict()), 200)
    else:
        parent.students.append(student)
        student.parent_id = parent_id

    storage.save()
    return make_response(jsonify(student.to_dict()), 201)


@app_views.route(
    "/parents/<parent_id>/students/<students_id>",
    methods=["DELETE"],
    strict_slashes=False
)
@swag_from('documentation/parent_students/unlink_parent_student.yml',
           methods=['DELETE'])
@token_required
@require_user_class("Administrator")
def unlink_parent_student(parent_id, student_id, user):
    """
    Unlinks a Student object from a Parent
    """
    parent = storage.get(Parent, parent_id)

    if not parent:
        abort(404)

    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    if student not in parent.students:
        abort(404)
    parent.students.remove(student)

    storage.save()
    return make_response(jsonify({}), 200)
