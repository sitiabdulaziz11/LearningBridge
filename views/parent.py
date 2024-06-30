from models.parent_models import Parent
import jwt as pyjwt
from models import storage
from views import app_views, auth
from flask import jsonify, request, session
from datetime import datetime, timedelta
from flask import current_app
from views.utils import token_required, require_user_class


@app_views.route('/parent', methods=['POST'], strict_slashes=False)
def create_parent():
    required_fields = ['firstname', 'middlename', 'lastname', 'email',
                       'password', 'phone_no', 'image_file', 'Address']
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing {field}"}), 400

    parent = Parent(**data)
    parent.save()
    return jsonify(parent.to_dict()), 201


@auth.route('/parent_login', methods=['POST'], strict_slashes=False)
def parent_login():
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

    parent = storage.get_by_email(Parent, email)
    if not parent:
        return jsonify({"error": "User not found or Invalid password"}), 400

    token_payload = {
        "user_name": parent.firstname,
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = pyjwt.encode(token_payload, secret_key)
    session['logged_in'] = True
    return jsonify({"token": token})


@app_views.route('/parents', methods=['GET'], strict_slashes=False)
# @token_required
# @require_user_class("Parent")
def get_parents():
    if session.get('logged_in') is None or not session['logged_in']:
        return jsonify({"error": "Unauthorized"}), 401

    parents = storage.all(Parent)
    parents = [user.to_dict() for user in parents.values()]
    return jsonify(parents), 200
