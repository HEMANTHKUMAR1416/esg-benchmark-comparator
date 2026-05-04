from flask import Flask, jsonify
from routes.describe import describe_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(describe_bp)

@app.route("/")
def home():
    return jsonify({"message": "AI Service running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)