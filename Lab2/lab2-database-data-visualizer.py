# pandas data frame reads data from sql query
# plotly turns the data into a plot

import pandas as pd

import plotly.express as px

import sqlite3

# connect to db
conn = sqlite3.connect('sensorDB.db')

# query to read data from table
sqlquery = 'SELECT * FROM sensordata'


# Use pandas.read_sql_query to execute the query and read the result into a DataFrame
df = pd.read_sql_query(sqlquery, conn)

fig = px.line(df, x='datetime', y=['temperature', 'humidity', 'pressure'], title='Sensor Data',
              labels={'value': 'Sensor Value', 'variable': 'Sensor Type'}, line_shape='linear')
conn.close()
fig.show()
