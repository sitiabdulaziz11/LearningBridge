#!/usr/bin/env python3
"""objects that handle RestFul API actions for Teacher - Students"""
from models.student_models import Student
from models.teacher_models import Teacher
from models.parent_models import Parent
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from api.v1.views.utils import token_required, require_user_class
from flasgger.utils import swag_from


@app_views.route(
    "/teachers/<teacher_id>/students", methods=["GET"], strict_slashes=False
)
@swag_from('documentation/students_teachers/get_teacher_students.yml',
           methods=['GET'])
@token_required
def get_teacher_students(teacher_id, user):
    """
    Retrieves the list of all Students of a Teacher
    """
    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    students = [student.to_dict() for student in teacher.students]

    return make_response(jsonify(students), 200)


@app_views.route(
    "/teachers/<teacher_id>/students/<student_id>",
    methods=["POST"],
    strict_slashes=False
)
@swag_from('documentation/students_teachers/link_student_teacher.yml',
           methods=['POST'])
@token_required
@require_user_class("Teacher")
def link_student_teacher(teacher_id, student_id, user):
    """
    Links a Student object to a Teacher
    """
    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    if student in teacher.students:
        return make_response(jsonify(student.to_dict()), 200)
    else:
        teacher.students.append(student)

    storage.save()
    return make_response(jsonify(student.to_dict()), 201)


@app_views.route(
    "/teachers/<teacher_id>/students/<students_id>",
    methods=["DELETE"],
    strict_slashes=False,
)
@swag_from('documentation/students_teachers/unlink_student_teacher.yml',
           methods=['DELETE'])
@token_required
@require_user_class("Administrator")
def unlink_student_teacher(teacher_id, student_id, user):
    """
    Unlinks a Student object from a Teacher
    """
    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    student = storage.get(Student, student_id)

    if not student:
        abort(404)

    if student not in teacher.students:
        abort(404)
    teacher.students.remove(student)

    storage.save()
    return make_response(jsonify({}), 200)
