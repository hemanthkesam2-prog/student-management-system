import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"Name: {student['name']} | "
            f"Roll No: {student['roll_no']} | "
            f"Course: {student['course']}"
        )


def search_student(students):
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student found!")
            print(student)
            return

    print("Student not found.")


def delete_student(students):
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if _name_ == "_main_":
    main()
