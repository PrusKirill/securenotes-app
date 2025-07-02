import sqlite3

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    content TEXT
)
''')

cursor.execute("INSERT INTO notes (content) VALUES (?)",
               ('<script>alert("XSS HACKED!")</script>',))

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password_hash TEXT
)
''')

cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
               ('admin', '5f4dcc3b5aa765d61d8327deb882cf99'))  # password: password

conn.commit()
conn.close()