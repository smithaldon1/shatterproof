## Insert Data Models
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = "adminusers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(email={self.email}, username={self.username}, password={self.password})"

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    d_created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    venue = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    facebooklink = db.Column(db.String(250), nullable=False)

    def __init__(self, d_created, venue, city, date, facebooklink):
        self.d_created = d_created
        self.venue = venue
        self.city = city
        self.date = date
        self.facebooklink = facebooklink

    def __repr__(self):
        return f"Event(id={self.id}, d_created={self.d_created}, venue={self.venue}, city={self.city}, date={self.date}, facebook_link={self.facebooklink})"
    
class Emails(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), nullable=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return f"Emails(id={self.id}, email={self.email})"