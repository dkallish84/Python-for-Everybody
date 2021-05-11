# This application will read an iTunes export file in XML and produce a properly normalized database

# Import the required libraries
import xml.etree.ElementTree as xmlET
import sqlite3

# Create a connection and cursor object
# Creates the database file if it doesn't exist yet
conn = sqlite3.connect('tracks_db.sqlite')
cur = conn.cursor()

# Drop the existing tables and create fresh using 'executescript()'
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Prompt the user for their library filename
fname = input('Enter your track library filename: ')
# Use a default if the user doesn't enter a value
if (len(fname) < 1): fname = 'Library.xml'

# Data in the iTunes export Library.xml is presented as follows:
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
# Function to look up the track data we're interested in from the XML
def track_lookup(d, key):
    found = False
    # Loop through the dictionary looking for the relevent 'key' text
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# Parse the xml data, use findall to search the data in the third level 'dict'
data = xmlET.parse(fname)
track_info = data.findall('dict/dict/dict')
print('Dict count:', len(track_info))
# Loop through the track_info, using the function to get the information to store in the database
for entry in track_info:
    # Skip when Track ID is empty
    if (track_lookup(entry, 'Track ID') is None): continue

    # Get the data using the track_lookup() method
    name = track_lookup(entry, 'Name')
    artist = track_lookup(entry, 'Artist')
    album = track_lookup(entry, 'Album')
    genre = track_lookup(entry, 'Genre')
    len = track_lookup(entry, 'Total Time')
    count = track_lookup(entry, 'Play Count')
    rating = track_lookup(entry, 'Rating')

    # Skip when required values are empty
    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, genre, len, count, rating)

    # Insert or update tables from the related tables heading into Track
    cur.execute(''' INSERT OR IGNORE INTO Artist (name)
        VALUES (?) ''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Genre (name)
        VALUES (?) ''', (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, genre_id, len, rating, count ) )

    # Commit the changes on each iteration
    conn.commit()
