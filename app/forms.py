from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired

class AddAssetForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    type = SelectField('Type', choices=[('pc', 'pc'), ('mobile', 'mobile'), ('router', 'router'), ('other', 'other')] ,validators = [DataRequired()])
    serial_number = StringField('Serialnumber')
    owner = StringField('Owner') 
    purchased = DateField('Purchased')
    submit = SubmitField('Add asset')

class LoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')