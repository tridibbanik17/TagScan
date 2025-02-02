from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS for handling cross-origin requests
from data import process_data  # This is from the data.py file, where the data processing logic is specified

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests (React running on a different port)

@app.route('/process', methods=['POST']) #Defines a route (like a URL) ending in /process, and accepts a 'POST' request
def process(): #This function will handles the requests that come from the webpage whose URL ends with the /process
    print("Received Data: ", request.json) # request.json is simply the user input in json form
    data = request.json.get('data') # 'data' is the key for the json input, so this basically just gets the user input
    
    if not data: #Error handling
        # Return an error if no data is provided
        return jsonify({"error": "No data provided"}), 400

    # Process the data (you can replace this with your actual logic)
    result = process_data(data)
    
    # Return the processed result as JSON
    return jsonify({"result": result}) # jsonify takes input, converts it to JSON form, and changed the HTTP header to match the conversion

if __name__ == '__main__': 
    app.run(debug=True)  # Run Flask with debugging enabled (only for development)

