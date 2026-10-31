import csv

# Student Result Analyzer

subjects = ["English", "Maths", "Science"]
students = []


def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if any(mark < 35 for mark in marks):
        grade = "F"
        status = "FAIL"
    elif average >= 90:
        grade = "A+"
        status = "PASS"
    elif average >= 80:
        grade = "A"
        status = "PASS"
    elif average >= 70:
        grade = "B"
        status = "PASS"
    elif average >= 60:
        grade = "C"
        status = "PASS"
    elif average >= 50:
        grade = "D"
        status = "PASS"
    else:
        grade = "E"
        status = "PASS"

    return total, average, grade, status


def get_mark(subject):
    while True:
        try:
            mark = int(input(f"Enter {subject} marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student():
    print("\n--- Enter Student Details ---")

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    marks = []
    for subject in subjects:
        marks.append(get_mark(subject))

    total, average, grade, status = calculate_result(marks)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade,
        "status": status
    }

    students.append(student)

    print("\nStudent result added successfully!")


def display_results():
    if not students:
        print("\nNo student records available.")
        return

    print("\n========== STUDENT RESULTS ==========")

    for student in students:
        print("\nName:", student["name"])
        print("Roll Number:", student["roll"])

        for i, subject in enumerate(subjects):
            print(subject + ":", student["marks"][i])

        print("Total:", student["total"], "/ 300")
        print("Average:", round(student["average"], 2), "%")
        print("Grade:", student["grade"])
        print("Status:", student["status"])
        print("-------------------------------------")


def save_results():
    if not students:
        print("\nNo records to save.")
        return

    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Name", "Roll Number",
            "English", "Maths", "Science",
            "Total", "Average", "Grade", "Status"
        ])

        for student in students:
            writer.writerow([
                student["name"],
                student["roll"],
                *student["marks"],
                student["total"],
                round(student["average"], 2),
                student["grade"],
                student["status"]
            ])

    print("\nResults saved successfully in results.csv!")
def search_student():
    roll = input("\nEnter roll number to search: ")

    found = False

    for student in students:
        if student["roll"] == roll:
            print("\n--- Student Found ---")
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])
            print("Total:", student["total"], "/ 300")
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            print("Status:", student["status"])
            found = True
            break

    if not found:
        print("\nStudent not found!")

# Main program

while True:
    print("\n================================")
    print("     STUDENT RESULT ANALYZER")
    print("================================")
    print("1. Add Student")
    print("2. Display Results")
    print("3. Save Results")
    print("4. Search Student")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_results()
    elif choice == "3":
        save_results()
    elif choice == "4":
        search_student()
    elif choice == "5":
        print("\nThank you for using Student Result Analyzer!")
        break
    else:
        print("\nInvalid choice. Please try again.")