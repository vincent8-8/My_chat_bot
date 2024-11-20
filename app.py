from flask import Flask, render_template, request, jsonify
from anthropic import Anthropic
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

app = Flask(__name__)

# API 키 가져오기
api_key = os.getenv('ANTHROPIC_API_KEY')
if not api_key:
    raise ValueError("API 키가 설정되지 않았습니다. .env 파일이나 환경 변수를 확인해주세요.")

anthropic = Anthropic(api_key=api_key)

def call_claude_api(prompt):
    try:
        message = anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    bot_response = call_claude_api(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)