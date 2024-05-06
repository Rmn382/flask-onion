from flask import Blueprint

bp = Blueprint("home", __name__, url_prefix="/home")

from L3_web.home import routes