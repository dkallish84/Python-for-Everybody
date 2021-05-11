# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
# Hint: The top organizational count is 536.
import sqlite3, re

conn = sqlite3.connect('orgdomains.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org VARCHAR(128), count INTEGER)')

fname = input('Enter a file name: ')
if (len(fname) < 1): fname = '/Users/dkallish/Documents/Coursera/Python for Everybody Specialization/mbox.txt'
fhand = open(fname)
for line in fhand:
    if not line.startswith('From: '): continue
    pieces = line.split()
    # Find the domain using RegEx
    pieces = re.findall('[a-zA-Z0-9]\S*@(\S*[a-zA-Z])', line)
    org = pieces[0]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
