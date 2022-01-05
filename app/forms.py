from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired

class AddAssetForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    type = SelectField('Type', choices=[('pc', 'pc'), ('mobile', 'mobile'), ('router', 'router'), ('other', 'other')] ,validators = [DataRequired()])
    serial_number = StringField('Serialnumber')
    owner = StringField('Owner') 
    purchased = DateField('Purchased')
    submit = SubmitField('Add asset')