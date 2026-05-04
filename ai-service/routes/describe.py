from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_client import call_groq

describe_bp = Blueprint("describe", __name__)

def load_prompt():
    with open("prompts/describe_prompt.txt", "r") as file:
        return file.read()

def validate_input(data):
    required_fields = ["company_name", "env_score", "social_score", "gov_score", "notes"]
    
    for field in required_fields:
        if field not in data:
            return f"{field} is required"
    
    return None

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    # 🔍 Validate input
    error = validate_input(data)
    if error:
        return jsonify({"error": error}), 400

    # 🧠 Load prompt
    prompt_template = load_prompt()

    prompt = prompt_template.format(
        company_name=data["company_name"],
        env_score=data["env_score"],
        social_score=data["social_score"],
        gov_score=data["gov_score"],
        notes=data["notes"]
    )

    # 🤖 Call AI
    result = call_groq(prompt)

    # 🕒 Response
    return jsonify({
        "summary": result,
        "generated_at": datetime.utcnow().isoformat()
    })