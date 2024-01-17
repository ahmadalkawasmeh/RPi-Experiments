# SYSC3010 Lab2 Deliverables

## The deliverables consist of:

### 1. `lab2-database-data-logger.py`
   - A Python script that reads the temperature, humidity, <br>and pressure from the sense hat and inserts this data into a table <br>in an sqlite3 database.

### 2. `lab2-database-manager.png`
   - A screenshot of the data contained in the database <br>created by the script in number 1 accessed through the gui <br>database manager.

### 3. `lab2-database-data-visualizer.py`
   - A Python script that turns the logged data from number <br>1 into a line plot, generated through plotly using a dataframe.

### 4. `lab2-database-plot.png`
   - A screenshot of the generated plot from the script in number 3.

### 5. `lab2-database-JSON.py`
   - A Python script that retrieves the weather data for a <br>particular city, then inserts the wind speed into a table in a <br>databse, then for every subsequent data retrieval for the same <br>city, it compares the new data with the most recent entry and <br>reports wether there is a difference.