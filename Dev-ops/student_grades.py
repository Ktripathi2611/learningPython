students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. Show All Grades")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
