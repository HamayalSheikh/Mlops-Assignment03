# scripts/train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

df = pd.read_csv('data/processed/processed_data.csv')
X = df[['humidity', 'wind_speed']]  # features
y = df['temperature']               # target

model = LinearRegression().fit(X, y)

# Save the model
os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
