import os


class Config(object):
    # CONFIGURATIONS

    # DB variables
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.database"

    # APP variables
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    TEMPLATE_DIR = "app/templates"
    DEBUG = True if os.environ.get("FLASK_ENV") == "development" else False
