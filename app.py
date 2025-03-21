from flask import Flask, render_template, request, jsonify, session
import requests
import os
import uuid
import json
from datetime import datetime

app = Flask(__name__)
# Generate a random secret key for sessions
app.secret_key = os.urandom(24).hex()

# Groq AI API Configuration
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = ""  # Replace with your actual API key if needed

@app.route('/')
def home():
    # Create a session ID if none exists
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get("message", "")
        session_id = session.get('session_id', str(uuid.uuid4()))
        
        # Log incoming messages for debugging
        print(f"[{datetime.now()}] User message: {user_input}")
        
        # Build the messages array for Groq API
        messages = [
            {"role": "user", "content": user_input}
        ]
        
        # Prepare the request payload with an updated model
        payload = {
            "model": "llama3-70b-8192",  # Updated to a currently supported model
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        # Send request to Groq AI
        response = requests.post(
            GROQ_API_URL, 
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=30
        )
        
        # Log API response for debugging
        print(f"[{datetime.now()}] API Status: {response.status_code}")
        
        if response.status_code != 200:
            error_message = f"API Error {response.status_code}"
            try:
                error_data = response.json()
                print(f"Error details: {json.dumps(error_data)}")
                if 'error' in error_data:
                    error_message += f": {error_data['error'].get('message', '')}"
            except Exception as e:
                print(f"Error parsing API error: {str(e)}")
            
            return jsonify({"response": f"Sorry, I encountered an error: {error_message}"}), 500
        
        # Parse the successful response
        response_data = response.json()
        bot_response = response_data.get("choices", [{}])[0].get("message", {}).get("content",
                                                                                   "I'm not sure how to respond.")
        
        print(f"[{datetime.now()}] Bot response: {bot_response[:100]}...")
        
        return jsonify({"response": bot_response})
    
    except Exception as e:
        print(f"[{datetime.now()}] Exception: {str(e)}")
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500

@app.route('/get_history', methods=['GET'])
def get_history():
    # Since we're not using ChromaDB, return an empty history
    return jsonify({"history": []})

@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    # Since we're not using ChromaDB, return empty data
    return jsonify({"all_data": []})

if __name__ == '__main__':
    print(f"[{datetime.now()}] Starting Flask app...")
    print(f"API URL: {GROQ_API_URL}")
    print(f"API Key (first 5 chars): {GROQ_API_KEY[:5]}...")
    app.run(debug=True, host='0.0.0.0', port=5000)
