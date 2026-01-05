from datetime import datetime
from app.config.db import db

def submit_request(data):
    request_doc = {
        "requestId": f"REQ-{int(datetime.now().timestamp())}",
        "memberName": data["memberName"],
        "amount": int(data["amount"]),
        "reason": data["reason"],
        "status": "pending",
        "createdAt": datetime.utcnow().isoformat()
    }

    db["requests"].insert_one(request_doc)

    # ✅ Return contract expected by frontend
    return {
        "success": True,
        "status": "pending",
        "request": {
            "requestId": request_doc["requestId"],
            "memberName": request_doc["memberName"],
            "amount": request_doc["amount"],
            "reason": request_doc["reason"],
            "status": request_doc["status"],
            "createdAt": request_doc["createdAt"]
        }
    }

