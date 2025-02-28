# -Data-Structures-and-Strings-in-Python
# TASK1 DETAILS:-
This Python program allows the user to look up a student's marks from a predefined dictionary of student marks. Here's a detailed breakdown of the program:

Program Breakdown
Dictionary of Student Marks:


students_marks = {
    "Alice": 85,
    "Ram": 92,
    "Shyam": 78,
    "Pranshu": 88,
    "Tiwari": 95
}
A dictionary students_marks is created with student names as keys and their corresponding marks as values. In this case, the dictionary contains five student names and their marks.
The keys are the student names (e.g., "Alice", "Ram", etc.), and the values are their marks (e.g., 85, 92, etc.).
User Input for Student Name:


student_name = input("Enter the student's name: ")
The program prompts the user to input the name of the student whose marks they want to look up.
The input() function reads the name as a string and stores it in the variable student_name.
Checking if the Student Exists in the Dictionary:


Copy
if student_name in students_marks:
    print(f"{student_name}'s marks are: {students_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
The if statement checks whether the entered student name is a key in the students_marks dictionary.
If the student's name is found, the program prints the corresponding marks for that student. The marks are accessed using students_marks[student_name].
If the student's name is not found, the program prints a message saying the student is not found in the records.
The dictionary lookup student_name in students_marks checks if the provided name exists as a key in the dictionary.
Example Walkthrough
Case 1: Student Found in the Dictionary
Input: The user enters Alice.
The program checks if "Alice" exists in the dictionary students_marks.
Since "Alice" is a key in the dictionary with a corresponding value of 85, the program will output:

Alice's marks are: 85
Case 2: Student Not Found in the Dictionary
Input: The user enters John.
The program checks if "John" exists in the dictionary students_marks.
Since "John" is not a key in the dictionary, the program will output:

Student 'John' not found in the records.
Key Concepts Explained
Dictionary in Python:

A dictionary is a collection of key-value pairs. In this case, student names (keys) are associated with their marks (values). The dictionary provides an efficient way to store and retrieve data based on a unique key.
The in Operator:

The in operator is used to check if a particular value (in this case, a student's name) exists as a key in the dictionary. It returns True if the key is found and False otherwise.
Input and Output:

The input() function is used to capture user input, and the print() function is used to display the results based on that input.
Example Output
Example 1 (Student Found):
User Input: Alice

Enter the student's name: Alice
Alice's marks are: 85
Example 2 (Student Not Found):
User Input: John


Enter the student's name: John
Student 'John' not found in the records.
