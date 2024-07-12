#!/usr/bin/env python3
"""App to register blueprint and start Flask"""

# from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from flasgger import Swagger
from flask_cors import CORS
from models.parent_models import Parent
from models.student_models import Student
from models.teacher_models import Teacher

# install flask login
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


app = Flask(__name__)
CORS(app, origin="0.0.0.0")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://lb:Team_Project@localhost/LB"
app.config["SECRET_KEY"] = "my_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # Check the user type and load the appropriate user model

    user_type = user_id.split('_')[0]
    if user_type == 'teacher':
        user = storage.get(Teacher, user_id)
    elif user_type == 'student':
        user = storage.get(Student, user_id)
    elif user_type == 'parent':
        user = storage.get(Parent, user_id)
    else:
        return None
    
    if user:
        return user
    else:
        return None


    # Register blueprints
app.register_blueprint(app_views)
    # app.register_blueprint(auth)

    # Swagger config
app.config['SWAGGER'] = {
    'title': 'LEARNINGBRIDGE RESTful API',
    'version': 1.0
}

Swagger(app)


# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Not found"}, 404

@app.errorhandler(500)
def internal_error(e):
    return {"error": "Internal server error"}, 500

# Teardown
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


# return app
if __name__ == "__main__":
    app.run(
        host="localhost", port=5000, debug=True
    )
