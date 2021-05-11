# Simple example of connecting to a database and creating a table to store email addresses and their count of occurrences from a user specified file

import sqlite3

# Connecting to databases requires two parts, as compared to just one for files
# If the database file doesn't exist, it will be created
conn = sqlite3.connect('emaildb.sqlite')
# This part is like the file handle, it is a datbase cursor
cur = conn.cursor()

# Drop the table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')
# Create the table to store the emails and their occurrence counts
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Prompt the user for a file name
fname = input('Enter a file name: ')
# Default to 'mbox-short.txt'
if (len(fname) < 1): fname = 'mbox-short.txt'
fhand = open(fname)
# Loop through the file
for line in fhand:
    # Skip the lines we aren't interested in
    if not line.startswith('From: '): continue
    # Split the line pieces into their chunks, email address is the second piece
    pieces = line.split()
    email = pieces[1]
    # Check to see if a row with this email address exists
    # Uses the '?' SQL wildcard and replaces it with the specified tuple
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    # Get one row at a time
    row = cur.fetchone()
    # If there is no row, create it. Otherwise update the row.
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    # Commit the changes
    conn.commit()

# Select the first 10 rows by count
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
# Print each row after converting to string
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the connection
cur.close()
