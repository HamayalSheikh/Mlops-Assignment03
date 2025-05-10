# scripts/train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import os
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")

# Enable autologging
mlflow.sklearn.autolog()

# Load the data
print("🔄 Loading processed data...")
df = pd.read_csv('data/processed/processed_data.csv')
X = df[['humidity', 'wind_speed']]  # Features
y = df['temperature']               # Target

# Start an MLflow run
with mlflow.start_run():
    print("🚀 Training Linear Regression model...")
    model = LinearRegression().fit(X, y)

    # Log metrics
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2_score", r2)
    mlflow.log_param("model_type", "LinearRegression")

    print(f"📊 Metrics:\n    MSE: {mse}\n    R2 Score: {r2}")

    # Save the model
    os.makedirs('models', exist_ok=True)
    model_path = 'models/model.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    # Log the model artifact
    mlflow.log_artifact(model_path)

    print(f"✅ Model saved and tracked in MLflow: {model_path}")

