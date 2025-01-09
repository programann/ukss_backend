from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from ..models import db, Admin, Event
from .. import bcrypt
from ..utils import upload_to_cloudinary

bp = Blueprint("admin", __name__)

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    admin = Admin.query.first()
    if admin and bcrypt.check_password_hash(admin.password, data["password"]):
        token = create_access_token(identity=admin.id)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401

@bp.route("/events", methods=["POST"])
@jwt_required()
def add_event():
    data = request.form
    file = request.files.get("image")
    image_url = upload_to_cloudinary(file)
    event = Event(title=data["title"], image=image_url, description=data["description"])
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Event added successfully!"}), 201

@bp.route("/events/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully!"})

@bp.route("/password", methods=["PUT"])
@jwt_required()
def update_password():
    data = request.json
    admin = Admin.query.first()
    admin.password = bcrypt.generate_password_hash(data["new_password"]).decode('utf-8')
    db.session.commit()
    return jsonify({"message": "Password updated successfully!"})
