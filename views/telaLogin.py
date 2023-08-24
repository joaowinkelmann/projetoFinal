import tkinter as tk
from tkinter import messagebox
from models.dbConn import connect

class LoginWindow(tk.Toplevel):
    def __init__(self, parent, login_successful_callback):
        super().__init__(parent)
        self.title("Login")
        self.parent = parent
        # self.authentication_callback = authentication_callback
        self.login_successful_callback = login_successful_callback
        self.configure(background="#F0F0F0")

        self.username_label = tk.Label(self, text="Usuário:", bg="#F0F0F0")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.username_entry = tk.Entry(self, width=20)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self, text="Senha:", bg="#F0F0F0")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(self, show="*", width=20)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        login_button = tk.Button(self, text="Login", command=self.login, bg="#4CAF50", fg="white")
        login_button.grid(row=2, columnspan=2, padx=10, pady=5)

        self.bind("<Return>", lambda event: self.login())

    def auth(self, username, password):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE username LIKE %s AND password LIKE %s ", [username, password])
        return cur.fetchone()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        res = None

        if (username and password):
            res = self.auth(username, password)
            # print(type(res))
            # print(res[0])
        
        if (res != None):
            # return True
            self.login_successful_callback(res[0])  # Call the successful login callback
        else:
            messagebox.showerror("Error", "Invalid username or password.")
            # return False