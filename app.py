# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the machine learning model from the new pickle file
model = joblib.load('model.pkl')  # Replace with the actual name of your model file

# Map company names to numerical values
company_mapping = {'AMD': 0, 'ASUS': 1, 'INTEL': 2, 'MSI': 3, 'NVIDIA': 4}

@app.route('/')
def index():
    return render_template('index.html', prediction_result=None)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        low = float(request.json['Low'])
        high = float(request.json['High'])
        volume = float(request.json['Volume'])
        open_price = float(request.json['Open'])
        year = int(request.json['Year'])
        month = request.json['Month']
        day = int(request.json['Day'])
        company = request.json['Company']

        # Convert month to numerical representation
        month_mapping = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
            'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        month_numeric = month_mapping.get(month, 1)

        # Map company name to numerical value
        company_numeric = company_mapping.get(company, 0)

        # Make predictions using the loaded model
        input_data = [[low, high, volume, open_price, year, month_numeric, day, company_numeric]]
        prediction = model.predict(input_data)

        # Return the prediction as JSON
        return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
