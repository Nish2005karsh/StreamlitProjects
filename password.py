# Password Manager using Streamlit and Fernet encryption

import json
import os
import streamlit as st
from getpass import getpass
from cryptography.fernet import Fernet
from streamlit_elements import elements, mui

# File to store passwords
PASSWORD_FILE = 'passwords.json'
KEY_FILE = 'key.key'

def generate_key():
    """
    Generate a new encryption key and save it to a file.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    """
    Load the encryption key from a file.
    """
    return open(KEY_FILE, 'rb').read()

def encrypt_password(password, key):
    """
    Encrypt a password using the provided key.

    Parameters:
    - password: The password to encrypt.
    - key: The encryption key.

    Returns:
    - The encrypted password.
    """
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password, key):
    """
    Decrypt a password using the provided key.

    Parameters:
    - encrypted_password: The encrypted password to decrypt.
    - key: The encryption key.

    Returns:
    - The decrypted password.
    """
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

def save_passwords(passwords):
    """
    Save the password data to a JSON file.

    Parameters:
    - passwords: A dictionary containing account-password pairs.
    """
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file)

def load_passwords():
    """
    Load the password data from a JSON file.

    Returns:
    - A dictionary containing account-password pairs.
    """
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            content = file.read().strip()
            if content:
                return json.loads(content)
            else:
                return {}  # Return an empty dictionary if file is empty
    else:
        return {}


def add_password(account, password, key):
    """
    Add a new account and password to the password manager.

    Parameters:
    - account: The account name (e.g., website or app name).
    - password: The password to store.
    - key: The encryption key.
    """
    passwords = load_passwords()
    encrypted_password = encrypt_password(password, key)
    passwords[account] = encrypted_password.decode()
    save_passwords(passwords)
    print(f"Password for {account} added successfully.")

def retrieve_password(account, key):
    """
    Retrieve the password for a specific account.

    Parameters:
    - account: The account name to retrieve the password for.
    - key: The encryption key.

    Returns:
    - The decrypted password, if found.
    """
    passwords = load_passwords()
    if account in passwords:
        encrypted_password = passwords[account].encode()
        return decrypt_password(encrypted_password, key)
    else:
        print(f"No password found for account: {account}")
        return None

def main():
    if not os.path.exists(KEY_FILE) or os.path.getsize(KEY_FILE) == 0:
        st.info("Encryption key not found or invalid. Generating a new key...")
        generate_key()

    key = load_key()

    try:
        # Validate key
        Fernet(key)
    except ValueError:
        st.warning("Invalid encryption key detected. Regenerating...")
        generate_key()
        key = load_key()

    st.title("Password Manager " + "🔒")
    

    st.subheader("Securely store and retrieve your passwords"+"🔐")
    choice = st.selectbox("Choose an option:", ["Add a new password", "Retrieve a password", "Quit"], key="unique_key_main_choice")

    if choice == "Add a new password":
        account = st.text_input("Enter the account name (e.g., website or app name): ", key="account_input")
        password = st.text_input("Enter the password: ", type="password", key="password_input")
        if st.button("Add Password"):
            add_password(account, password, key)
            st.success(f"Password for {account} added successfully.")

    elif choice == "Retrieve a password":
        account = st.text_input("Enter the account name:", key="retrieve_account_input")
        if st.button("Retrieve Password"):
            password = retrieve_password(account, key)
            if password:
                st.success(f"Password for {account}: {password}")
            else:
                st.error(f"No password found for account: {account}")

    elif choice == "Quit":
        st.warning("Exiting the Password Manager. Close the app.")
    st.divider()
    st.write("Developed by Nishkarsh Pandey")
    st.write( "GitHub: [Nishkarsh Pandey](https://github.com/Nish2005karsh)")
    with elements("multiple_childrens"):
        mui.Button(mui.icon.Facebook())
        mui.Button(mui.icon.Twitter())
        mui.Button(mui.icon.Instagram())
        mui.Button(mui.icon.LinkedIn())
        mui.Button(mui.icon.GitHub())


if __name__ == "__main__":
    main()
