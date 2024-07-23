from flask import Flask, render_template, request, jsonify
from model import prompt_llama2, prompt_llama3_70b, prompt_llama3_8b, callerMessageTemplate
import json

import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/llama2', methods=['POST'])
def llama2():
    """
    Interact with Llama2 model.
    """
    user_message = request.form['prompt']
    SYSTEM_MESSAGE = "You are a Support Engineer from support team receiving a message from a caller. " + callerMessageTemplate()
    start_time = time.time()
    response = prompt_llama2(SYSTEM_MESSAGE, user_message)
    result = json.loads(response)
    result['duration'] = time.time() - start_time
    return jsonify(response)

@app.route('/llama3_70b', methods=['POST'])
def llama3_70b():
    """
    Interact with Llama3 model.
    """
    user_message = request.form['prompt']
    SYSTEM_MESSAGE = "You are a Support Engineer from support team receiving a message from a caller. " + callerMessageTemplate()
    start_time = time.time()
    response = prompt_llama3_70b(SYSTEM_MESSAGE, user_message)
    result = json.loads(response)
    result['duration'] = time.time() - start_time
    return jsonify(response)

@app.route('/llama3_8b', methods=['POST'])
def llama3_8b():
    """
    Interact with Llama3 8b model.
    """
    user_message = request.form['prompt']
    SYSTEM_MESSAGE = "You are a Support Engineer from support team receiving a message from a caller. " + callerMessageTemplate()
    start_time = time.time()
    response = prompt_llama3_8b(SYSTEM_MESSAGE, user_message)
    stripped_response = response[response.find('{'):response.rfind('}')+1]
    print(stripped_response)
    result = json.loads(stripped_response)
    result['duration'] = time.time() - start_time
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)