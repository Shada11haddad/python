from cryptography.fernet import Fernet
import hashlib

def write_key():
    key = Fernet.generate_key()
    with open("Key.Key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("Key.Key", "rb") as file:
        key = file.read()
    return key

master_pwd = input("What is the master password? ")

# Derive a Fernet key using the master password
base_key = load_key()
hashed_pwd = hashlib.sha256(master_pwd.encode()).digest()  # Hash the master password
final_key = base_key[:16] + hashed_pwd[:16]  # Ensure a 32-byte key
fer = Fernet(final_key)

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_passw = data.split("|")
                decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                print("User:", user, ", Password:", decrypted_passw)
    except FileNotFoundError:
        print("No password file found. Please add a password first.")
    except Exception as e:
        print("Error occurred:", e)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('password.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add) or q to quit: ").lower()
    if mode == "q":
        quit()
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
