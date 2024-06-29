from models.teacher_models import Teacher
# i want to do authentication for the student
"""This module defines all the paths for the user moijdule"""
import jwt as pyjwt
from models import storage
from views import app_views, auth
from flask import jsonify, request, session
from datetime import datetime, timedelta
from flask import current_app
from views.utils import require_user_class, token_required

@app_views.route('/teacher', methods=['POST'], strict_slashes=False)
def create_teacher():
    required_fields = ['firstname', 'middilename', 'lastname', 'email',
                       'password', 'birth_date', 'image_file', 'phone_no',
                       'conduct', 'section']
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    teacher = Teacher(**data)
    teacher.save()
    return jsonify(teacher.to_dict()), 201


@auth.route('/teacher_login', methods=['POST'], strict_slashes=False)
def teacher_login():
    secret_key = current_app.config['SECRET_KEY']
    required_fields = ['email', 'password']
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing {', '.join(missing_fields)}"}), 400

    email, password = data['email'], data['password']
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    teacher = storage.get_by_email(Teacher, email)
    if not teacher:
        return jsonify({"error": "Teacher not found or Invalid password"}), 400

    token_payload = {
        "user_name": teacher.firstname,
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = pyjwt.encode(token_payload, secret_key)
    session['logged_in'] = True
    return jsonify({"token": token})


@app_views.route('/teachers', methods=['GET'], strict_slashes=False)
@token_required
@require_user_class("Teacher")
def get_teachers(user):
    if not session.get('logged_in', False):
        return jsonify({"error": "Unauthorized"}), 401

    teachers = [teacher.to_dict() for teacher in storage.all(Teacher).values()]
    return jsonify(teachers), 200
