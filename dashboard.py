import customtkinter

#pylint: disable=no-member

def dashboard_window():
    dashboard = customtkinter.CTk()
    dashboard.title("Dashboard")
    dashboard.geometry("1000x600")
    customtkinter.set_appearance_mode("Dark")
    
    frame = customtkinter.CTkFrame(master=dashboard)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="You are viewing the dashboard")
    label.pack(pady=12, padx=10)
    
    dashboard.mainloop()