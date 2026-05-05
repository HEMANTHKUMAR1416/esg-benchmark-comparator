from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime
import json

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.json

    prompt = f"""
    You are an ESG analyst.

    Generate a structured ESG report:

    Company: {data.get("company_name")}
    Environment Score: {data.get("env_score")}
    Social Score: {data.get("social_score")}
    Governance Score: {data.get("gov_score")}
    Notes: {data.get("notes")}

    Return STRICT JSON with:
    title, summary, overview, key_items, recommendations
    """

    result = call_groq(prompt)

    print("RAW AI RESPONSE:", result)  # 👈 DEBUG

    try:
        parsed = json.loads(result)
        return jsonify(parsed)

    except Exception as e:
        return jsonify({
            "error": "Invalid AI response",
            "raw": result,
            "generated_at": datetime.utcnow().isoformat()
        })