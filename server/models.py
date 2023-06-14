from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer(50))
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipcode = db.Column(db.Integer(50))
    country = db.Column(db.String(50))
    admin = db.Column(db.Boolean)
    job_title = db.Column(db.String(50))
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Schedule(db.Model, SerializerMixin):
    __tablename__ = 'schedules'
    
    id = db.Column(db.Integer, primary_key=True)
    monday = db.Column(db.String(50))
    tuesday = db.Column(db.String(50))
    wednesday = db.Column(db.String(50))
    thursday = db.Column(db.String(50))
    friday = db.Column(db.String(50))
    saturday = db.Column(db.String(50))
    sunday = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'    