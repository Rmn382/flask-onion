from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth")

from app.L2_infrastructure.web.auth import routes