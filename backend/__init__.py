from backend.extensions.doppler import DopplerConfig
from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Load settings from Doppler
    DopplerConfig(app=app)

    # Init database
    from .database import db

    db.init_app(app=app)

    from .database import models  # noqa: F401

    # Commands
    from . import commands

    app.cli.add_command(commands.create_db)

    return app
