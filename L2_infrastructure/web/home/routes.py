from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required

from L1_service import home_service
from . import bp


@bp.before_request
@login_required
def before_request():
    # check if user is logged in
    pass


@bp.route('/', methods=['GET'])
def index():
    return render_template('home/index.html')
