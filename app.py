from flask import Flask, render_template, request, jsonify
import json
import re

app = Flask(__name__)

# Load responses
with open("responses.json", encoding="utf-8") as file:
    data = json.load(file)

def get_bot_response(user_input):
    user_input = user_input.lower()

    # Remove punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)

    # INTENTS (keywords)
    keywords = {
        "fee": ["fee", "fees", "payment", "pay fee", "fee details"],
        "courses": ["course", "courses", "branches", "subjects"],
        "admission": ["admission", "apply", "join", "enroll"],
        "hostel": ["hostel", "accommodation", "stay"],
        "placement": ["placement", "jobs", "companies"],
        "syllabus": ["syllabus", "pdf", "materials"],

        "events": ["events", "fest", "functions"],
        "sports": ["sports", "games", "cricket", "football"],
        "clubs": ["clubs", "activities"],
        "facilities": ["facilities", "labs", "infrastructure"],
        "wifi": ["wifi", "internet"],
        "internship": ["internship", "training"],

        # 🔥 IMPORTANT (YOUR ISSUE FIX)
        "contact": ["contact", "phone", "email", "call", "reach"],
        "address": ["address", "location", "where", "place"]
    }

    # Match keywords
    for intent, words in keywords.items():
        for word in words:
            if word in user_input:
                return data.get(intent, "Information not available.")

    return "Sorry, I didn't understand. Try asking about fees, courses, admission, hostel, or contact details."

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.form["msg"]
    response = get_bot_response(user_msg)
    return jsonify({"response": response})

# Run
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)