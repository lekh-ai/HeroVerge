from flask import Flask, request, jsonify, render_template
from model import prompt_llama2, prompt_llama3_70b, prompt_llama3_8b, callerMessageTemplate, generate_mail_draft_llm
import json

app = Flask(__name__)

def parse_llama2_response(response):
    parsed_output = {
        'summary': response['properties']['summary']['description'],
        'script': response['properties']['script']['description'],
        'sentiment': response['properties']['sentiment']['description'],
        'complete': response['properties']['complete']['description'],
        'notes': response['properties']['notes']['description'],
        'duration': response.get('duration', 'N/A')  # Use default 'N/A' if 'duration' is not found
    }
    return parsed_output

def parse_llama3_response(response):
    parsed_output = {
        'summary': response['summary'],
        'script': response['script'],
        'sentiment': response['sentiment'],
        'complete': response['complete'],
        'notes': response['notes'],
        'duration': response.get('duration', 'N/A')  # Use default 'N/A' if 'duration' is not found
    }
    return parsed_output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_query', methods=['POST'])
def process_query():
    data = request.json
    user_message = data['query']
    model_choice = data['model']

    SYSTEM_MESSAGE = "You are a Support Engineer from support team receiving a message from a caller. " + callerMessageTemplate()

    if model_choice == 'llama2':
        response = prompt_llama2(SYSTEM_MESSAGE, user_message)
        parsed_result = parse_llama2_response(json.loads(response))
    elif model_choice == 'llama3_70b':
        response = prompt_llama3_70b(SYSTEM_MESSAGE, user_message)
        parsed_result = parse_llama3_response(json.loads(response))
    elif model_choice == 'llama3_8b':
        response = prompt_llama3_8b(SYSTEM_MESSAGE, user_message)
        parsed_result = parse_llama3_response(json.loads(response))
    else:
        return jsonify({'error': 'Invalid model choice'}), 400

    mail_draft = generate_mail_draft_llm(parsed_result)

    return jsonify({
        'summary': parsed_result['summary'],
        'script': parsed_result['script'],
        'sentiment': parsed_result['sentiment'],
        'complete': parsed_result['complete'],
        'notes': parsed_result['notes'],
        'mail_draft': mail_draft
    })

if __name__ == '__main__':
    app.run(debug=True)
