import sqlite3

def connect_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    return conn, cursor

def create_user(username, password):
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()

def login_user(username, password):
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    data = cursor.fetchone()
    return data

def create_character(username, strength, intelligence, skin_color, hair):
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO characters (username, strength, intelligence, skin_color, hair) VALUES (?, ?, ?, ?, ?)', (username, strength, intelligence, skin_color, hair))
    conn.commit()

def get_characters(username):
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM characters WHERE username = ?', (username,))
    characters = cursor.fetchall()
    return characters
