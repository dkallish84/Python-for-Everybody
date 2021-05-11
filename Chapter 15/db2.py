# Now that we have created a table named Tracks, we can put some data into that table using the SQL INSERT operation. Again, we begin by making a connection to the database and obtaining the cursor. We can then execute SQL commands using the cursor.

# Import the sqlite library
import sqlite3

# Create a connection object and a 'cursor', similar to a file handle
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# Insert two new rows into the database using SQL statements and tuples
cur.execute('INSERT INTO Tracks VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks VALUES (?, ?)', ('My Way', 15))

# Commit the changes to the file from memory
conn.commit()

# Print the results
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

# Delete the added data to reset the database
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

# Close the connection to the database
conn.close()
