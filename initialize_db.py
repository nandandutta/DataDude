import sqlite3
import bcrypt

def hash_password(password):
    """Hash a password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def initialize_db():
    """Create necessary tables if they do not exist and add admin user."""
    conn = sqlite3.connect('datadude.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    # Add admin user if not already present
    admin_username = 'admin'
    admin_password = 'admin'  # Change this to a secure password

    # Check if the admin user already exists
    cursor.execute('SELECT 1 FROM users WHERE username = ?', (admin_username,))
    if cursor.fetchone() is None:
        hashed_password = hash_password(admin_password)
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (admin_username, hashed_password))
        print(f"Admin user '{admin_username}' added to the database.")
    else:
        print(f"Admin user '{admin_username}' already exists in the database.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
