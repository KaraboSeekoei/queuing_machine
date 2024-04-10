# mental_health_dep.py

import tkinter as tk

department_location = "Student Services Building, Room 202"

staff_members = [
    {"name": "Dr. Lisa Johnson", "email": "lisa.johnson@example.com"},
    {"name": "Dr. Michael Smith", "email": "michael.smith@example.com"},
    {"name": "Sarah Brown", "email": "sarah.brown@example.com"},
    {"name": "David Miller", "email": "david.miller@example.com"},
    {"name": "Dr. Emily Wilson", "email": "emily.wilson@example.com"}
]

department_mission = """
The mission of the Mental Health Department is to promote the psychological well-being and
mental health of our institution's community members. We offer counseling services, support 
programs, and resources to help individuals cope with challenges, reduce stress, and enhance 
their overall quality of life.
"""

def display_department_info():
    root = tk.Tk()
    root.title("Mental Health Department Information")
    info_label = tk.Label(root, text=f"Department Location: {department_location}\n\nStaff Members:")
    info_label.pack()
    for member in staff_members:
        member_label = tk.Label(root, text=f"- {member['name']} ({member['email']})")
        member_label.pack()
    mission_label = tk.Label(root, text=f"\nDepartment Mission:\n{department_mission}")
    mission_label.pack()

    def print_department_info():
        department_info = f"Department Location: {department_location}\n\nStaff Members:\n"
        for member in staff_members:
            department_info += f"- {member['name']} ({member['email']})\n"
        department_info += f"\nDepartment Mission:\n{department_mission}"
        print(department_info)

    print_button = tk.Button(root, text="Print Mental Health Department Info", command=print_department_info)
    print_button.pack(pady=10)

    root.mainloop()
