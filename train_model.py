import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Dummy dataset for illustration
# In real case, use actual weather and sales data
import numpy as np
np.random.seed(42)
data = pd.DataFrame({
    'Temperature': np.random.randint(15, 40, 100),
    'Humidity': np.random.randint(30, 90, 100),
    'WindSpeed': np.random.randint(0, 20, 100),
    'IsWeekend': np.random.randint(0, 2, 100),
})
data['Revenue'] = (
    200 + data['Temperature'] * 10
    - data['Humidity'] * 2
    - data['WindSpeed'] * 5
    + data['IsWeekend'] * 150
    + np.random.normal(0, 50, 100)
)

X = data.drop('Revenue', axis=1)
y = data['Revenue']

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
