import secrets

cookie_key = secrets.token_hex(16)
with open("cookie_key.txt", "w") as key_file:
    key_file.write(cookie_key)
print("Cookie key generated and saved to cookie_key.txt")
