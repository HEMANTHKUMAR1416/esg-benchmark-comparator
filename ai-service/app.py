from flask import Flask
from services.model_loader import get_model
app = Flask(__name__)   # ✅ FIRST create app
# 🔥 preload model at startup
model = get_model()
print("✅ Sentence Transformer loaded at startup")
# import after app creation
from routes.generate_report import report_bp
from routes.describe import describe_bp
from routes.recommend import recommend_bp

# register routes
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)

if __name__ == "__main__":
    app.run(debug=True)