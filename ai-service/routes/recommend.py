from flask import Blueprint, request, jsonify
from services.groq_client import generate_ai_response
from datetime import datetime

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json

        # Create prompt (simple and clear)
        prompt = f"""
        Give ESG improvement recommendations for the company:
        Name: {data.get('company_name')}
        Environmental Score: {data.get('envScore')}
        Social Score: {data.get('socialScore')}
        Governance Score: {data.get('govScore')}
        Notes: {data.get('notes')}
        """

        # Call AI
        ai_response = generate_ai_response(prompt)

        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "result": ai_response["result"],
            "is_fallback": ai_response["is_fallback"],
            "response_time": ai_response["response_time"]
})
    except Exception as e:
        return jsonify({
            "generated_at": datetime.utcnow().isoformat(),
            "recommendations": "Error generating recommendations",
            "is_fallback": True,
            "response_time": 0
        }), 500