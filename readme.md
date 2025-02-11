# SecurePass - Password Manager

## Overview
SecurePass is a secure and efficient password manager built using Python and Tkinter. It allows users to store, retrieve, generate, and manage passwords securely. The application encrypts stored passwords using the `cryptography` library to ensure security.

## Features
- **Secure Password Storage**: Encrypts passwords using AES encryption with a master password.
- **Master Password Protection**: Protects stored passwords with a user-defined master password.
- **Search Functionality**: Easily find stored credentials using a search bar.
- **Clipboard Support**: Copies retrieved passwords to the clipboard for convenience.
- **Password Generation**: Generates strong passwords with adjustable length.
- **Logging and Security**: Maintains a security log for tracking activity.
- **User-Friendly UI**: Built using Tkinter for an intuitive graphical interface.

## Installation
### Prerequisites
Ensure you have Python installed on your system. Then, install the required dependencies:
```sh
pip install cryptography pyperclip
```

## Usage
1. **Run the Application**:
   ```sh
   python password_manager.py
   ```
2. **Set Up Master Password**:
   - When running for the first time, you will be prompted to create a master password.
   - This password will be used for encrypting and decrypting stored passwords.
3. **Store Passwords**:
   - Click on `Add Password` to save a new login.
4. **Retrieve Passwords**:
   - Select an entry and click `View Password` to retrieve login details.
5. **Generate Secure Passwords**:
   - Use `Generate Password` to create a strong password and copy it to the clipboard.
6. **Delete Passwords**:
   - Click `Delete Password` to remove stored credentials.

## Security Mechanism
- **Encryption**: Uses AES encryption (via `cryptography.fernet.Fernet`) with a derived key from the master password using PBKDF2.
- **Salted Hashing**: A randomly generated salt is used for key derivation to enhance security.
- **Secure Storage**:
  - Passwords are stored in an encrypted format inside `vault.json`.
  - The master key is stored securely in `master.key`.
  - Salt is saved in `salt.key` to ensure secure key derivation.

## File Structure
```
password_manager.py      # Main application file
master.key               # Encrypted master password file
vault.json               # Encrypted password storage file
salt.key                 # Salt file for key derivation
security.log             # Log file for tracking security events
```

## Notes
- Do not forget your master password, as it is required to decrypt stored credentials.
- Always back up `vault.json`, `master.key`, and `salt.key` if you need to migrate data.

## License
This project is released under the MIT License.


https://private-user-images.githubusercontent.com/79321758/411977807-fdb985cb-e671-4cc2-b099-27b5078c904d.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzkyNzg5OTYsIm5iZiI6MTczOTI3ODY5NiwicGF0aCI6Ii83OTMyMTc1OC80MTE5Nzc4MDctZmRiOTg1Y2ItZTY3MS00Y2MyLWIwOTktMjdiNTA3OGM5MDRkLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjExVDEyNTgxNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWEzYjM2ZThlMWZiY2IzZjM4ZWZiMDFmMDc5NWZkMmRjMTRhNjE2YzI3MDExNjViZGY5NDQ1NWYzYWQ3MWFmNTEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0._zKvhATUBYWDqn4Jfks2h84w2zLMVOea0S5UzhkcZ74


