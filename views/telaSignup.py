import tkinter as tk
from tkinter import messagebox
from models.dbConn import connect

class SignupWindow(tk.Toplevel):
    def __init__(self, parent, signup_successful_callback):
        super().__init__(parent)
        self.title("Sign up")
        self.parent = parent
        # self.authentication_callback = authentication_callback
        self.signup_successful_callback = signup_successful_callback
        self.configure(background="#F0F0F0")

        self.username_label = tk.Label(self, text="Usuário:", bg="#F0F0F0")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.username_entry = tk.Entry(self, width=20)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self, text="Senha:", bg="#F0F0F0")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(self, show="*", width=20)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.confirm_password_label = tk.Label(self, text="Confirmar:", bg="#F0F0F0")
        self.confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.confirm_password_entry = tk.Entry(self, show="*", width=20)
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

        login_button = tk.Button(self, text="Sign up", command=self.signup, bg="#b55e24", fg="white")
        login_button.grid(row=3, columnspan=2, padx=10, pady=5)

        self.bind("<Return>", lambda event: self.login())

    def add_user(self, username, password):
        try:
            conn = connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            return cur.lastrowid
        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", e)
            return None

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        res = None

        if (username and (password == confirm_password)):
            res = self.add_user(username, password)
            # print(type(res))
            # print(res[0])
        
        if (res != None):
            # return True
            self.signup_successful_callback(res)  # Call the successful login callback
        else:
            messagebox.showerror("Error", "Invalid credentials")
            # return False