from flask_login import UserMixin
from __init__ import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


@login.user_loader
def load_user(email):
    return User.query.filter_by(id=email).first()
