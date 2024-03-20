import customtkinter
import requests
import json
from tkinter import messagebox

from dashboard import dashboard_window
from constants import LOGIN_URL, SIGNUP_URL

# pylint: disable=no-member

login = customtkinter.CTk()
login.title("Log In")
login.geometry("1000x600")
customtkinter.set_appearance_mode("System")

frame = customtkinter.CTkFrame(master=login)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome Back!")
label.pack(pady=12, padx=10)

email_input = customtkinter.CTkEntry(master=frame, placeholder_text="email@example.com")
email_input.pack(pady=12, padx=10)

password_input = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_input.pack(pady=12, padx=10)

def login_form():
    email = email_input.get()
    password = password_input.get()
    
    if not email or not password:
        messagebox.showerror("Error", "Please enter an email address and password.")
        return

    url = LOGIN_URL
    
    data = {
        'email': email,
        'password': password,
    }
    try:
        json_data = json.dumps(data)
        
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(url, data=json_data, headers=headers)
        
        if response.status_code == 200:
            login.destroy()
            dashboard_window()
        elif response.status_code == 400:
            messagebox.showerror("Error", "Invalid login credentials!")
        else:
            messagebox.showerror("Error", "Log in request failed!")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to connect to the server.")


button = customtkinter.CTkButton(master=frame, text="Log in", command=login_form)
button.pack(pady=12, padx=10)

signup_link = customtkinter.CTkLabel(master=frame, text="Not yet registered? ", cursor="hand2")
signup_link.pack(pady=5, padx=10)
signup_link.configure(text_color="blue")


def signup_window():
    def signup_form():
        email = email_input.get()
        password = password_input.get()
        
        if not email or not password:
            messagebox.showerror("Error", "Please enter an email address and password.")
            return

        url = SIGNUP_URL
        
        data = {
            'email': email,
            'password': password,
        }
        try:
            json_data = json.dumps(data)
            
            headers = {'Content-Type': 'application/json'}
            
            response = requests.post(url, data=json_data, headers=headers)
            
            if response.status_code == 201:
                signup.destroy()
                dashboard_window()
            elif response.status_code == 400:
                messagebox.showerror("Error", "Sign up failed!")
            else:
                messagebox.showerror("Error", "Sign up request failed!")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Failed to connect to the server.")
            
    signup = customtkinter.CTk()
    signup.title("Sign Up")
    signup.geometry("1000x600")

    email_input = customtkinter.CTkEntry(master=signup, placeholder_text="email@example.com")
    email_input.pack(pady=12, padx=10)

    password_input = customtkinter.CTkEntry(master=signup, placeholder_text="Password", show="*")
    password_input.pack(pady=12, padx=10)

    signup_button = customtkinter.CTkButton(master=signup, text="Sign Up", command=signup_form)
    signup_button.pack(pady=5)

    signup.mainloop()


def open_signup_and_close_login(event):
    login.destroy()
    signup_window()
    

signup_link.bind("<Button-1>", open_signup_and_close_login)


login.mainloop()