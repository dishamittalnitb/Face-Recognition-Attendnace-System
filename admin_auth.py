import tkinter as tk
from tkinter import messagebox
import hashlib

# Admin credentials stored securely (hashed passwords)
admin_credentials = {
    "admin": hashlib.sha256("123".encode()).hexdigest(),  # Update password securely
}

# Function to verify admin login
def verify_admin(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return admin_credentials.get(username) == hashed_password

# Function to handle login attempt
def admin_login():
    username = username_entry.get()
    password = password_entry.get()

    if verify_admin(username, password):
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        root.destroy()  # Close login window
        import attendance
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials! Access Denied.")


# GUI for Admin Login
root = tk.Tk()
root.title("Admin Login")
root.geometry("400x250")

tk.Label(root, text="Admin Login", font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(root, text="Username:", font=("Arial", 12)).pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack()

tk.Label(root, text="Password:", font=("Arial", 12)).pack()
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=admin_login, bg="blue", fg="white", font=("Arial", 12))
login_button.pack(pady=10)

root.mainloop()
