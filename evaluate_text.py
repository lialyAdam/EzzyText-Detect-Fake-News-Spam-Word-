from flask import Flask, request, jsonify, render_template_string
from dotenv import load_dotenv
import os
import requests
import json
import re

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string(open("index.html", encoding="utf-8").read())

@app.route("/analyze", methods=["POST"])
def analyze():
    user_text = request.json.get("text", "")
    if not user_text:
        return jsonify({"error": "Please enter text"}), 400

    instruction = """
INSTRUCTION:

You will be evaluating a human/LLM generated text based on an evaluation protocol along several policy dimensions...

TEXT:

{{MyText}}

OUTPUT FORMATTING:

Respond ONLY with a JSON object containing the keys:
"fakeNews", "SpamWord", and "explanation".
- "fakeNews" and "SpamWord" values should be integers from 1 to 5.
- "explanation" should be a brief string explaining your evaluation.
Do not include any other text.
"""
    prompt = instruction.replace("{{MyText}}", user_text)

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You analyze the quality of responses produced by LLMs based on the instructions provided in the prompt."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result_text = response.json()['choices'][0]['message']['content']
    except Exception as e:
        return jsonify({"error": f"OpenAI API error: {e}"}), 500

    try:
        match = re.search(r"\{.*\}", result_text, re.DOTALL)
        if match:
            result_json = json.loads(match.group())
        else:
            raise ValueError("No valid JSON found in output.")
    except json.JSONDecodeError as e:
        return jsonify({"error": f"JSON decode error: {e}\nRaw: {result_text}"}), 500

    return jsonify(result_json)

if __name__ == "__main__":
    app.run(debug=True)
