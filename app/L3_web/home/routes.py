from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from . import bp
from app.L1_application.services.aggregate import AggregateRootService
from app.L2_infrastructure.database.repositories.aggregate import AggregateRootRepository

aggregate_service = AggregateRootService(AggregateRootRepository())
aggregate_repo = AggregateRootRepository()


@bp.before_request
@login_required
def before_request():
    # check if user is logged in
    pass


@bp.route('/', methods=['GET'])
def index():
    aggregates = aggregate_repo.get_all_by_user(current_user.id)
    return render_template('home/index.html', user=current_user, aggregates=aggregates)
