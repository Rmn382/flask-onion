from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user

from __init__ import db
from L2_infrastructure.database.models.user import User
from . import bp, forms




@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("already logged in", category="warning")
        return redirect(request.referrer or url_for("home.index"))

    form = forms.RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered.')
        return redirect(url_for('home.index'))
    return render_template('auth/register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("already logged in", category="warning")
        return redirect(request.referrer or url_for("home.index"))

    if request.method == 'GET':
        form = forms.LoginForm()
        return render_template('auth/login.html', form=form)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("user not found", category="danger")
            return redirect(url_for("auth.login"))
        elif user.check_password(password):
            login_user(user)
            flash("login successful", category="success")
            return redirect(url_for("home.index"))
        else:
            flash("wrong password", category="danger")
            return redirect(url_for("auth.login"))


@bp.route('/logout')
def logout():
    if not current_user.is_authenticated:
        flash("already logged out", category="warning")
        return redirect(url_for("auth.login"))
    logout_user()
    flash("logged out", category="success")
    return redirect(url_for("auth.login"))
