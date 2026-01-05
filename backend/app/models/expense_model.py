from app.config.db import db

expenses = db["expenses"]

def get_expenses_by_member(member_id):
    return list(expenses.find({"memberId": member_id}))
