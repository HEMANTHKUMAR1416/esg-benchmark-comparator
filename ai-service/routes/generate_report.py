from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from datetime import datetime

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    try:
        data = request.json

        # Create structured prompt
        prompt = f"""
        Generate a structured ESG report for the company:

        Name: {data.get('company_name')}
        Environmental Score: {data.get('envScore')}
        Social Score: {data.get('socialScore')}
        Governance Score: {data.get('govScore')}
        Notes: {data.get('notes')}

        Output format:
        - Title
        - Summary
        - Overview
        - Key Insights
        - Recommendations
        """

        # Call AI
        ai_response = call_groq(prompt)

        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "report": ai_response["result"],
            "is_fallback": ai_response["is_fallback"],
            "response_time": ai_response["response_time"]
        })

    except Exception as e:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "report": "Error generating report",
            "is_fallback": True,
            "response_time": 0
        }), 500