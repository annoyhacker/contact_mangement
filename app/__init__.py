from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from config import config

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)

    from app.routes.auth import auth_bp
    from app.routes.contact import contact_bp

    app.register_blueprint(auth_bp, url_prefix='/user')
    app.register_blueprint(contact_bp, url_prefix='/contact')

    return app