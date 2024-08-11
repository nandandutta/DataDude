from authenticator import Authenticator
from auth_logic import verify_password


def main():
    auth = Authenticator()

    # Simulate storing a password
    auth.store_password('example_user', 'example_password')

    # Simulate verifying a password
    is_verified = auth.verify_password('example_user', 'example_password')
    if is_verified:
        print("Password verified successfully!")
    else:
        print("Failed to verify password.")

if __name__ == "__main__":
    main()
