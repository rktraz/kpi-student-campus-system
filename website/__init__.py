from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
# DB_NAME = "database.db"

import json

# Opening JSON file
with open('website/registration_codes.json') as json_file:
    registration_codes = json.load(json_file)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mykola barabolya'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    username = "postgres"
    password = "admin"
    dbname = "postgres"

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Administrator, Dormitory, Resident, Faculty, Payment

    # create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Administrator.query.get(int(id))

    return app
