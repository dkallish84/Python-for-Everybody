# A simple database dumper to take a look at what is in our spider.sqlite file:

# DO NOT RUN THIS PROGRAM!

import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Twitter')
count = 0
for row in cur: print(row)
    count = count + 1
print(count, 'rows.')
cur.close()
