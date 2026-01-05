

from datetime import datetime
from collections import defaultdict
from app.config.db import db

requests_col = db["requests"]
funds_col = db["funds"]
expenses_col = db["expenses"]

# ------------------ FUND SERVICES ------------------

def add_fund(amount, reason):
    fund = {
        "amount": int(amount),
        "reason": reason,
        "createdAt": datetime.utcnow().isoformat()
    }
    funds_col.insert_one(fund)
    return {"success": True}

def get_all_funds():
    return list(funds_col.find({}, {"_id": 0}))

def get_total_fund():
    return sum(int(f["amount"]) for f in funds_col.find({}))

# ------------------ EXPENSE SERVICES ------------------

def get_total_expense():
    return sum(int(e["amount"]) for e in expenses_col.find({}))

def get_current_balance():
    return get_total_fund() - get_total_expense()

# ------------------ REQUEST SERVICES ------------------

def get_all_requests():
    return list(requests_col.find({}, {"_id": 0}))

def update_request_status(request_id, new_status):
    req = requests_col.find_one({"requestId": request_id})

    if not req:
        return {"error": "Request not found"}

    if new_status == "sent":
        balance = get_current_balance()

        if int(req["amount"]) > balance:
            requests_col.update_one(
                {"requestId": request_id},
                {"$set": {"status": "insufficient"}}
            )
            return {"status": "insufficient"}

        # 🧱 Prevent duplicate expense entry
        existing = expenses_col.find_one({"requestId": request_id})
        if not existing:
            expenses_col.insert_one({
                "memberName": req["memberName"],
                "amount": int(req["amount"]),
                "reason": req["reason"],
                "requestId": request_id,
                "createdAt": datetime.utcnow().isoformat()
            })

    requests_col.update_one(
        {"requestId": request_id},
        {"$set": {"status": new_status}}
    )

    return {"status": new_status}

# ------------------ ANALYTICS ------------------

def get_analytics():
    total_fund = get_total_fund()
    total_expense = get_total_expense()
    current_balance = total_fund - total_expense

    member_map = defaultdict(int)
    monthly = defaultdict(int)

    expenses = list(expenses_col.find({}))

    for e in expenses:
        member_map[e["memberName"]] += int(e["amount"])

        dt = datetime.fromisoformat(e["createdAt"])
        month_key = dt.strftime("%Y-%m")
        monthly[month_key] += int(e["amount"])

    return {
        "totalFund": total_fund,
        "totalExpense": total_expense,
        "currentBalance": current_balance,
        "memberMap": dict(member_map),
        "monthly": dict(monthly)
    }
