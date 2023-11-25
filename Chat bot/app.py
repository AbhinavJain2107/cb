from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = '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'

def get_chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = get_chatbot_response(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
