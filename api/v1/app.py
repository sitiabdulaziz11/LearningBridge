#!/usr/bin/env python3
"""App to register blueprint and start Flask"""

from dotenv import load_dotenv
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views, auth
from flasgger import Swagger
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    load_dotenv()
    
    # Load environment variables from .env
    # load_dotenv(os.path.join(os.getcwd(), 'models', '.env')) when .env inside models directory.

    # Configuration settings
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SESSION_TYPE"] = "sqlalchemy"
    app.config["SESSION_SQLALCHEMY"] = None
    
    secret = os.getenv("SECRET_KEY")
    print(secret)
    # print(f"SECRET_KEY: {secret}")  # Debugging: Print SECRET_KEY to ensure it's loaded
    
    # Enable CORS
    CORS(app, origin="0.0.0.0")

    # Register blueprints
    app.register_blueprint(app_views)
    app.register_blueprint(auth)

    # Swagger config
    app.config['SWAGGER'] = {
        'title': 'LEARNINGBRIDGE RESTful API',
        'version': 1.0
    }

    Swagger(app)
    
    @app.route('/api/v1/results', methods=['POST'])
    def handle_results():
        print('Received POST request for results')
        # Handle request logic here
        return jsonify({'message': 'Results received'})


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

    # print(app.url_map)  # Print the registered routes after initialization
    
    return app
