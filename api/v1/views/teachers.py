from models.teacher_models import Teacher
import jwt as pyjwt
from models import storage
from api.v1.views import app_views, auth
from flask import jsonify, request, session, abort, make_response
from datetime import datetime, timedelta
from flask import current_app
from api.v1.views.utils import require_user_class, token_required
from flasgger.utils import swag_from


@app_views.route("/teachers", methods=["POST"], strict_slashes=False)
@swag_from('documentation/teacher/create_teacher.yml', methods=['POST'])
def create_teacher():
    required_fields = [
        "firstname",
        "middilename",
        "lastname",
        "email",
        "password",
        "phone_no",
        "hire_date",
        "age",
        "gender",
        "adress",
        "grade",
        "section",
    ]
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    teacher = Teacher(**data)
    teacher.save()
    return jsonify(teacher.to_dict()), 201


@auth.route("/login/teacher", methods=["POST"], strict_slashes=False)
@swag_from('documentation/teacher/teacher_login.yml', methods=['POST'])
def teacher_login():
    secret_key = current_app.config["SECRET_KEY"]
    required_fields = ["email", "password"]
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing {', '.join(missing_fields)}"}), 400

    email, password = data["email"], data["password"]
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    teacher = storage.get_by_email(Teacher, email)
    if not teacher:
        return jsonify({"error": "Teacher not found or Invalid password"}), 400

    token_payload = {
        "user_name": teacher.firstname,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=30),
    }
    token = pyjwt.encode(token_payload, secret_key)
    session["logged_in"] = True
    return jsonify({"token": token})


@app_views.route("/teachers", methods=["GET"], strict_slashes=False)
@swag_from('documentation/teacher/all_teachers.yml', methods=['GET'])
@token_required
@require_user_class("Administrator")
def get_teachers(user):
    """Retrieves all teacher objects"""
    if not session.get("logged_in", False):
        return jsonify({"error": "Unauthorized"}), 401

    teachers = [teacher.to_dict() for teacher in storage.all(Teacher).values()]
    return jsonify(teachers), 200


@app_views.route("/teachers/teacher_id>", methods=["GET"],
                 strict_slashes=False)
@swag_from('documentation/teacher/get_teacher.yml', methods=['GET'])
@token_required
@require_user_class("Teacher")
def get_teacher(teacher_id, user):
    """Retrieves an teacher"""
    if session.get("logged_in") is None or not session["logged_in"]:
        return jsonify({"error": "Unauthorized"}), 401

    teacher = storage.get(Teacher, teacher_id)
    if not teacher:
        abort(404)

    return jsonify(teacher.to_dict())


@app_views.route("/teachers/<teacher_id>", methods=["DELETE"],
                 strict_slashes=False)
@swag_from('documentation/teacher/delete_teacher.yml', methods=['DELETE'])
@token_required
@require_user_class("Administrator")
def delete_teacher(teacher_id, user):
    """
    Deletes a teacher Object
    """
    if session.get("logged_in") is None or not session["logged_in"]:
        return jsonify({"error": "Unauthorized"}), 401

    teacher = storage.get("Teacher", teacher_id)

    if not teacher:
        abort(404)

    storage.delete(teacher)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route("/teachers/<teacher_id>", methods=["PUT"],
                 strict_slashes=False)
@swag_from('documentation/teacher/update_teacher.yml', methods=['PUT'])
@token_required
@require_user_class("Teacher")
def update_teacher(teacher_id, user):
    """
    Updates a teacher profile
    """
    if session.get("logged_in") is None or not session["logged_in"]:
        return jsonify({"error": "Unauthorized"}), 401

    teacher = storage.get(Teacher, teacher_id)

    if not teacher:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ["id", "email", "created_at", "updated_at"]

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(teacher, key, value)
    storage.save()

    return make_response(jsonify(teacher.to_dict()), 200)
