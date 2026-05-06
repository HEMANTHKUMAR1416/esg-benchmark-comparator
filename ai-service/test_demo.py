import requests

url = "http://127.0.0.1:5000/describe"

demo_data = [
    {
        "company_name": f"Company {i}",
        "envScore": i % 100,
        "socialScore": (i * 2) % 100,
        "govScore": (i * 3) % 100,
        "notes": "Demo company data"
    }
    for i in range(1, 31)
]

for data in demo_data:
    res = requests.post(url, json=data)
    print(data["company_name"], "->", res.json())