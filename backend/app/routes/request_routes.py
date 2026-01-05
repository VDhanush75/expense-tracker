
from flask import Blueprint, request, jsonify
from app.services.request_service import submit_request
from app.config.db import db

request_bp = Blueprint("request_bp", __name__)


@request_bp.route("/add-request", methods=["POST"])
def add_request_route():
    data = request.json
    print("RECEIVED:", data)

    result = submit_request(data)
    return jsonify(result), 200


@request_bp.route("/member-requests", methods=["GET"])
def member_requests():
    member = request.args.get("memberName")
    data = list(db["requests"].find({"memberName": member}, {"_id": 0}))
    return jsonify(data), 200
