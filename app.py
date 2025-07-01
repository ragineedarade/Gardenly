import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

# --- WARNING: FOR TESTING PURPOSES ONLY ---
# Hardcoding your API key is NOT secure for production applications.
# It exposes your key to anyone who can access your code.
# Always use environment variables or a secure configuration management system in production.
API_KEY = "AIzaSyDSr_72ZtflK4VM1UJ129I38JJRNgCq-uE" # <--- YOUR GOOGLE GEMINI API KEY HERE
# --- END OF WARNING ---

if not API_KEY:
    # This check will now only trigger if you accidentally delete the key above
    raise ValueError("API_KEY is not set in the script. Please provide your key.")

# Configure the generative AI model with your API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') 

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app) 

@app.route('/')
def index():
    return render_template('chatbot.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({'botResponse': 'Please provide a message.'}), 400

    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_message)
        bot_response = response.text
        
        return jsonify({'botResponse': bot_response})
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return jsonify({'botResponse': 'An error occurred while getting the AI response. Please try again.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
