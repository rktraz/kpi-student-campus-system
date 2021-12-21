from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import enum


class Administrator(db.Model, UserMixin):
    __tablename__ = 'administrators'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(64))
    password = db.Column(db.String(512))
    dormitories = db.relationship("Dormitory")

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit or self


class Dormitory(db.Model):
    __tablename__ = 'dormitories'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    number = db.Column(db.Integer)
    address = db.Column(db.String(256), unique=True)
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrators.id'),  nullable=True)
    resident = db.relationship("Resident")


class Faculty(db.Model):
    __tablename__ = 'faculties'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    resident = db.relationship("Resident")


class Resident(db.Model):
    __tablename__ = 'residents'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    room = db.Column(db.Integer)
    course = db.Column(db.Integer)
    group = db.Column(db.String(8))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'))
    dormitory_id = db.Column(db.Integer, db.ForeignKey('dormitories.id'))


class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    month_payed = db.Column(db.String(16))
    resident_id = db.Column(db.Integer, db.ForeignKey('residents.id'))

