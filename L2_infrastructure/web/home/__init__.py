from flask import Blueprint

bp = Blueprint("home", __name__, url_prefix="/home")

from L2_infrastructure.web.home import routes