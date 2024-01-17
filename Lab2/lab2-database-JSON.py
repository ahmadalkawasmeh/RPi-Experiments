'''
Script to access weather data from openweathermap.org using a REST API
Data are returned as a JSON string
The JSON string is then deserialized/parsed into a Python dictionary
Sample data fields are printed.

See http://openweathermap.org/current#current for the API

Originally written by Cheryl Schramm ~2015
Updated by James Green Jan-2023
'''

from urllib.request import urlopen
from urllib.parse import urlencode
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# Prof Schramm created this API key several years ago. If it doesn’t work, get your own.
apiKey = "a808bbf30202728efca23e099a4eecc7"
# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"metric", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print(f"Requesting data from URL: {url}")
webData = urlopen(url)
results = webData.read().decode('utf-8')  # results is a JSON string
webData.close()

print("The raw JSON string returned by the query is")
print(results)

# Deserialize/parse the JSON string into a Python Dictionary data structure
# See https://www.geeksforgeeks.org/json-loads-in-python/ for loads details
data = json.loads(results)

# Use the Dictionary to print specific fields from the data

print ("Temperature: %d%sC" % (data["main"]["temp"], chr(176) ))

print ("Humidity: %d%%" % data["main"]["humidity"])

print ("Pressure: %d" % data["main"]["pressure"] )

print ("Wind : %d" % data["wind"]["speed"])

# save the wind speed value
windvalue= (data["wind"]["speed"])

# save the city name
cityname = data["name"]

# connect to database or create it if it doesn't exist
conn = sqlite3.connect('lab2weatherDB.db')

# to access columns by name we need to set row_factory to sqlite3.Row class
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

# conditional table creation
table_creation_query = ("CREATE TABLE IF NOT EXISTS Winds(City TEXT, Date DATETIME DEFAULT CURRENT_TIMESTAMP, "
                        "WindSpeed FLOAT)")

# table created
cursor.execute(table_creation_query)

# data insertion query
cursor.execute('''INSERT INTO Winds(City, WindSpeed) values (?, ?)''', (cityname, windvalue))

# Function to check and output wind speed comparison
def compare_wind_speed(city, new_wind_speed):
    # Query to get the most recent wind speed for the given city
    query = f'''
        SELECT WindSpeed FROM Winds
        WHERE City = ? 
        ORDER BY Date DESC
        LIMIT 1
    '''
    cursor.execute(query, (city,))
    result = cursor.fetchone()

    if result:
        most_recent_wind_speed = result[0]
        if new_wind_speed > most_recent_wind_speed:
            print(f"The new wind speed ({new_wind_speed}) is higher than the most recent ({most_recent_wind_speed}) for {city}.")
        elif new_wind_speed < most_recent_wind_speed:
            print(f"The new wind speed ({new_wind_speed}) is lower than the most recent ({most_recent_wind_speed}) for {city}.")
        else:
            print(f"The new wind speed ({new_wind_speed}) is the same as the most recent for {city}.")
    else:
        print(f"No previous records found for {city}.")

compare_wind_speed(cityname, windvalue)

conn.commit()
conn.close()
