## Insert Data Models
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = "adminusers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, password={self.password})"

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    d_created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    venue = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    facebooklink = db.Column(db.String(250), nullable=False)

    def __init__(self, id, d_created, venue, city, date, facebooklink):
        self.id = id
        self.d_created = d_created
        self.venue = venue
        self.city = city
        self.date = date
        self.facebooklink = facebooklink

    def __repr__(self):
        return f"Event(id={self.id}, d_created={self.d_created}, venue={self.venue}, city={self.city}, date={self.date}, facebook_link={self.facebooklink})"