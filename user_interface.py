import tkinter as tk
from Departments import performance_team, mental_health_d
#  git testing
def framework_start():
    root = tk.Tk()
    root.title("Queuing Machine Dispenser")
    root.geometry("600x400")
    current_ticket_label = tk.Label(root)
    current_ticket_label.pack()
    choosing_option(root, current_ticket_label)
    root.mainloop()

def handle_button_click(option, label):
    # Clear the label text
    label.config(text="")
    
    if option == "Performance Team":
        performance_team.display_team_info()
    elif option == "Mental Health Dep":
        mental_health_d.display_department_info()
    # Add handling for other departments here

def choosing_option(root, label):
    options = ["Performance Team", "Mentors", "Financial Dep", "Mental Health Dep"]
    label.config(text="Select a department")
    label.pack()
    for option in options:
        btn = tk.Button(root, text=option, command=lambda opt=option: handle_button_click(opt, label))
        btn.pack(pady=5)

framework_start()
