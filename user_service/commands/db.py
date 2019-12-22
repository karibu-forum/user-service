import click
import subprocess
from user_service import app

# import alembic.config


DB_NAME = 'karibu_user'

@click.group()
def db():
    pass


def _drop_db():
    print('--> Dropping database')
    subprocess.run('dropdb {}'.format(DB_NAME), shell=True, check=True)

def _create_db():
    print('--> Creating database')
    subprocess.run('createdb {}'.format(DB_NAME), shell=True, check=True)

@click.command(name='drop')
def drop_db():
    _drop_db()


@click.command(name='create')
@click.option('--drop', is_flag=True)
@click.option('--tables/--no-tables', 'create_tables', default=True)
def create_db(drop, create_tables):
    if drop:
        _drop_db()
    _create_db()
    if create_tables:
        from user_service.db.base import Base, get_engine
        engine = get_engine()
        conn = engine.connect()
        print('--> Creating tables')
        Base.metadata.create_all(conn)


@click.command(name='reset')
@app.app_context()
def reset_db():
    from user_service.db.base import Base, get_engine
    engine = get_engine()
    conn = engine.connect()

    print('--> Dropping tables')
    Base.metadata.drop_all(conn)
    print('--> Creating tables')
    Base.metadata.create_all(conn)


db.add_command(drop_db)
db.add_command(create_db)
db.add_command(reset_db)
