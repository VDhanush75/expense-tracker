from app.models.expense_model import get_expenses_by_member
from app.services.serializer import serialize

def fetch_member_expenses(member_id):
    expenses = get_expenses_by_member(member_id)

    expenses = serialize(expenses)

    total = sum(exp["amount"] for exp in expenses)

    return {
        "expenses": expenses,
        "total": total
    }
