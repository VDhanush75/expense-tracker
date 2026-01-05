from flask import request, jsonify
from app.services.expense_service import fetch_member_expenses

def member_expenses():
    member_id = request.args.get("memberId")

    result = fetch_member_expenses(member_id)
    return jsonify(result)
