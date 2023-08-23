import tkinter as tk
from views.telaSplash import SplashScreen
from views.telaDashboard import Dashboard

def launch_main_app():
    splash_screen.destroy()
    app = Dashboard()
    app.mainloop()

if __name__ == "__main__":
    splash_screen = SplashScreen(launch_main_app)
    splash_screen.mainloop()