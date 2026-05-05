from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_client import call_groq

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.json

    prompt = f"""
    Analyze the ESG performance of the company:

    Company: {data.get("company_name")}
    Environment Score: {data.get("env_score")}
    Social Score: {data.get("social_score")}
    Governance Score: {data.get("gov_score")}
    Notes: {data.get("notes")}

    Provide a concise summary.
    """

    result = call_groq(prompt)

    return jsonify({
        "summary": result,   # ✅ IMPORTANT FIX
        "generated_at": datetime.utcnow().isoformat()
    })