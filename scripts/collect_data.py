# # scripts/collect_data.py
# import requests, csv, time
# from datetime import datetime

# API_KEY = "65fd833bd0877ed9ae3333d9417463f0"
# CITY = "Lahore"
# URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# def collect_weather_data():
#     data = []
#     for _ in range(5):  # simulate 5 days
#         response = requests.get(URL).json()
#         record = {
#             "temperature": response["main"]["temp"],
#             "humidity": response["main"]["humidity"],
#             "wind_speed": response["wind"]["speed"],
#             "weather": response["weather"][0]["main"],
#             "timestamp": datetime.utcnow().isoformat()
#         }
#         data.append(record)
#         time.sleep(86400)  # Sleep 24 hours for real scenario, simulate for test

#     with open('data/raw/raw_data.csv', 'w', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=data[0].keys())
#         writer.writeheader()
#         writer.writerows(data)

# if __name__ == "__main__":
#     collect_weather_data()

import requests
import csv
from datetime import datetime, timezone

API_KEY = '65fd833bd0877ed9ae3333d9417463f0'  # Replace with your actual API key
CITY = 'Karachi'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def collect_weather_data():
    response = requests.get(URL)
    data = response.json()

    print("API Response: ", data)  # This will show the raw API response

    # Check if the 'main' key exists in the response data
    if 'main' in data:
        weather_record = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'weather_condition': data['weather'][0]['main'],
            'datetime': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            # 'datetime': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Specify the file path to save the raw data
        filename = 'data/raw/raw_data.csv'

        # Write header if file doesn't exist
        try:
            with open(filename, 'x', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=weather_record.keys())
                writer.writeheader()
                writer.writerow(weather_record)
        except FileExistsError:
            # Append to the file if it already exists
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=weather_record.keys())
                writer.writerow(weather_record)

        print("Weather data saved successfully.")
    else:
        print("Error: Unable to find expected 'main' data in the response.")
        # You can print additional error info if needed
        print("Response structure:", data)

if __name__ == '__main__':
    collect_weather_data()
