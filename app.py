
from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

# ✅ Initialize OpenAI client with environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]

    try:
        # ✅ Chat completion using GPT-4o-mini (light & fast)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful and friendly AI assistant created by Opyra Infotech."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=200,
            temperature=0.7
        )

        bot_reply = response.choices[0].message.content.strip()
        return bot_reply

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I'm having trouble responding right now."

# ✅ Hosting-friendly Flask run command
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use dynamic port for hosting
    app.run(host="0.0.0.0", port=port)
