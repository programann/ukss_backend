from . import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=False)  # Cloudinary URL
    description = db.Column(db.Text, nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), nullable=False)  # Hashed password
