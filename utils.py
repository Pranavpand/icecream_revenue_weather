import pickle
import pandas as pd

def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def preprocess_input(temp, humidity, wind_speed, is_weekend):
    data = pd.DataFrame({
        'Temperature': [temp],
        'Humidity': [humidity],
        'WindSpeed': [wind_speed],
        'IsWeekend': [1 if is_weekend == "Yes" else 0]
    })
    return data
