from services.groq_client import call_groq

def load_prompt():
    with open("prompts/describe_prompt.txt", "r") as file:
        return file.read()

def test_case(data):
    prompt = load_prompt().format(**data)
    result = call_groq(prompt)

    print("\n============================")
    print(f"Company: {data['company_name']}")
    print("============================")
    print(result)

if __name__ == "__main__":
    test_data = [
        {
            "company_name": "GreenTech Ltd",
            "env_score": 90,
            "social_score": 85,
            "gov_score": 88,
            "notes": "Strong sustainability practices"
        },
        {
            "company_name": "OilMax Corp",
            "env_score": 20,
            "social_score": 30,
            "gov_score": 25,
            "notes": "High emissions and weak governance"
        },
        {
            "company_name": "MediCare Inc",
            "env_score": 70,
            "social_score": 80,
            "gov_score": 75,
            "notes": "Strong social impact, moderate environmental concerns"
        },
        {
            "company_name": "TechNova",
            "env_score": 85,
            "social_score": 78,
            "gov_score": 82,
            "notes": "Innovative and sustainable operations"
        },
        {
            "company_name": "BuildCorp",
            "env_score": 50,
            "social_score": 60,
            "gov_score": 55,
            "notes": "Average performance across all ESG factors"
        }
    ]

    for data in test_data:
        test_case(data)