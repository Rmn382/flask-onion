import os
from collections import OrderedDict
from pathlib import Path


class Config(object):

    # CONFIGURATIONS

    # DB variables
    SQLALCHEMY_DATABASE_URI = "sqlite:///dscrubber.database"


    # APP variables
    SECRET_KEY = "super_secret_key"

