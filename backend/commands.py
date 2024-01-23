import click
from flask import current_app
from flask.cli import with_appcontext
from .database import db


@click.command()
@with_appcontext
def create_db():
    db.create_all()
    current_app.logger.info("DB tables created")
