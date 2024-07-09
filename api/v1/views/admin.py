#!/usr/bin/env python3
"""This module defines all the paths for the user moijdule"""

import jwt as pyjwt
from models import storage
from api.v1.views import app_views, auth
from flask import jsonify, request, session
from datetime import datetime, timedelta
from flask import current_app
from api.v1.views.utils import token_required, require_user_class, blacklist
from models.admin_models import Administrator
from flasgger.utils import swag_from


@app_views.route("/administrators", methods=["POST"], strict_slashes=False)
@swag_from('documentation/admin/create_admin.yml', methods=['POST'])
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


@auth.route("/login/administrator", methods=["POST"], strict_slashes=False)
@swag_from('documentation/admin/admin_login.yml', methods=['POST'])
def administrator_login():
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

    administrator = storage.get_by_email(Administrator, email)
    if not administrator:
        return jsonify({"error": "User not found or Invalid password"}), 400

    token_payload = {
        "user_name": administrator.firstname,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=30),
    }
    token = pyjwt.encode(token_payload, secret_key)
    session["logged_in"] = True
    return jsonify({"token": token})


@auth.route("/logout/admin", methods=["POST"], strict_slashes=False)
@token_required
@require_user_class("Administrator")
def admin_logout(user):
    """
    Logout a user
    """
    # expire the token immediately
    token = request.headers.get("Authorization")
    if token is None:
        return jsonify({"error": "Token is missing"}), 401
    blacklist.add(token)
    session["logged_in"] = False
    return jsonify({"message": f"{user.firstname} Logged out"})


@app_views.route("/administrators", methods=["GET"], strict_slashes=False)
@swag_from('documentation/admin/all_admins.yml', methods=['GET'])
@token_required
@require_user_class("Administrator")
def get_administrators(user):
    if session.get("logged_in") is None or not session["logged_in"]:
        return jsonify({"error": "Unauthorized"}), 401

    administrators = storage.all(Administrator)
    administrators = [user.to_dict() for user in administrators.values()]
    return jsonify(administrators), 200
