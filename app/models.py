from enum import unique
from app import db
from datetime import datetime

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True) 
    type = db.Column(db.String(64), index=True) 
    purchased = db.Column(db.DateTime, default=datetime.utcnow) # data zakupu sprzętu
    owner = db.Column(db.String(64), index=True) # atkualny właściciel
    serial_number = db.Column(db.String(64), index=True) # numer seryjny
    added_by = db.Column(db.String(64), db.ForeignKey('user.id')) # dodane przez, klucz obcy dla user.id


class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(120), index=True, unique=True) 
    password_hash = db.Column(db.String(128)) # hasło które będziemy hashować
    assets = db.relationship('Asset', backref='author', lazy='dynamic') # asset który dodał user