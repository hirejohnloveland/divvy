from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        from app.blueprints.divvy import bp as divvy
        app.register_blueprint(divvy)

        from app.blueprints.api import bp as api
        app.register_blueprint(api)

    return app
