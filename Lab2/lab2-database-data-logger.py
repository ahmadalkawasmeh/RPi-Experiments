from sense_hat import SenseHat
import time
import sqlite3

# get the pressure, humidity and temperature readings, round to 1 digit
# init sensehat
sense = SenseHat()

# connect to database
dbconnect = sqlite3.connect("sensorDB.db")

# to access columns by name we need to set row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row

# create cursor to work with db
cursor = dbconnect.cursor()

# collect data every 1 second and insert into table
for i in range(30):
    idn = i
    temp = round(sense.get_temperature(), 1)
    hum = round(sense.get_humidity(), 1)
    press = round(sense.get_pressure(), 1)
    cursor.execute('''INSERT INTO sensordata (ID, temperature, humidity, pressure) VALUES (?, ?, ?, ?)''',
                   (idn, temp, hum, press))
    time.sleep(1)

dbconnect.commit()
dbconnect.close()
