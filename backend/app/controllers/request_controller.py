from flask import request, jsonify
from app.config.db import db
from app.services.request_service import submit_request
from app.services.admin_service import get_current_balance, update_request_status, record_expense


# =========================
# MEMBER → CREATE REQUEST
# =========================
def add_request():
    try:
        data = request.json
        amount = int(data["amount"])

        balance = get_current_balance()

        # Block immediately if insufficient fund
        if amount > balance:
            return jsonify({
                "success": False,
                "status": "insufficient",
                "message": "Insufficient fund"
            }), 200

        result = submit_request(data)

        return jsonify({
            "success": True,
            "status": "pending",
            "request": result
        }), 200

    except Exception as e:
        print("ADD REQUEST ERROR:", e)
        return jsonify({"success": False, "error": "server"}), 500


# =========================
# ADMIN → UPDATE REQUEST
# =========================
def update_request():
    try:
        data = request.json
        req_id = data.get("requestId")
        action = data.get("action")

        if not req_id or not action:
            return jsonify({"error": "Invalid data"}), 400

        req = db["requests"].find_one({"requestId": req_id})
        if not req:
            return jsonify({"error": "Request not found"}), 404

        amount = int(req["amount"])

        # APPROVE → only mark approved
        if action == "approve":
            update_request_status(req_id, "approved")
            return jsonify({"status": "approved"}), 200

        # REJECT → move to history
        if action == "reject":
            update_request_status(req_id, "rejected")
            return jsonify({"status": "rejected"}), 200

        # SEND → check fund & record expense
        if action == "send":
            balance = get_current_balance()

            if amount > balance:
                update_request_status(req_id, "insufficient")
                return jsonify({"status": "insufficient"}), 200

            record_expense(req)
            update_request_status(req_id, "sent")
            return jsonify({"status": "sent"}), 200

        return jsonify({"error": "Invalid action"}), 400

    except Exception as e:
        print("UPDATE REQUEST ERROR:", e)
        return jsonify({"error": "server"}), 500

