# The code to create a database file and a table named Tracks with two columns inthe database is as follows

# Import the sqlite library
import sqlite3

# Create a connection object and a 'cursor', similar to a file handle
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# Delete the table if it already exists, create the table
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# Close the connection to the database
conn.close()
