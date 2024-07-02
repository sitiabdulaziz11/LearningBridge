from functools import wraps
from flask import request, jsonify, session, current_app
import jwt as pyjwt
from models import storage
from models.student_models import Student
from models.teacher_models import Teacher
from models.parent_models import Parent
from models.admin_models import Administrator


def get_current_user():
    token = request.headers.get("Authorization")
    if token is None:
        return None
    secret_key = current_app.config["SECRET_KEY"]
    data = pyjwt.decode(token, secret_key, algorithms=["HS256"])
    email = data["email"]

    user_classes = [Student, Teacher, Parent, Administrator]
    for user_class in user_classes:
        user = storage.get_by_email(user_class, email)
        if user:
            return user
    return None


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        secret_key = current_app.config["SECRET_KEY"]
        print(secret_key)
        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            data = pyjwt.decode(token, secret_key, algorithms=["HS256"])
            print(data)
            session.setdefault("logged_in", True)
            student = storage.get_by_email(Student, data["email"])
            teacher = storage.get_by_email(Teacher, data["email"])
            parent = storage.get_by_email(Parent, data["email"])
            admin = storage.get_by_email(Administrator, data["email"])
            if not student and not teacher and not parent and not admin:
                return jsonify({"error": "User not found"}), 401
            else:
                session["logged_in"] = True
                kwargs["user"] = student or teacher or parent or admin
        except:
            return jsonify({"error": "Token is invalid"}), 401
        return f(*args, **kwargs)  # Add this line

    return decorated


def require_user_class(required_class):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = get_current_user()
            if user.__class__.__name__ != required_class:
                return jsonify({"error": "Access denied!!"}), 401
            return f(*args, **kwargs)

        return decorated_function

    return decorator
