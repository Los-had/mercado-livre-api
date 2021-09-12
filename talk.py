import sqlite3
from sqlite3 import Error
from datetime import datetime

try:
    conn = sqlite3.connect('talk.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS talk (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        post TEXT NOT NULL,
        date TEXT NOT NULL
    );
    ''')
except Error as e:
    print(f'error: {e}')

def add_comment_to_db(name, content):
    actual_date = datetime.now().strftime('%Y-%m-%d')
    c.execute('''
    INSERT INTO talk (name, post, date)
    VALUES (?, ?, ?)
    ''', (name, content, actual_date))
    conn.commit()
    conn.close()

def get_all_posts():
    c.execute('''
    SELECT * FROM talk
    ''')
    posts = c.fetchall()

    return posts