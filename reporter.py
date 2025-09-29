import requests
import json
import csv
import os

# Configuration
API_KEY = "a286721d741b022920e4e771bb6e3ad6"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CSV_FILE = "city_data.csv"
FIELD_NAMES = ['City', 'Country', 'Temperature (C)', 'Humidity (%)', 'Description']

def get_weather_report():
    """Main function to run the simplified weather reporter."""

    # 1. Capture and Validate User Input
    while True:
        city = input("Enter city name: ").strip()
        if city:
            break
        print("City cannot be empty.")

    # 2. Retrieve Data
    try:
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching data: {e}. Check city name or API key.")
        return

    # 3. Parse and Print Data
    try:
        info = {
            'City': data['name'],
            'Country': data['sys']['country'],
            'Temperature (C)': round(data['main']['temp'], 1),
            'Humidity (%)': data['main']['humidity'],
            'Description': data['weather'][0]['description'].capitalize()
        }
    except KeyError:
        print("Error: Failed to parse required data fields.")
        return

    print(f"\n--- Report for {info['City']} ---")
    print(f"Temp: {info['Temperature (C)']:.1f}°C | Humidity: {info['Humidity (%)']}%")
    print(f"Weather: {info['Description']}")
    print("-" * 25)

    # 4. Write to CSV
    file_exists = os.path.exists(CSV_FILE)
    try:
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
            if not file_exists:
                writer.writeheader()
            writer.writerow(info)
            print(f"Data saved to {CSV_FILE}.")
    except Exception as e:
        print(f"Error writing to CSV: {e}")

    # 5. Read and Report from CSV
    print("\n--- Recorded Cities ---")
    try:
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as f:
            records = list(csv.DictReader(f))
            print(f"Total: {len(records)} cities recorded.")
            for r in records:
                print(f"  > {r['City']}: {r['Temperature (C)']}°C")
    except Exception:
        print("No CSV data to report.")

if __name__ == "__main__":
    get_weather_report()