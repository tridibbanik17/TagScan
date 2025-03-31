<div align="center">

<h3 align="center">TagScan</h3>

  <p align="center">
    AI-powered cloth tag reader with Flask backend and React frontend.
    <br />
     <a href="https://github.com/tridibbanik17/tagscan">github.com/tridibbanik17/tagscan</a>
  </p>
</div>

## Table of Contents

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
      </ul>
    </li>
    <li><a href="#architecture">Architecture</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

TagScan is an AI-powered cloth tag reader that utilizes a Flask backend and a React frontend. The backend processes image uploads, leveraging the Gemini API to identify laundry tags and interpret their symbols. The React frontend provides a user interface for image selection and upload, displaying the backend's analysis of the tag.

### Key Features

- **Image Upload and Processing:** Allows users to upload images of laundry tags for analysis.
- **AI-Powered Tag Recognition:** Uses the Gemini API to identify laundry tags and decode the meaning of each symbol.
- **Flask Backend:** Provides an API endpoint for handling image uploads and processing.
- **React Frontend:** Offers a user-friendly interface for interacting with the backend.
- **CORS Support:** Enables cross-origin requests, allowing the frontend and backend to run on different ports.

## Architecture

The project consists of two main components:

- **Frontend (React):**  The React frontend allows users to select an image from their local system and send it to the backend for processing. It uses `axios` for making HTTP requests. Key files include:
    - `src/App.jsx`:  Handles image selection, upload, and display of results.
    - `src/main.jsx`:  Entry point for the React application.
- **Backend (Flask):**  The Flask backend provides an API endpoint (`/process`) that accepts image files, processes them using the Gemini API, and returns the results. It uses `flask-cors` to handle cross-origin requests. Key files include:
    - `backend.py` or `testFullStack/backend/flask_file.py`: Defines the Flask application and API endpoints.
    - `testFullStack/backend/egbackendpyfile.py`: Contains the `get_tag_info` function, which uses the Gemini API to process the image.

## Getting Started

To get started with the project, follow these steps:

### Prerequisites

- Python 3.x
- Node.js (for React frontend)
- Flask
- Flask-CORS (for handling cross-origin requests)
- Axios (for making HTTP requests in React)
- Google Gemini API key

### Installation

1.  **Backend (Flask) Setup:**

    Install the required Python dependencies:

    ```bash
    pip install Flask flask-cors google-generativeai Pillow
    ```

2.  Set the Gemini API key as an environment variable.

3.  Run the Flask backend:

    Navigate to the backend directory (either `tridibbanik17-tagscan` or `tridibbanik17-tagscan/testFullStack/backend`) and execute:

    ```bash
    python backend.py  # or python flask_file.py
    ```

    The backend will start on `http://localhost:5000`.

4.  **Frontend (React) Setup:**

    Ensure you have Node.js installed.

5.  Install the necessary frontend dependencies:

    Navigate to the frontend directory (`tridibbanik17-tagscan/testFullStack/frontend`) and run:

    ```bash
    npm install axios
    ```

6.  Start the React development server:

    ```bash
    npm start
    # or
    npm run dev
    ```

    The frontend will be available at `http://localhost:3000`.

7.  **Using the Application:**

    - Open the frontend in your browser.
    - Select an image file and click "Upload Image."
    - The result of the image processing will be displayed below the button.

## Acknowledgments

- This README was created using [gitreadme.dev](https://gitreadme.dev) — an AI tool that looks at your entire codebase to instantly generate high-quality README files.
- The project utilizes the Gemini API for image analysis.
