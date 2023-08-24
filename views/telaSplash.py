import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from views.telaLogin import LoginWindow
from views.telaSignup import SignupWindow

class SplashScreen(tk.Tk):
    def __init__(self, launch_main_app_callback):
        super().__init__()
        self.title("Home / Splash Screen")

        self.launch_main_app = launch_main_app_callback

        ttk.Label(self, text="Welcome to the Application!").pack(pady=20)

        login_button = ttk.Button(self, text="Log In", command=self.open_login_window)
        login_button.pack(pady=10)

        signup_button = ttk.Button(self, text="Create New Account", command=self.open_signup_window)
        signup_button.pack(pady=10)

    def open_login_window(self):
        # Open the LoginWindow
        login_window = LoginWindow(self, self.login_successful_callback)

    def login_successful_callback(self, user_id):
        # Your authentication logic here
        # If successful, call self.launch_main_app()
        # mandar o user_id de volta para o main_app
        self.launch_main_app()

    def open_signup_window(self):
        # Handle new account creation
        signup_window = SignupWindow(self, self.signup_successful_callback)
        # pass

    def signup_successful_callback(self, user_id):
        print(user_id + " aaaa")

if __name__ == "__main__":
    app = SplashScreen()
    app.mainloop()
