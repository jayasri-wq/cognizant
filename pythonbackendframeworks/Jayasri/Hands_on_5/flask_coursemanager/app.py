from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Database
    db.init_app(app)

    # Initialize Migration
    migrate.init_app(app, db)

    # Register Blueprint
    from courses.routes import courses_bp
    app.register_blueprint(courses_bp)

    return app