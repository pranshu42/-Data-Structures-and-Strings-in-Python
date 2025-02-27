students_marks = {
    "Alice": 85,
    "Ram": 92,
    "Shyam": 78,
    "Pranshu": 88,
    "Tiwari": 95
}

student_name = input("Enter the student's name: ")

if student_name in students_marks:
    print(f"{student_name}'s marks are: {students_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
