import click

from user_service.commands.db import db
from user_service.commands import seed
from user_service.commands.server import run_server
from user_service import app


@click.group()
def cli():
    pass


cli.add_command(db)
if app.config.APP_ENV != 'production':
    cli.add_command(run_server)
