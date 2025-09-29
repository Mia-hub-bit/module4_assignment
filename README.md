# REPORTER.PY: City Weather Reporter
Overview
reporter.py is a command-line application built with Python that retrieves current weather data for any specified city using the OpenWeatherMap API. The program displays a formatted summary to the console, saves the data to a local CSV file, and reports on all previously recorded cities.

Features
Interactive Input: Prompts the user for a city name and validates the input.

Live Data Retrieval: Uses the requests library to fetch current weather data (temperature, humidity, description, etc.).

Error Handling: Catches common API errors (e.g., city not found, unauthorized key).

CSV Persistence: Appends new weather data to a file named city_data.csv.

Reporting: Reads and prints a summary of all cities stored in the CSV file.

Setup
1. Obtain an API Key
Before running the application, you must get a free API key from OpenWeatherMap.

Sign up or log in on the OpenWeatherMap website.

Navigate to the API keys tab in your account.

Copy the generated key.

2. Install Dependencies
This project requires the requests library for making API calls.

Open your terminal or command prompt and run:
pip install requests

3. Configure the Code

How to Run
Make sure you have completed the Setup steps.

Open your terminal in the directory where you saved reporter.py.

Execute the script using the Python interpreter:
python reporter.py

Example Session
The program will prompt you for a city name:

Welcome to the City Weather Reporter.
-----------------------------------
Enter city name: Sample City

--- Report for Sample City---
Temp: 23.5°C | Humidity: 68%
Weather: Clear sky
-------------------------
Data saved to city_data.csv.

--- Recorded Cities ---
Total: 1 cities recorded.
  > Sample City: 23.5°C
Output File
The program creates and updates a CSV file in the same directory:

city_data.csv
City	Country	Temperature (C)	Humidity (%)	Description
Minneapolis USA	18.2	75	Light rain
New York USA	23.5	68	Clear sky
Seattle USA	20.1	60	Few clouds
