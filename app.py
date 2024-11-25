from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# JokeAPI endpoint
JOKE_API = "https://v2.jokeapi.dev/joke/Any"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_joke', methods=['GET'])
def get_joke():
    # Fetch a random joke from the API
    response = requests.get(JOKE_API)
    joke_data = response.json()
    
    # Extract joke information
    if joke_data.get("type") == "single":
        joke = joke_data.get("joke")  # Single-line joke
    else:
        joke = f"{joke_data.get('setup')} {joke_data.get('delivery')}"  # Two-part joke

    return jsonify({"joke": joke})

if __name__ == '__main__':
    app.run(debug=True)
