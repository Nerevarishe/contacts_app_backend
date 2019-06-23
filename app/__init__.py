from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config

db = MongoEngine()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.contacts import bp as contacts_bp
    app.register_blueprint(contacts_bp)

    return app
