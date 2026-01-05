from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

from app.config.db import db
from app.routes.auth_routes import auth_bp
from app.routes.expense_routes import expense_bp
from app.routes.request_routes import request_bp
from app.routes.analytics_routes import analytics_bp
from app.routes.admin_routes import admin_bp



# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(expense_bp)
app.register_blueprint(request_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(admin_bp)


@app.route("/")
def home():
    return {"message": "Backend is running"}

@app.route("/test-db")
def test_db():
    collections = db.list_collection_names()
    return {"status": "connected", "collections": collections}

# ========================
#  EXPENSE EXPORT ROUTES
# ========================

@app.route("/all-expenses", methods=["GET"])
def all_expenses():
    data = list(db["expenses"].find({}, {"_id": 0}))
    return jsonify(data)

@app.route("/export-expenses", methods=["GET"])
def export_expenses():
    member = request.args.get("memberName")
    data = list(db["expenses"].find({"memberName": member}, {"_id": 0}))

@app.route("/export-preview", methods=["GET"])
def export_preview():
    data = list(db["expenses"].find({}, {"_id": 0}))
    return jsonify(data)


@app.route("/add-fund", methods=["POST"])
def add_fund():
    data = request.json
    data["createdAt"] = datetime.now().isoformat()
    db["funds"].insert_one(data)
    return jsonify({"success": True})

@app.route("/fund-history", methods=["GET"])
def fund_history():
    history = list(db["funds"].find({}, {"_id": 0}))
    return jsonify(history)


# ========================

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
