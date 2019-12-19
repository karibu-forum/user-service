import click

from user_service.api.rest.server import app as flask_app


@click.command(name='runserver')
@click.option('-h', '--host', default='0.0.0.0')
@click.option('-p', '--port', default=3000)
def run_server(host, port):
    print('Running Flask development server on port {}'.format(port))
    flask_app.run(
        host=host,
        port=port,
        debug=True,
    )
