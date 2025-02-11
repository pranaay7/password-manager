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

<video controls>
  <source src="https://private-user-images.githubusercontent.com/174170622/381173706-7f78341a-d004-4eae-b518-5eeb7b9f5aaa.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzkyNzgwNDAsIm5iZiI6MTczOTI3Nzc0MCwicGF0aCI6Ii8xNzQxNzA2MjIvMzgxMTczNzA2LTdmNzgzNDFhLWQwMDQtNGVhZS1iNTE4LTVlZWI3YjlmNWFhYS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxMVQxMjQyMjBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yNzcwOWI5MDNiMzM2OTY1MDMyZGQ0YmEzYTgwYTA1ZTcxY2EyM2EzNjJmMGE1YTdmNjBiOTQ0YzVkY2M4MTA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.sr9e9m3DbS7snk-BiKJNB1sSjtEChP7cY0laD3Hgzv8" type="video/mp4">
</video>


