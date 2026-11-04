from flask import Flask, render_template, request
from prompt_builder import build_prompt

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    prompt = request.form["prompt"]

    final_prompt = build_prompt(prompt)

    return final_prompt

if __name__ == "__main__":
    app.run(debug=True)
