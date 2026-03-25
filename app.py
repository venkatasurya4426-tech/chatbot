from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load responses (UTF-8 for emojis)
with open("responses.json", encoding="utf-8") as file:
    data = json.load(file)

def get_bot_response(user_input):
    user_input = user_input.lower()

    for key in data:
        if key in user_input:
            return data[key]

    return "Sorry, I didn't understand that. Try asking about fees, courses, or admissions."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.form["msg"]
    response = get_bot_response(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)