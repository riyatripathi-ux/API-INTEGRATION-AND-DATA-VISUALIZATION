import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

# --- Configuration ---
API_KEY = 'your_api_key_here'  # Replace with your API key
CITY = 'New York'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# --- Fetch Weather Data ---
response = requests.get(URL)
if response.status_code != 200:
    raise Exception(f"API Error: {response.status_code}, {response.json()}")

weather_data = response.json()

# --- Parse Data ---
timestamps = []
temps = []
humidity = []
wind_speed = []

for entry in weather_data['list']:
    timestamps.append(datetime.fromtimestamp(entry['dt']))
    temps.append(entry['main']['temp'])
    humidity.append(entry['main']['humidity'])
    wind_speed.append(entry['wind']['speed'])

# --- Create DataFrame ---
df = pd.DataFrame({
    'Timestamp': timestamps,
    'Temperature (°C)': temps,
    'Humidity (%)': humidity,
    'Wind Speed (m/s)': wind_speed
})

# --- Set Style ---
sns.set(style='whitegrid')
plt.figure(figsize=(14, 10))

# --- Subplot 1: Temperature ---
plt.subplot(3, 1, 1)
sns.lineplot(data=df, x='Timestamp', y='Temperature (°C)', marker='o', color='red')
plt.title(f'Temperature Forecast - {CITY}')
plt.xticks(rotation=45)

# --- Subplot 2: Humidity ---
plt.subplot(3, 1, 2)
sns.lineplot(data=df, x='Timestamp', y='Humidity (%)', marker='o', color='blue')
plt.title('Humidity Forecast')
plt.xticks(rotation=45)

# --- Subplot 3: Wind Speed ---
plt.subplot(3, 1, 3)
sns.lineplot(data=df, x='Timestamp', y='Wind Speed (m/s)', marker='o', color='green')
plt.title('Wind Speed Forecast')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
