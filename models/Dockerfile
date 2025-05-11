# Base Image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY ../scripts/train_model.py /app/train_model.py
COPY ../requirements.txt /app/requirements.txt
COPY ../data /app/data
# COPY models /app/models
COPY ../models /app/models


# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables for MLflow tracking
ENV MLFLOW_TRACKING_URI=http://localhost:5000

# Run the application
CMD ["python", "train_model.py"]
