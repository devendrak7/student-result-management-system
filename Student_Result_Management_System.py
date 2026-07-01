
# ******** By Devendra Kumawat ******
import os
import json


def student_save():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)


def load_students():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []


students = []
load_students()   


def management():
    print("="*70)
    print("\t-----Welcome to the Student Result Management System-----")
    print("="*70)
    print("""
            __________________________
            | 1. Add Student         |
            | 2. View All Students   |
            | 3. Search Student      |
            | 4. Delete Student      |
            | 5. Update Student      |
            | 6. Exit                |
            |________________________|
        """)

    choice = int(input("Enter your choice number (1-6): "))
    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == 1:
        add_student()
    elif choice == 2:
        view_all_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        update_student()
    elif choice == 6:
        exit_system()
    else:
        print("Invalid Choice")


def title(tname):
    print("="*70)
    print("\t\t\t", tname)
    print("="*70)


def add_student():
    title("Add Student Details")

    while True:
        try:
            student = {
                "student_name": input("Enter student name: ").title(),
                "student_roll_no": int(input("Enter student roll number: ")),
                "student_branch": input("Enter student branch: ").upper(),
                "student_dsa": int(input("Enter DSA marks: ")),
                "student_cpp": int(input("Enter C++ marks: ")),
                "student_java": int(input("Enter Java marks: ")),
                "student_python": int(input("Enter Python marks: ")),
            }

            
            new_roll = student["student_roll_no"]

            duplicate = False

            for current_student in students:

                if new_roll == current_student["student_roll_no"] :
                    print("Roll Number already exists")
                    print("Please enter a different Roll Number.....")
                    duplicate = True
                    break

            if duplicate:
                continue
            
            if (
                student["student_dsa"] < 0 or student["student_dsa"] > 100 or
                student["student_cpp"] < 0 or student["student_cpp"] > 100 or
                student["student_java"] < 0 or student["student_java"] > 100 or
                student["student_python"] < 0 or student["student_python"] > 100
            ):
                print("Invalid Marks Retry (0-100 only)")
                continue
            break  
        except ValueError:
            print("Invalid input. Please enter correct details.")

    students.append(student)
    student_save()   
    print("Student record saved successfully.")
    print("Enter for contionu")


def view_all_students():
    title("View All Students")

    if not students:
        print("No students found. Please add students first.")
        return

    i = 0
    for student in students:
        i += 1
        print(f"\nStudent {i}")
        print(f"Name        : {student['student_name']}")
        print(f"Roll No     : {student['student_roll_no']}")
        print(f"Branch      : {student['student_branch']}")
        print(f"DSA Marks   : {student['student_dsa']}")
        print(f"C++ Marks   : {student['student_cpp']}")
        print(f"Java Marks  : {student['student_java']}")
        print(f"Python Marks: {student['student_python']}")
         
        total,percentage,result,back = student_result_calculate(student)
        print(f"Total Marks {total}/400")
        print(f"Student Percentage : {percentage:.2f}%")
        print(f"Student Grade : {student_grade(percentage)}")
        print(f"Student Result : {result}")
        if back:
            print(f"Student Back Subject : {', '.join(back)}")
        else:
            print("Student Back Subject : No Back Subjects")



def search_student():
    title("Search Student")

    find_student = input("Enter Student Name: ")
    find_roll_no = int(input("Enter Roll No: "))
    find = False

    for student in students:
        if (
            find_student.lower() == student["student_name"].lower()
            and find_roll_no == student["student_roll_no"]
        ):

            print(f"\nStudent Name      : {student['student_name']}")
            print(f"Student Roll No   : {student['student_roll_no']}")
            print(f"Student Branch    : {student['student_branch']}")
            print(f"DSA Marks         : {student['student_dsa']}")
            print(f"C++ Marks         : {student['student_cpp']}")
            print(f"Java Marks        : {student['student_java']}")
            print(f"Python Marks      : {student['student_python']}")

            total, percentage, result, back = student_result_calculate(student)

            print(f"Total Marks       : {total}/400")
            print(f"Percentage        : {percentage:.2f}%")
            print(f"Grade             : {student_grade(percentage)}")
            print(f"Result            : {result}")

            if back:
                print(f"Back Subjects     : {', '.join(back)}")
            else:
                print("Back Subjects     : No Back Subjects")

            find = True
            break

    if not find:
        print("\nStudent not found.")
        print("Please enter the correct Name and Roll Number.")


def delete_student():
    title("Delete Student")
    name = input("Enter student name: ")

    for student in students:
        if student["student_name"].lower() == name.lower():
            students.remove(student)
            student_save()   
            print("Student deleted successfully.")
            return

    print("Student not found.")


def update_student():
    title("Update Student")
    name = input("Enter student name: ")

    for student in students:
        if student["student_name"].lower() == name.lower():

            print("""
            1. Name
            2. Roll No
            3. Branch
            4. DSA Marks
            5. C++ Marks
            6. Java Marks
            7. Python Marks
            """)

            choice = int(input("Enter choice: "))

            try:
                if choice == 1:
                    student["student_name"] = input("Enter new name: ").title()

                elif choice == 2:
                    new_roll = int(input("Enter new roll no: "))
                    duplicate = False

                    for current_student in students:
                        if (
                            new_roll == current_student["student_roll_no"]
                            and current_student != student
                        ):
                            print("Roll Number already exists")
                            duplicate = True
                            break

                    if duplicate:
                        return

                    student["student_roll_no"] = new_roll

                elif choice == 3:
                    student["student_branch"] = input("Enter new branch: ").upper()

                elif choice == 4:
                    marks = int(input("Enter new DSA marks: "))
                    if 0 <= marks <= 100:
                        student["student_dsa"] = marks
                    else:
                        print("Invalid Marks (0-100 only)")
                        return

                elif choice == 5:
                    marks = int(input("Enter new C++ marks: "))
                    if 0 <= marks <= 100:
                        student["student_cpp"] = marks
                    else:
                        print("Invalid Marks (0-100 only)")
                        return

                elif choice == 6:
                    marks = int(input("Enter new Java marks: "))
                    if 0 <= marks <= 100:
                        student["student_java"] = marks
                    else:
                        print("Invalid Marks (0-100 only)")
                        return

                elif choice == 7:
                    marks = int(input("Enter new Python marks: "))
                    if 0 <= marks <= 100:
                        student["student_python"] = marks
                    else:
                        print("Invalid Marks (0-100 only)")
                        return

                else:
                    print("Invalid Choice")
                    return

                student_save()
                print("Student updated successfully.")
                return

            except ValueError:
                print("Invalid input.")
                return

    print("Student not found.") 

def student_grade(percentage):
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    return grade
def student_result_calculate(student):
    total = (
        student["student_dsa"] +
        student["student_cpp"] +
        student["student_java"] +
        student["student_python"]
    )

    percentage = total / 4
    passing_marks = 40

    back = []

    if student["student_dsa"] < passing_marks:
        back.append("DSA")

    if student["student_cpp"] < passing_marks:
        back.append("C++")

    if student["student_java"] < passing_marks:
        back.append("Java")

    if student["student_python"] < passing_marks:
        back.append("Python")

    if back:
        result = "Fail"
    else:
        result = "Pass"

    return total, percentage, result, back

def exit_system():
    print("Exiting system...")
    global st
    st = False


st = True
while st:
    management()