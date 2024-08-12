from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "sk-BtCSeJyGv06T4Y1swTMDnuKW6z_575JFzcct0E9M7tT3BlbkFJNJuvHARbFH2kMdwS3VKxoJF0LSpqOCsXOGv3f_H2MA"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    if user_message.strip() != "":
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",  # or another engine like "gpt-3.5-turbo"
                prompt=user_message,
                max_tokens=2048
            )
            reply = response.choices[0].text.strip()
            return jsonify({"response": reply})
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "Failed to get response from OpenAI"})
    else:
        return jsonify({"error": "Empty message"})

if __name__ == "__main__":
    app.run(debug=True)