import time

import pyrebase
from datetime import datetime
from sense_hat import SenseHat

# Config will contain the information needed to connect to your firebase
#   The API KEY and Project ID are found in your project settings
#   The DB URL can be found under the Realtime Database tab
config = {
    "apiKey": "AIzaSyC3QNNa52-lh5JimhS0zgC0sA_z6XUq3JY",
    "authDomain": "sysc3010-f898a.firebaseapp.com",
    "databaseURL": "https://sysc3010-f898a-default-rtdb.firebaseio.com/",
    "storageBucket": "sysc3010-f898a.appspot.com"
}

# Connect using your configuration
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Initializing sense hat
sense = SenseHat()


# Function to read data from sense hat
def get_sensor_data(sensor_name):
    if sensor_name == "Humidity":
        return round(sense.get_humidity(), 1)

    elif sensor_name == "Temperature":
        return round(sense.get_temperature(), 1)

    elif sensor_name == "Pressure":
        return round(sense.get_pressure(), 1)

    else:
        return "Invalid sensor name"


# Function to write sensor data to database
def write_to_database(username, dataset_name, sample_num):
    counter = 0
    while counter < sample_num:
        # When writing to your DB each child is a JSON key:value pair
        db.child(username).child(dataset_name).child(datetime.now().strftime("%H:%M:%S")).set(
            get_sensor_data(dataset_name))

        # Wait for 1 second to keep the keys unique
        time.sleep(1)

        # The above command will add a JSON string to your DB in the form:
        # {
        #   "username":{
        #     "dataset_name":{
        #       "<timeStamp>":"<sensorValue>"
        #     }
        #   }
        # }

        # Increment the counter
        counter += 1
        # After running the above while loop your DB should look something like this:
        # {
        #   "YOUR_USERNAME":{
        #     "sensor1":{
        #       "0":"0.6335737283"
        #       "1":"0.3235343823"
        #       "2":"0.4263353683"
        #       "3":"0.2394958673"
        #       ...
        #       "9":"0.8472648495"
        #     }
        #   }
        # }


# Next, we will retrieve the data we wrote to the DB
# This code will read all sensor data as a Python dictionary,
# convert it to a list, extract the final entry, and print its
# key and value pair

# Function to read from database and print last elements
def read_data_from_my_database(username, dataset_name):

    if dataset_name == "Temperature":
        # Read data in database, will be a dictionary
        my_temp_db_data = db.child(username).child(dataset_name).get()

        # Make dictionary into a list
        my_temp_db_data_list = my_temp_db_data.each()

        # Get last element from each list
        last_temp = my_temp_db_data_list[-1]

        # Print last Temperature element
        print("     " + str(my_temp_db_data.key()) + ": " + str(last_temp.val()))


    elif dataset_name == "Humidity":
        # Read data in database, will be a dictionary
        my_humi_db_data = db.child(username).child(dataset_name).get()

        # Make dictionary into a list
        my_humi_db_data_list = my_humi_db_data.each()

        # Get last element from each list
        last_humi = my_humi_db_data_list[-1]

        # Print last Humidity element
        print("     " + str(my_humi_db_data.key()) + ": " + str(last_humi.val()))

    elif dataset_name == "Pressure":
        # Read data in database, will be a dictionary
        my_pres_db_data = db.child(username).child(dataset_name).get()

        # Make dictionary into a list
        my_pres_db_data_list = my_pres_db_data.each()

        # Get last element from each list
        last_pres = my_pres_db_data_list[-1]

        # Print last Pressure element
        print("     " + str(my_pres_db_data.key()) + ": " + str(last_pres.val()) + " \n")


    else:
        print("\nMy latest entries are:")

def get_all_data():
    # Iterate over usernames
    for username in db.shallow().get().val():

        print("\nLatest entries by " + username + " are:")

        # Iterate over datasets for each username
        for dataset_name in db.child(username).shallow().get().val():

            db_data = db.child(username).child(dataset_name).get()

            # Make dictionary into a list
            db_data_list = db_data.each()

            # Get last element from each list
            last_entry = db_data_list[-1]

            # Print last Temperature element
            print("     " + str(db_data.key()) + ": " + str(last_entry.val()))


# Adding data to my database
write_to_database("ahmadalkawasmeh", "Temperature", 5)
write_to_database("ahmadalkawasmeh", "Humidity", 5)
write_to_database("ahmadalkawasmeh", "Pressure", 5)
#######################################################################################
# Simulated teammates adding data to my database
write_to_database("teammate1", "Temperature", 5)
write_to_database("teammate1", "Humidity", 5)
write_to_database("teammate1", "Pressure", 5)

write_to_database("teammate2", "Temperature", 5)
write_to_database("teammate2", "Humidity", 5)
write_to_database("teammate2", "Pressure", 5)

write_to_database("teammate3", "Temperature", 5)
write_to_database("teammate3", "Humidity", 5)
write_to_database("teammate3", "Pressure", 5)
#######################################################################################
# Fetching my latest entries
read_data_from_my_database("ahmadalkawasmeh", "default")
read_data_from_my_database("ahmadalkawasmeh", "Temperature")
read_data_from_my_database("ahmadalkawasmeh", "Humidity")
read_data_from_my_database("ahmadalkawasmeh", "Pressure")
#######################################################################################
# Fetching latest entries for all usernames in my database
get_all_data()
