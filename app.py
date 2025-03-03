from flask import Flask, render_template
from config import Config
from chat.routes import chat_bp
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

# Register Blueprints
app.register_blueprint(chat_bp, url_prefix="/chat")

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
