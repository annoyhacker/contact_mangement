from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Contact, User
from sqlalchemy import asc, desc

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

    # Get query parameters
    page = request.args.get('page', 1, type=int)
    per_page = 10  # You can make this customizable
    sort_by = request.args.get('sort_by', 'alphabetically_a_to_z')

    # Apply sorting logic
    if sort_by == 'alphabetically_z_to_a':
        sort_order = desc(Contact.name)
    else:  # Default to A to Z
        sort_order = asc(Contact.name)

    # Apply pagination and sorting
    contacts_paginated = Contact.query.filter_by(user_id=user_id)\
        .order_by(sort_order)\
        .paginate(page=page, per_page=per_page, error_out=False)

    # Return formatted response
    return jsonify({
        "message": "Contact list",
        "page": page,
        "per_page": per_page,
        "total": contacts_paginated.total,
        "pages": contacts_paginated.pages,
        "data": [
            {
                "id": contact.id,
                "name": contact.name,
                "email": contact.email,
                "phone": contact.phone,
                "address": contact.address,
                "country": contact.country
            } for contact in contacts_paginated.items
        ]
    }), 200
