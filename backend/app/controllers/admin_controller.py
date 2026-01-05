

from flask import request, jsonify
from app.services.admin_service import add_fund, update_request

def add_fund_controller():
    data = request.json
    add_fund(data["amount"], data["reason"])
    return jsonify({"message": "Fund added successfully"})

def update_request_controller():
    data = request.json
    result = update_request(data["requestId"], data["status"])
    return jsonify(result)
