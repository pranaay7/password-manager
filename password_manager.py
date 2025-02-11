import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import json
import pyperclip
import secrets
import logging
from datetime import datetime, timedelta

class PasswordManager:
    def __init__(self):
        self.KEY_FILE = "master.key"
        self.DATA_FILE = "vault.json"
        self.SALT_FILE = "salt.key"
        self.LOG_FILE = "security.log"
        self.setup_logging()
        
        if not os.path.exists(self.SALT_FILE):
            self.salt = os.urandom(16)
            with open(self.SALT_FILE, "wb") as salt_file:
                salt_file.write(self.salt)
        else:
            with open(self.SALT_FILE, "rb") as salt_file:
                self.salt = salt_file.read()

        if not os.path.exists(self.KEY_FILE):
            while True:
                password = simpledialog.askstring(
                    "Master Password", 
                    "Create your master password:",
                    show='*'
                )
                if password:
                    self.master_password = password
                    self.setup_encryption()
                    self.save_master_password(password)
                    break
                else:
                    messagebox.showerror("Invalid Password", "Please enter a password.")
        else:
            while True:
                password = simpledialog.askstring("Master Password", "Enter master password:", show='*')
                self.master_password = password
                self.setup_encryption()
                if self.verify_master_password(password):
                    break
                messagebox.showerror("Error", "Incorrect master password!")

        self.load_passwords()
        self.setup_ui()

    def setup_logging(self):
        logging.basicConfig(
            filename=self.LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def setup_encryption(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_password.encode()))
        self.cipher = Fernet(key)

    def save_master_password(self, password):
        hashed = self.cipher.encrypt(password.encode()).decode()
        with open(self.KEY_FILE, "w") as key_file:
            key_file.write(hashed)

    def verify_master_password(self, password):
        try:
            with open(self.KEY_FILE, "r") as key_file:
                stored_hash = key_file.read()
            decrypted = self.cipher.decrypt(stored_hash.encode()).decode()
            return password == decrypted
        except:
            return False

    def load_passwords(self):
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, "r") as file:
                    self.passwords = json.load(file)
            except:
                self.passwords = {}
        else:
            self.passwords = {}

    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("SecurePass")
        self.root.geometry("600x700")
        self.root.configure(bg="#1e1e1e")
        self.setup_styles()
        self.create_widgets()
        self.update_listbox()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Custom.TEntry",
            fieldbackground="#2d2d2d",
            foreground="white",
            insertcolor="white"
        )

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="SecurePass",
            font=("Arial", 34, "bold"),
            fg="#61afef",
            bg="#1e1e1e"
        )
        title_label.pack(pady=20)

        search_frame = tk.Frame(self.root, bg="#1e1e1e")
        search_frame.pack(fill=tk.X, padx=20, pady=10)

        search_label = tk.Label(
            search_frame,
            text="Search",
            font=("Arial", 12),
            fg="#787276",
            bg="#1e1e1e"
        )
        search_label.pack(anchor="w", pady=(0, 5))

        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self.filter_passwords)
        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            style="Custom.TEntry",
            font=("Arial", 12)
        )
        search_entry.pack(fill=tk.X)

        list_frame = tk.Frame(self.root, bg="#1e1e1e")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.listbox = tk.Listbox(
            list_frame,
            bg="#2d2d2d",
            fg="white",
            font=("Arial", 12),
            selectmode=tk.SINGLE
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        button_configs = [
            ("Add Password", self.add_password),
            ("View Password", self.view_password),
            ("Delete Password", self.delete_password),
            ("Generate Password", self.generate_and_copy_password)
        ]

        for text, command in button_configs:
            btn = tk.Button(
                self.root,
                text=text,
                command=command,
                font=("Arial", 14),
                bg="#282c34",
                fg="black",
                activebackground="#61afef",
                activeforeground="white",
                width=15
            )
            btn.pack(pady=5)

    def filter_passwords(self, *args):
        search_term = self.search_var.get().lower()
        self.update_listbox(search_term)

    def update_listbox(self, search_term=""):
        self.listbox.delete(0, tk.END)
        sorted_entries = sorted(self.passwords.items(), key=lambda x: x[0].lower())
        
        for website, data in sorted_entries:
            if search_term.lower() in website.lower() or search_term.lower() in data["username"].lower():
                self.listbox.insert(tk.END, f"{website} - {data['username']}")

    def add_password(self):
        website = simpledialog.askstring("Website", "Enter website name:")
        if not website:
            return

        username = simpledialog.askstring("Username", "Enter username:")
        if not username:
            return

        password = simpledialog.askstring("Password", "Enter password:")
        if not password:
            return

        self.passwords[website] = {
            "username": username,
            "password": self.cipher.encrypt(password.encode()).decode()
        }
        
        self.save_passwords()
        self.update_listbox()
        messagebox.showinfo("Success", "Password saved successfully!")

    def view_password(self):
        selected = self.listbox.get(tk.ACTIVE)
        if not selected:
            messagebox.showwarning("Warning", "Please select an entry first!")
            return

        website = selected.split(" - ")[0]
        data = self.passwords.get(website)
        if data:
            decrypted_password = self.cipher.decrypt(data["password"].encode()).decode()
            pyperclip.copy(decrypted_password)
            
            details = (
                f"Website: {website}\n"
                f"Username: {data['username']}\n"
                f"Password: {decrypted_password}\n\n"
                f"Password has been copied to clipboard!"
            )
            
            messagebox.showinfo("Password Details", details)
        else:
            messagebox.showerror("Error", "No password found!")

    def delete_password(self):
        selected = self.listbox.get(tk.ACTIVE)
        if not selected:
            messagebox.showwarning("Warning", "Please select an entry first!")
            return

        website = selected.split(" - ")[0]
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the entry for {website}?"):
            if website in self.passwords:
                del self.passwords[website]
                self.save_passwords()
                self.update_listbox()
                messagebox.showinfo("Success", "Password deleted successfully!")

    def generate_and_copy_password(self):
        length = simpledialog.askinteger("Password Length", "Enter desired password length:", initialvalue=16)
        if length:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            password = ''.join(secrets.choice(chars) for _ in range(length))
            pyperclip.copy(password)
            messagebox.showinfo("Generated Password", 
                              f"New password generated and copied to clipboard!\n\nLength: {length} characters")

    def save_passwords(self):
        with open(self.DATA_FILE, "w") as file:
            json.dump(self.passwords, file, indent=4)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordManager()
    app.run()