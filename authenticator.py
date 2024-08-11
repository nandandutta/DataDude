import bcrypt
from database import Database
import streamlit as st
from auth_logic import verify_password

class Authenticator:
    def hash_password(self, password):
        """Hash a password."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def store_password(self, username, password):
        """Store a hashed password in the SQLite database."""
        hashed_password = self.hash_password(password)
        db = Database()
        db.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
        db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        db.close()

    def verify_password(self, username, password):
        """Verify a stored password against one provided by the user."""
        db = Database()
        db.execute('SELECT password FROM users WHERE username = ?', (username,))
        stored_password = db.fetchone()
        db.close()

        if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0].encode('utf-8')):
            return True
        return False

    def login(self, title, location):
        st.sidebar.title(title)
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if verify_password(username, password):
                return username, True, username
            else:
                return None, False, None
        return None, None, None