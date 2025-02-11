SecurePas - A Simple Password Manager




Please note :-


Do not forget your master password, as it is required to decrypt stored credentials.

Always back up vault.json, master.key, and salt.key if you need to migrate data.

If any key is lost, encrypted passwords cannot be recovered.




File Structure

password_manager.py      # Main application file
master.key               # Encrypted master password file
vault.json               # Encrypted password storage file
salt.key                 # Salt file for key derivation
security.log             # Log file for tracking security events



Usage


Run the Application:
python password_manager.py

Set Up Master Password:
When running for the first time, you will be prompted to create a master password.
This password will be used for encrypting and decrypting stored passwords.

Store Passwords:
Click on Add Password to save a new login.

Retrieve Passwords:
Select an entry and click View Password to retrieve login details.

Generate Secure Passwords:
Use Generate Password to create a strong password and copy it to the clipboard.

Delete Passwords:
Click Delete Password to remove stored credentials.




Features :-



Secure Password Storage: Encrypts passwords using AES encryption with a master password.

Master Password Protection: Protects stored passwords with a user-defined master password.

Search Functionality: Easily find stored credentials using a search bar.

Clipboard Support: Copies retrieved passwords to the clipboard for convenience.

Password Generation: Generates strong passwords with adjustable length.

Logging and Security: Maintains a security log for tracking activity.

User-Friendly UI: Built using Tkinter for an intuitive graphical interface.





Installation

Make sure you have Python installed. Then, install the required dependencies:
pip install -r requirements.txt




License

This project is open-source under the MIT License.