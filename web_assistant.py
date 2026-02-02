from gemini_client import *
from flask import Flask, request, render_template

app = Flask(__name__)
client = GeminiClient()  

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["GET"])
def prompt_url():
    user_text = request.args.get("").strip()
    response_text = client.generate_response(user_text)
    return render_template("index.html", user_text=user_text, response_text=response_text)

@app.route("/read-form", methods=["POST"])
def read_form():
    user_text = request.form.get("prompt", "").strip()
    response_text = client.generate_response(user_text)
    return render_template("index.html", user_text=user_text, response_text=response_text)

if __name__ == "__main__":
    app.run()