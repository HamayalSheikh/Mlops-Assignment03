FROM apache/airflow:2.9.0-python3.12

USER airflow
RUN pip install scikit-learn

# USER airflow
