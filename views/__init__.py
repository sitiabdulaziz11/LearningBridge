from flask import Blueprint
from flask import request, jsonify, session
from functools import wraps
from flask import current_app
from models import storage
import jwt as pyjwt

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1/")
auth = Blueprint("auth", __name__, url_prefix="/auth")


from views.students import *

from models.student_models import Student
from models.teacher_models import Teacher
from models.subject_models import Subject
from models.result_models import Result
from models.parent_models import Parent
from models.base_model import Base, BaseClass
from models.admin_models import Adminstrator

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        secret_key = current_app.config['SECRET_KEY']

        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            data = pyjwt.decode(token, secret_key, algorithms=["HS256"])
            session.setdefault('logged_in', True)
            user_types = [Student, Teacher, Parent, Adminstrator]
            user = None
            for user_type in user_types:
                user = storage.get_by_email(user_type, data['email'])
                if user:
                    break
            if not user:
                return jsonify({"error": "User not found"}), 401
            kwargs['user'] = user
        except pyjwt.ExpiredSignatureError:
            return jsonify({"error": "Token is invalid"}), 401
        return f(*args, **kwargs)
    return decorated

