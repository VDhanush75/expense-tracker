


from flask import Blueprint, jsonify
from app.db import db

expense_bp = Blueprint("expense_bp", __name__)

expenses_col = db["expenses"]

@expense_bp.route("/member-expenses/<member_name>", methods=["GET"])
def get_member_expenses(member_name):
    expenses = list(expenses_col.find(
        {"memberName": member_name},
        {"_id": 0}
    ))
    return jsonify(expenses)

