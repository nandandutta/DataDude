import bcrypt
import sqlite3

def hash_password(password):
    """Hash a password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def initialize_db():
    """Create necessary tables if they do not exist."""
    conn = sqlite3.connect('datadude.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def store_password(username, password):
    """Store a hashed password in the SQLite database."""
    hashed_password = hash_password(password)
    initialize_db()  # Ensure the table is created
    conn = sqlite3.connect('datadude.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def verify_password(username, password):
    """Verify a stored password against one provided by the user."""
    conn = sqlite3.connect('datadude.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    stored_password = cursor.fetchone()
    conn.close()

    if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0].encode('utf-8')):
        return True
    return False

def user_exists(username):
    """Check if a username already exists in the database."""
    conn = sqlite3.connect('datadude.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE username = ?', (username,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
