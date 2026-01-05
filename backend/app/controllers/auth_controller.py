from flask import request, jsonify
from app.services.auth_service import authenticate_user

def login():
    data = request.json
    user_id = data.get("userId")
    password = data.get("password")

    result = authenticate_user(user_id, password)
    return jsonify(result)
