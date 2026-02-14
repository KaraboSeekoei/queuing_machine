# Queue as a list
admin_queue = []

# Function to add a student
def add_student(student_id, first_name, surname, reason):
    student = {
        "id": student_id,
        "first_name": first_name,
        "surname": surname,
        "reason": reason
    }
    admin_queue.append(student)
    print(f"{first_name} {surname} added to the admin queue for : {reason}.")

# Function to serve the next student
def serve_student():
    if admin_queue:
        student = admin_queue.pop(0)
        print(f"Serving {student['first_name']} {student['surname']} for {student['reason']}.")
    else:
        print("No students waiting.")

# Function to view the queue
def view_queue():
    if admin_queue:
        print("Students waiting:")
        for i, student in enumerate(admin_queue, start=1):
            print(f"{i}. {student['first_name']} {student['surname']} (ID: {student['id']}) - {student['reason']}")
    else:
        print("Queue is empty.")

# --- Interactive prompt loop ---
while True:
    print("\nCommands: add | serve | view | exit")
    command = input("Enter command: ").strip().lower()

    if command == "add":
        student_id = int(input("Enter student ID: "))
        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        reason = input("Enter reason for admin help: ")
        add_student(student_id, first_name, surname, reason)

    elif command == "serve":
        serve_student()

    elif command == "view":
        view_queue()

    elif command == "exit":
        print("Exiting queue system.")
        break

    else:
        print("Invalid command. Try again.")
