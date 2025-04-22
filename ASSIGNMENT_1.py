#Task 1: Perform Basic Mathematical Operations
#Problem Statement: Write a Python program that does the following:

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero is not allowed)"

print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print("\n")

#Task 2: Create a Personalized Greeting
#Problem Statement: Write a Python program that:


first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print(f" YOU ARE {full_name} THE FAMOUS WARLOCK AND EXORCIST")
