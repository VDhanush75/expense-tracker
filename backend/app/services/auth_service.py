
from app.models.user_model import find_user_by_userid

def authenticate_user(user_id, password):
    user = find_user_by_userid(user_id)

    if not user:
        return {"success": False, "message": "User not found"}

    if user["password"] != password:
        return {"success": False, "message": "Invalid password"}

    return {
        "success": True,
        "userId": user["userId"],
        "role": user["role"],
        "name": user["name"]
    }
