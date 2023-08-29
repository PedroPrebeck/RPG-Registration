import sqlite3
import hashlib

def connect_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            username TEXT PRIMARY KEY,
            strength INTEGER NOT NULL,
            intelligence INTEGER NOT NULL,
            skin_color TEXT NOT NULL,
            hair TEXT NOT NULL
        )
    ''')
    return conn, cursor

def create_user(username, password):
    conn, cursor = connect_db()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return True
    else:
        return False

def login_user(username, password):
    conn, cursor = connect_db()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    data = cursor.fetchone()
    return data

def create_character(username, strength, intelligence, skin_color, hair):
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM characters WHERE username = ?', (username,))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO characters (username, strength, intelligence, skin_color, hair) VALUES (?, ?, ?, ?, ?)', (username, strength, intelligence, skin_color, hair))
        conn.commit()
        return True
    else:
        return False

def get_characters(username):
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM characters WHERE username = ?', (username,))
    characters = cursor.fetchall()
    return characters
