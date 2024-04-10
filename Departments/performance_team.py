# performance_team.py

import tkinter as tk

team_location = "3rd Floor, Performance Department"

team_members = [
    {"name": "Corban", "email": "corban@wethinkcode.co.za"},

]

team_mission = """
Our mission is to enhance the performance and productivity of our organization through strategic planning, 
data analysis, and performance optimization strategies. We strive to foster a culture of excellence 
and continuous improvement, empowering every member of the team to reach their full potential.
"""

def display_team_info():
    root = tk.Tk()
    root.title("Performance Team Information")
    info_label = tk.Label(root, text=f"Team Location: {team_location}\n\nTeam Members:")
    info_label.pack()
    for member in team_members:
        member_label = tk.Label(root, text=f"- {member['name']} ({member['email']})")
        member_label.pack()
    mission_label = tk.Label(root, text=f"\nTeam Mission:\n{team_mission}")
    mission_label.pack()

    def print_team_info():
        team_info = f"Team Location: {team_location}\n\nTeam Members:\n"
        for member in team_members:
            team_info += f"- {member['name']} ({member['email']})\n"
        team_info += f"\nTeam Mission:\n{team_mission}"
        print(team_info)

    print_button = tk.Button(root, text="Print Performance Team Info", command=print_team_info)
    print_button.pack(pady=10)

    root.mainloop()
