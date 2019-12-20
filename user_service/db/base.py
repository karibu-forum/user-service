from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from user_service.app.configuration import config


Base = declarative_base()

engine = None
Session = None


def initialize_database():
    global engine, Session
    
    database_url = config.DATABASE_URL
    connection_args = {
        'connect_args': {
            'connect_timeout': 10
        }
    }

    if config.DEBUG_SQL:
        connection_args.update({'echo': True})

    engine = create_engine(database_url, **connection_args)
    session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Session = scoped_session(session_factory)
    from user_service.db import models   # noqa


def get_engine():
    return engine
