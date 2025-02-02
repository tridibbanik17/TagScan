import React, { useState } from 'react';
import axios from 'axios'; //Library used to make HTTP requests

function App() {
  // The 2 consts below are useState hooks (basically, inputData is a variable that'll hold the value entered by the user, response will be the processed data from the backend)
  const [inputData, setInputData] = useState('');  // State to hold input data
  const [responseData, setResponseData] = useState('');  // State to display the response

  // Handle processing when the button is clicked
  const handleProcessData = async () => { // This is a function which is triggered when the 'Process' button is pressed on the webpage 
    console.log("Button clicked, processing data...");
    try {
      // Make the POST request to Flask backend
      const response = await axios.post('http://localhost:5000/process', { //This sends an HTTP 'POST' request to the backend (flask file)
        data: inputData,  // Send the input data to Flask (sent in JSON format)
      });
      // Set the processed result to be displayed
      setResponseData(response.data.result); //The processed data is extracted from 'resonse.data.result' and stored in the responseData variable from above
    } catch (error) { //Error handling
      console.error('Error processing data:', error);
      setResponseData('Error processing data');
    }
  };

  return (
    // Defines the UI of the page
    <div>
      <h1>Basic Data Processor</h1>
      <input
        type="text"
        value={inputData}
        onChange={(e) => setInputData(e.target.value)}  // Update inputData on change
        placeholder="Enter data here"
      />
      <button onClick={handleProcessData}>Process</button>
      <p>{responseData}</p>  {/* Display the result or error */}
    </div>
  );
}

export default App; //This is needed for the file to be imported by main.jsx, where this function is called
