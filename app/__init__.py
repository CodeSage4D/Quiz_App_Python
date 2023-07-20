from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_app.db'
    db.init_app(app)

    # Import the models here to avoid circular imports
    from .models import Question

    # Import the routes module to register the routes with the Flask app
    from .routes import main

    # Register the blueprints or add other routes
    app.register_blueprint(main)

    return app
