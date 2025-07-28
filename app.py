# from flask import Flask, request, render_template
# from dotenv import load_dotenv
# import os
# import openai

# # Load environment variables
# load_dotenv()

# # Set your API key
# client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("chat.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.form["message"]

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_input}
#         ]
#     )

#     reply = response.choices[0].message.content.strip()
#     return render_template("chat.html", user_input=user_input, reply=reply)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
from together import Together
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

@app.route('/')
def index():
    return render_template('chat.html')  # Ensure index.html exists in templates/

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = client.chat.completions.create(
        model="Qwen/Qwen3-235B-A22B-Thinking-2507",
        messages=[{"role": "user", "content": user_input}]
    )
    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)
