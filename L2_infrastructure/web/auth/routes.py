from . import bp, forms
from L1_service import auth_service

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user

from __init__ import db
from L2_infrastructure.database.models import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            flash("already logged in", category="warning")
            return redirect(request.referrer or url_for("overview.index"))
        form = forms.LoginForm()
        return render_template('auth/login.html', form=form)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(id=current_user.id).first()
        if user is None:
            user = User(id=current_user.id, email=email, password=password)
            db.session.add(user)
            db.session.commit()
        login_user(user)
        flash("login successful", category="success")
        return redirect(url_for("overview.index"))


@bp.route('/logout')
def logout():
    logout_user()
    flash("logged out", category="success")
    return redirect(url_for("auth.login"))
