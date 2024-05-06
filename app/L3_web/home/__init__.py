from flask import Blueprint

bp = Blueprint("home", __name__, url_prefix="/home")

from app.L3_web.home import routes