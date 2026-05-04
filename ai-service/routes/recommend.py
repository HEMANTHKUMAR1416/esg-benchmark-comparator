from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import json

recommend_bp = Blueprint("recommend", __name__)

def load_prompt():
    with open("prompts/recommend_prompt.txt", "r") as file:
        return file.read()

def validate_input(data):
    required_fields = ["company_name", "env_score", "social_score", "gov_score", "notes"]
    
    for field in required_fields:
        if field not in data:
            return f"{field} is required"
    
    return None

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    # Validate input
    error = validate_input(data)
    if error:
        return jsonify({"error": error}), 400

    # Load prompt
    prompt_template = load_prompt()

    prompt = prompt_template.format(
        company_name=data["company_name"],
        env_score=data["env_score"],
        social_score=data["social_score"],
        gov_score=data["gov_score"],
        notes=data["notes"]
    )

    # Call AI
    result = call_groq(prompt)

    try:
        recommendations = json.loads(result)
    except:
        return jsonify({
            "error": "Invalid AI response format",
            "raw_output": result
        }), 500

    return jsonify({
        "recommendations": recommendations
    })