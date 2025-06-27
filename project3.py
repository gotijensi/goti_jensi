# Student Data Organizer

display_menu():


print("\n====== Student Data Organizer ======")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Info")
    print("4. Delete Student")
    print("5. Display All Subjects")
    print("6. Exit")

# Global student list

student records = []

add_student():
    student_id = input("Enter Student ID: ")
    dob = input("Enter Date of Birth (DD-MM-YYYY): ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    subjects_input = input("Enter subjects (comma-separated): ")
    subjects = set(subjects_input.split(","))
    subjects = {s.strip().title() for s in subjects}  # Clean formatting

 student_data = {
        "id_dob": (student_id, dob),  # Tuple: immutable
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects

student_records.append(student_data)
    print(f"Student {name} added successfully.")

#display_students():
    if not student_records:
        print("No student records found.")
        return
    for student in student_records:
        print("\n--- Student Info ---")
        print("ID:", student["id_dob"][0])
        print("DOB:", student["id_dob"][1])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print("Subjects:", ", ".join(student["subjects"]))

 update_student():
    sid = input("Enter Student ID to update: ")
    for student in student_records:
        if student["id_dob"][0] == sid:
            print(f"Found: {student['name']}")
            print("1. Update Name\n2. Update Age\n3. Update Grade\n4. Update Subjects")
            choice = input("Select what to update: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")
            elif choice == "2":
                student["age"] = int(input("Enter new age: "))
            elif choice == "3":
                student["grade"] = input("Enter new grade: ")
            elif choice == "4":
                subjects_input = input("Enter new subjects (comma-separated): ")
                student["subjects"] = {s.strip().title() for s in subjects_input.split(",")}
            print("Student info updated.")
            return
    print("Student not found.")

 delete_student():
    sid = input("Enter Student ID to delete: ")
    for i, student in enumerate(student_records):
        if student["id_dob"][0] == sid:
            del student_records[i]  # Using del keyword
            print("Student deleted.")
            return
    print("Student ID not found.")

 display_all_subjects():
    all_subjects = set()
    for student in student_records:
        all_subjects.update(student["subjects"])
    if all_subjects:
        print("All Subjects Offered:", ", ".join(sorted(all_subjects)))
    else:
        print("No subjects found.")

# Main program loop
while True:
    display_menu()
    option = input("Choose an option (1-6): ")
    if option == "1":
        add_student()
    elif option == "2":
        display_students()
    elif option == "3":
        update_student()
    elif option == "4":
        delete_student()
    elif option == "5":
        display_all_subjects()
    elif option == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


