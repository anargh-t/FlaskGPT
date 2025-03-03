from flask import Blueprint, request, jsonify, session
from chat.ai_handler import get_ai_response

chat_bp = Blueprint("chat", __name__)

# Store chat history in session (Temporary Storage)
@chat_bp.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    prompt = data.get("prompt", "")
    model = data.get("model", "chatgpt")

    if not prompt:
        return jsonify({"error": "Empty prompt"}), 400

    # Get response from AI model
    response = get_ai_response(model, prompt)

    # Store chat history in session
    if "history" not in session:
        session["history"] = []
    session["history"].append({"user": prompt, "bot": response})

    return jsonify({"response": response})

@chat_bp.route("/get_history", methods=["GET"])
def get_history():
    return jsonify({"history": session.get("history", [])})
