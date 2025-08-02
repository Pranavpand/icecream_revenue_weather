# Ice Cream Revenue Prediction Based on Weather

This project predicts ice cream shop revenue based on weather conditions using a simple machine learning model and Streamlit UI.

## Features
- Predicts revenue using:
  - Temperature
  - Humidity
  - Wind Speed
  - Weekend or Weekday
- Streamlit web app for user input

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python train_model.py

# Run the web app
streamlit run app.py
```

## Folder Structure
```
.
├── app.py
├── utils.py
├── model.pkl
├── train_model.py
├── requirements.txt
└── README.md
```

## Example
Input:
- Temperature: 32°C
- Humidity: 60%
- Wind Speed: 8 km/h
- Weekend: Yes

Output:
- Predicted Revenue: ₹742.13

## Author
AI-generated template by ChatGPT. Feel free to modify!
"# icecream_revenue_weather" 
