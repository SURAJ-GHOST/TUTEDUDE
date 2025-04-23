student_marks = { "Alice": 85,
                  "Bob": 92,
                  "Charlie": 78,
                  "Diana": 89,
                  "Ethan": 95
                }

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student named {student_name} not found in the records.")


    # Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
first_five = numbers[:5]
reversed_first_five = first_five[::-1]
print("Extracted list:", first_five)
print("Reversed list:", reversed_first_five)