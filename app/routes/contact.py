from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Contact, User

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/', methods=['POST'])
@jwt_required()
def add_contact():
    user_id = get_jwt_identity()
    data = request.get_json()
    name, phone = data.get('name'), data.get('phone')

    if not name or not phone:
        return jsonify({"message": "Name and phone are required", "data": {}}), 400

    try:
        contact = Contact(
            name=name,
            phone=phone,
            email=data.get('email'),
            address=data.get('address'),
            country=data.get('country'),
            user_id=user_id
        )
        db.session.add(contact)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Database error", "error": str(e)}), 500

    return jsonify({
        "message": "Contact added",
        "data": {
            "id": contact.id,
            "name": contact.name,
            "phone": contact.phone,
            "email": contact.email,
            "address": contact.address
        }
    }), 201  # Changed to 201 Created status code

@contact_bp.route('/', methods=['GET'])
@jwt_required()
def get_contacts():
    user_id = get_jwt_identity()
    contacts = Contact.query.filter_by(user_id=user_id).all()
    
    return jsonify({
        "message": "Contact list",
        "data": [
            {
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "phone": contact.phone,
                "address": contact.address,
                "country": contact.country
            } for contact in contacts
        ]
    }), 200