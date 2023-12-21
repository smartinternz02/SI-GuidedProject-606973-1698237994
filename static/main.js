// static/main.js

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('predictionForm');
    const resultDiv = document.getElementById('predictionResult');

    // Add event listener to form
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        submitAndPredict();
    });

    // Function to submit form and predict
    function submitAndPredict() {
        // Get form data
        const formData = {
            Low: document.getElementById('Low').value,
            High: document.getElementById('High').value,
            Volume: document.getElementById('Volume').value,
            Open: document.getElementById('Open').value,
            Year: document.getElementById('Year').value,
            Month: document.getElementById('Month').value,
            Day: document.getElementById('Day').value,
            Company: document.getElementById('Company').value,
        };

        // Perform an AJAX request to send data to the backend
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            // Display the prediction result
            resultDiv.innerHTML = `<p>Prediction result: ${data.prediction}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors if needed
        });
    }
});
