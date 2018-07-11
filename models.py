from flask import Flask
from werkzeug import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    phonenumber = db.Column(db.String(15))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256))

    def __init__(self, firstname, lastname, phonenumber, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.phonenumber = phonenumber.title()
        self.email = email.lower()
        self.username = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    comment = db.Column(db.String())
    username = db.Column(db.String(100))
    status = db.Column(db.String(20))

    def __init__(self, title, comment, username, status):
        self.title = title.title()
        self.comment = comment.title()
        self.username = username.title()
        self.status = status.title()
