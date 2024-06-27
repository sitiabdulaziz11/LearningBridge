#!/usr/bin/env python3
"""App to register blueprint and start Flask"""
from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views, auth
from flask_swagger_ui import get_swaggerui_blueprint
from flask_swagger import swagger


def create_app():
    app = Flask(__name__)

    load_dotenv()

    # Configuration settings
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config["SESSION_TYPE"] = "sqlalchemy"
    app.config['SESSION_SQLALCHEMY'] = None
    secret = os.getenv('SECRET_KEY')
    print(secret)
    # Enable CORS
    CORS(app, origin="0.0.0.0")

    # Register blueprints
    app.register_blueprint(app_views)
    app.register_blueprint(auth)

    # Swagger UI blueprint
    SWAGGER_URL = '/api/docs'
    API_URL = '/api/spec'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "LEARNERSBRIDGE API"},
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

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

    # API spec
    @app.route(API_URL)
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "LEARNERSBRIDGE API"
        return jsonify(swag)

    return app
