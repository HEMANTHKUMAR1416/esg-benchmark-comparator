from flask import Blueprint, request, jsonify
from services.groq_client import generate_ai_response

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    try:
        data = request.get_json()

        # 🔥 IMPORTANT: pass JSON (dict), not string
        ai_response = generate_ai_response(data)

        return jsonify({
            "generated_at": ai_response["generated_at"],
            "report": ai_response["result"],
            "is_fallback": ai_response["is_fallback"],
            "response_time": ai_response["response_time"]
        })

    except Exception as e:
        print("REPORT ERROR:", str(e))
        return jsonify({
            "generated_at": "",
            "report": "Error generating report",
            "is_fallback": True,
            "response_time": 0
        }), 500