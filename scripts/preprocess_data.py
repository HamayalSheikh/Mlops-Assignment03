# # scripts/preprocess_data.py
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# df = pd.read_csv('data/raw/raw_data.csv')
# df.dropna(inplace=True)

# scaler = StandardScaler()
# df[['temperature', 'humidity', 'wind_speed']] = scaler.fit_transform(df[['temperature', 'humidity', 'wind_speed']])
# df.to_csv('data/processed/processed_data.csv', index=False)

import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# df = pd.read_csv('data/raw/raw_data.csv')
# df.dropna(inplace=True)
# Create the processed directory if it doesn't exist
os.makedirs('/opt/airflow/data/processed', exist_ok=True)
# df = pd.read_csv('data/raw/raw_data.csv')

df = pd.read_csv('/opt/airflow/data/raw/raw_data.csv')
df.dropna(inplace=True)
df.to_csv('/opt/airflow/data/processed/processed_data.csv', index=False)


scaler = StandardScaler()
df[['temperature', 'humidity', 'wind_speed']] = scaler.fit_transform(df[['temperature', 'humidity', 'wind_speed']])
# df.to_csv('data/processed/processed_data.csv', index=False)
df.to_csv('/opt/airflow/data/processed/processed_data.csv', index=False)
print("✅ Preprocessing complete.")


# import os
# import platform

# if platform.system() == 'Windows':
#     data_path = os.path.join('data', 'raw', 'raw_data.csv')
# else:
#     data_path = '/opt/airflow/data/raw/raw_data.csv'

# df = pd.read_csv(data_path)
