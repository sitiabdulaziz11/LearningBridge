#!/usr/bin/env python3
"""This module defines all the paths for the user moijdule"""

import jwt as pyjwt
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, session, abort, make_response
from datetime import datetime, timedelta
from flask import current_app
from api.v1.views.user_auth import require_user_class
from models.admin_models import Administrator
from flasgger.utils import swag_from
from flask_login import login_required, current_user, login_user


@app_views.route("/administrators", methods=["POST"], strict_slashes=False)
@swag_from('documentation/admin/create_admin.yml', methods=['POST'])
# @login_required
# @require_user_class('Administrator')
def create_administrator():
    required_fields = [
        "firstname",
        "middlename",
        "lastname",
        "email",
        "password",
        "phone_no",
        "gender",
        "age",
        "hire_date",
        "address",
    ]
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    administrator = Administrator(**data)
    administrator.save()
    return jsonify(administrator.to_dict()), 201

@app_views.route("/administrators", methods=["GET"], strict_slashes=False)
@swag_from('documentation/admin/all_admins.yml', methods=['GET'])
@login_required
# @require_user_class('Administrator')
def get_administrators():
    if (current_user.id.startswith('administrator_')):
        administrators = storage.all(Administrator)
        administrators = [user.to_dict() for user in administrators.values()]
        return jsonify(administrators), 200
    else:
        return jsonify({"error": "User is not administrator"}), 400

@app_views.route("/login/administrator", methods=["POST"], strict_slashes=False)
@swag_from('documentation/admin/admin_login.yml', methods=['POST'])
def administrator_login():
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

    administrator = storage.get_by_email(Administrator, email)
    if not administrator:
        return jsonify({"error": "User not found or Invalid password"}), 400
    login_user(administrator)
    return jsonify({"message": "login successful"}), 200


@app_views.route("/admin/admin_id>", methods=["GET"],
                 strict_slashes=False)
# @swag_from('documentation/teacher/get_teacher.yml', methods=['GET'])
@login_required
@require_user_class("Teacher")
def get_administrator(admin_id):
    """Retrieves an Admin"""
    admin = storage.get(Administrator, admin_id)
    if not admin:
        abort(404)
    return jsonify(admin.to_dict())


@app_views.route("/admin/admin_id>", methods=["DELETE"],
                 strict_slashes=False)
# @swag_from('documentation/teacher/delete_teacher.yml', methods=['DELETE'])
@login_required
@require_user_class("Teacher")
def delete_administrator(admin_id):
    """
    Deletes a teacher Object
    """
    admin = storage.get("Administrator", admin_id)

    if not admin:
        abort(404)

    storage.delete(admin)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route("/admin/admin_id>", methods=["PUT"],
                 strict_slashes=False)
# @swag_from('documentation/teacher/update_teacher.yml', methods=['PUT'])
@login_required
@require_user_class("Teacher")
def update_administrator(admin_id):
    """
    Updates a teacher profile
    """
    admin = storage.get(Administrator, admin_id)

    if not admin:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ["id", "email", "created_at", "updated_at"]

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(admin, key, value)
    storage.save()
    return make_response(jsonify(admin.to_dict()), 200)
