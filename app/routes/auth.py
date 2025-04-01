from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models import User
from flask_jwt_extended import (
    create_access_token,
    jwt_required, 
    get_jwt_identity
)

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name, email, password = data.get('name'), data.get('email'), data.get('password')

    if not name or not email or not password:
        return jsonify({"message": "All fields are required", "data": {}}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered", "data": {}}), 400

    try:
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Database error", "error": str(e)}), 500

    # Convert user.id to string for JWT identity
    access_token = create_access_token(identity=str(user.id))
    return jsonify({
        "message": "User signup complete",
        "data": {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        }
    }), 201  # Changed status code to 201 Created

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials", "data": {}}), 401

    # Convert user.id to string for JWT identity
    access_token = create_access_token(identity=str(user.id))
    return jsonify({
        "message": "Login successful",
        "data": {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        }
    }), 200

@auth_bp.route('/', methods=['GET'])
@jwt_required()
def get_user_profile():
    try:
        # Convert string identity back to integer
        user_id = int(get_jwt_identity())  # Convert to int
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({"message": "User not found", "data": {}}), 404

        return jsonify({
            "message": "User profile",
            "data": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        }), 200
    except ValueError:
        return jsonify({"message": "Invalid user identity format", "data": {}}), 400