from . import bp, forms
from L1_service import auth_service

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("already logged in", category="warning")
        return redirect(url_for("overview.index"))

    email = request.form.get('email')
    password = request.form.get('password')
    user = auth_service.login(email, password)
    login_user(user)
    flash("login successful", category="success")
    return redirect(url_for("overview.index"))
