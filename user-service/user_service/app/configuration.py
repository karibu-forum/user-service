import os  


class Base:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    DEBUG_TB_ENABLED = False              
    DEBUG_TB_INTERCEPT_REDIRECTS = False  
    CELERY_BROKER_URL='redis://redis:6379/0'
    REDIS_URL='redis://redis:6379'
    REQUIRE_API_AUTHENTICATION = False

class Development(Base):
    """Development configuration"""
    DATABASE_URL = os.environ.get('DATABASE_URL')  
    DEBUG_SQL = True  

class Production(Base):
    """Development configuration"""
    DATABASE_URL = os.environ.get('DATABASE_URL')  
    DEBUG_SQL = False  


app_env = os.environ.get("APP_ENV", 'development')

config_class = {
    'development': Development,
    'production': Production,
}.get(app_env, Base)

config = config_class()

# Quick hack to get store APP_ENV somewhere
config.APP_ENV = app_env
