from models.student_models import Student
from models import storage
from api.v1.views import app_views
from flask import jsonify, request, session, make_response, abort
from datetime import datetime, timedelta
from flask import current_app
from flasgger.utils import swag_from
from flask_login import login_user, logout_user, current_user



@app_views.route("/login", methods=["POST"])
def login():
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

    student = storage.get_by_email(Student, email)
    if not student:
        return jsonify({"error": "User not found or Invalid password"}), 400
    # student_id = f'student_{student.id}'
    login_user(student)
    return jsonify({"message": "login successful"}), 200
    # if request.method == "POST":
    #     user = Users.query.filter_by(
    #         username=request.form.get("username")).first()
    #     if user.password == request.form.get("password"):
    #         login_user(user)
    #         return redirect(url_for("home"))


@app_views.route("/logout")
def logout():
    logout_user()
    return jsonify({"message": "logout successful"}), 200


@app_views.route('user_status', methods=['GET'])
def get_user_status():
    if current_user.is_authenticated:
        return jsonify({
            'is_authenticated': True,
            'user': current_user.to_dict()
        })
    else:
        return jsonify({
            'is_authenticated': False
        })