import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime


# instantiate the db
db = SQLAlchemy()


# # set config
# app.config.from_object('project.config.DevelopmentConfig')


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    return app