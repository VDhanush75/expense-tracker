
from flask import Blueprint, request, jsonify
from app.services.admin_service import (
    add_fund,
    get_all_funds,
    get_all_requests,
    update_request_status,
    get_current_balance
)
from app.config.db import db

admin_bp = Blueprint("admin_bp", __name__)

# ---------------- FUND ----------------

@admin_bp.route("/add-fund", methods=["POST"])
def add_fund_route():
    data = request.json
    return jsonify(add_fund(data["amount"], data["reason"]))

@admin_bp.route("/fund-history", methods=["GET"])
def fund_history():
    return jsonify(get_all_funds())

# ---------------- REQUESTS ----------------

@admin_bp.route("/admin-requests", methods=["GET"])
def admin_requests():
    return jsonify(get_all_requests())

@admin_bp.route("/update-request", methods=["POST"])
def update_request():
    try:
        data = request.json
        request_id = data.get("requestId")
        action = data.get("action")

        if not request_id or not action:
            return jsonify({"error": "Invalid data"}), 400

        req = db["requests"].find_one({"requestId": request_id})
        if not req:
            return jsonify({"error": "Request not found"}), 404

        amount = int(req["amount"])

        if action == "approve":
            update_request_status(request_id, "approved")
            return jsonify({"status": "approved"})

        if action == "reject":
            update_request_status(request_id, "rejected")
            return jsonify({"status": "rejected"})

        if action == "send":
            balance = get_current_balance()

            if amount > balance:
                update_request_status(request_id, "insufficient")
                return jsonify({"status": "insufficient"})

            # record_expense(req)
            update_request_status(request_id, "sent")
            return jsonify({"status": "sent"})

        return jsonify({"error": "Invalid action"}), 400

    except Exception as e:
        print("UPDATE REQUEST ERROR:", e)
        return jsonify({"error": "server"}), 500
