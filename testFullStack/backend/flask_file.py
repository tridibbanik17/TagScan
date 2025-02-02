from flask import Flask, request, jsonify
from flask_cors import CORS
import os 
from egbackendpyfile import get_tag_info  # This is from the backend file, where the data processing logic is specified

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests (React running on a different port)

UPLOAD_FOLDER = 'uploads'  # Folder where images are saved
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Creates folder if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Store the path of UPLOAD_FOLDER for later use

@app.route('/process', methods=['POST'])  # Endpoint to process image
def process():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image_file = request.files['image']
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
    
    print(f"Saving image to: {image_path}")  # Log where the image is being saved
    try:
        image_file.save(image_path)  # Save the image to the specified path
        print(f"Image saved successfully.")
    except Exception as e:
        print(f"Error saving image: {e}")
        return jsonify({"error": "Error saving image"}), 500
    
    try:
        result = get_tag_info(image_path)  # Process the image with backend function
        print(f"Processing result: {result}")  # Log result
        return jsonify({"result": result})  # Return processed data
    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({"error": "Error processing image"}), 500

if __name__ == '__main__':
    app.run(debug=True)
