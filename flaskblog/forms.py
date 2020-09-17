from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username*',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email*',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password*', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password*', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email*',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password*', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username*',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email*',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, field):
        if field.data != current_user.username:
            user = User.query.filter_by(username=field.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, field):
        if field.data != current_user.email:
            user = User.query.filter_by(email=field.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post_content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    submit = SubmitField('Request Password Reset')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password*', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password*', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
