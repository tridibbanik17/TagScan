from flask import Flask, request, jsonify
import json
import google.generativeai as genai
import PIL.Image
import os

def get_tag_info(path):
    try:
        print(f"Processing image: {path}")
        prompt = """Is this a laundry tag? If so, what does each laundry icon on it represent?
        Use this schema:
        {is_tag: bool, tag = {Laundry icon name: Icon instructions}}
        For example:
        output could be {True, {"Do not bleach": "This clothing cannot be bleached as it could lead to discoloration."}}
        Ensure that each icon's instructions are no more than two sentences.
        """
        
        genai.configure(api_key="AIzaSyAPfW7HmuKCBDWbNJSd_Ceh9VxbMWVhzYs")  # Gemini API key
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        user_image = PIL.Image.open(path)
        
        # Generate content from the model
        response = model.generate_content([prompt, user_image])
        content = response._result.candidates[0].content.parts[0].text
        print(f"Received response: {content}")

        # Clean the output and parse it into JSON
        content_cleaned = content.strip("```json\n").strip("\n```")
        json_data = json.loads(content_cleaned)
        json_string = json.dumps(json_data)  # Convert to string
        
        # If it's a valid laundry tag
        if json_data.get("is_tag", False):
            return json_string
        else:
            return json.dumps({"message": "Image is not a laundry tag"})
    except Exception as e:
        print(f"Error in get_tag_info: {e}")
        return json.dumps({"message": "Error processing the image"})
