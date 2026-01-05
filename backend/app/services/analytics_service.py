

from app.config.db import db
from datetime import datetime

def get_analytics():
    expenses = list(db["expenses"].find({}))
    funds = list(db["funds"].find({}))

    total_fund = sum(int(f["amount"]) for f in funds)
    total_expense = sum(int(e["amount"]) for e in expenses)
    current_balance = total_fund - total_expense

    member_map = {}
    weekly = {}
    monthly = {}
    yearly = {}

    for e in expenses:
        amt = int(e["amount"])
        name = e["memberName"]

        member_map[name] = member_map.get(name, 0) + amt

        date = datetime.fromisoformat(e["createdAt"])
        week = date.strftime("%Y-W%U")
        month = date.strftime("%Y-%m")
        year = date.strftime("%Y")

        weekly[week] = weekly.get(week, 0) + amt
        monthly[month] = monthly.get(month, 0) + amt
        yearly[year] = yearly.get(year, 0) + amt

    return {
        "totalFund": total_fund,
        "totalExpense": total_expense,
        "currentBalance": current_balance,
        "memberMap": member_map,
        "weekly": weekly,
        "monthly": monthly,
        "yearly": yearly
    }
