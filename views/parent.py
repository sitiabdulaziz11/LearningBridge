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

    parent = Parent(**data) # This line creates a new instance of the Parent class,
    # using the data dictionary to provide keyword arguments to the constructor.
    parent.save()
    return jsonify(parent.to_dict()), 201


@auth.route('/parent_login', methods=['POST'], strict_slashes=False)
def parent_login():
    """
    Login a parent.

    This function handles the POST request for the parent login endpoint.
    It expects a JSON payload containing the email and password of the parent.

    Returns:
        A JSON response containing a token if the login is successful.
        Otherwise, a JSON response with an error message and a status code of 400.
    """
    # Get the secret key from the application configuration
    secret_key = current_app.config['SECRET_KEY']

    # Define the required fields in the JSON payload
    required_fields = ['email', 'password']

    # Get the JSON payload from the request
    data = request.get_json()

    # Check if the payload is not a JSON
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    # Check if all the required fields are present in the payload
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing {', '.join(missing_fields)}"}), 400

    # Get the email and password from the payload
    email, password = data['email'], data['password']

    # Check if the email and password are missing
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    # Get the parent from the storage using the email
    parent = storage.get_by_email(Parent, email)

    # Check if the parent is not found or the password is invalid
    if not parent:
        return jsonify({"error": "User not found or Invalid password"}), 400

    # Create the token payload
    token_payload = {
        "user_name": parent.firstname,
        'email': email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }

    # Encode the token payload using the secret key
    token = pyjwt.encode(token_payload, secret_key)

    # Set the logged_in flag in the session to True
    session['logged_in'] = True

    # Return a JSON response containing the token
    return jsonify({"token": token})


@app_views.route('/parents', methods=['GET'], strict_slashes=False)
@token_required
@require_user_class("Parent")
def get_parents():
    """To get all parents
    """
    
    if session.get('logged_in') is None or not session['logged_in']:
        return jsonify({"error": "Unauthorized"}), 401

    parents = storage.all(Parent)
    parents = [user.to_dict() for user in parents.values()]
    return jsonify(parents), 200


@app_views.route('/parent/<int:parent_id>', methods=['GET'], strict_slashes=False)
@token_required
@require_user_class("Parent")
def get_individual_parent(parent_id):
    """To get an individual parent
    """
    
    if session.get('logged_in') is None or not session['logged_in']:
        return jsonify({"error": "Unauthorized"}), 401

    parent = storage.get(Parent, parent_id)
    if not parent:
        return jsonify({"error": "Parent not found"}), 404
    return jsonify(parent.to_dict()), 200


@app_views.route('/parent/<int:parent_id>', methods=['PUT'], strict_slashes=False)
@token_required
@require_user_class("Parent")
def update_parent(parent_id):
    """To update an individual parent
    """
    
    if session.get('logged_in') is None or not session['logged_in']:
        return jsonify({"error": "Unauthorized"}), 401

    parent = storage.get(Parent, parent_id)
    if not parent:
        return jsonify({"error": "Parent not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(parent, key, value)
    parent.save()
    return jsonify(parent.to_dict()), 200


@app_views.route('/parent/<int:parent_id>', methods=['DELETE'], strict_slashes=False)
@token_required
@require_user_class("Parent")
def delete_parent(parent_id):
    """delete an individual parent
    """
    
    if session.get('logged_in') is None or not session['logged_in']:
        return jsonify({"error": "Unauthorized"}), 401

    parent = storage.get(Parent, parent_id)
    if not parent:
        return jsonify({"error": "Parent not found"}), 404

    storage.delete(parent)
    storage.save()
    return jsonify({}), 200


# updating deleting getting individual parent , signout *898#