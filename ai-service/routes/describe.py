from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.json

    # Simple prompt
    prompt = f"Describe ESG performance of {data['company_name']}"

    # Call AI
    ai_response = call_groq(prompt)

    return jsonify({
        "generated_at": datetime.utcnow().isoformat(),
        "data": ai_response["result"],
        "is_fallback": ai_response["is_fallback"],
        "response_time": ai_response["response_time"]
    })