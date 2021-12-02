from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class Registration(FlaskForm):
    username = StringField("Username", validators= [DataRequired(), Length(min=5, max=20)])
    email = StringField("Emailid", validators= [DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    confirm_password= PasswordField("Confirm Password",validators=[DataRequired(), EqualTo("password")])
    submit= SubmitField("Sign Up")


class Login(FlaskForm):
    email = StringField("Emailid", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    login = SubmitField("Login")