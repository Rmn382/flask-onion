from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.L2_infrastructure.database.models.user import User


class LoginForm(FlaskForm):
    email_or_username = StringField('E-Mail or Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_email_or_username(self, email_or_username):
        user = User.query.filter_by(email=email_or_username.data).first()
        if user is None:
            user = User.query.filter_by(name=email_or_username.data).first()
        if user is None:
            raise ValidationError('User not found.')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')

    # Custom validators: validate_<field_name> will be called when form.validate_on_submit() is called
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('email address already in use.')

    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('name already in use.')
