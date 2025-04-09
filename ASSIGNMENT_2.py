                       
                         #  ASSIGNMENT 2:
 
# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:

n = int(input("Enter an integer: "))


if n% 2 == 0:
    print(f"The number {n} is even.")
else:
    print(f"The number {n} is odd.")


# Task 2:Sum of Integers from 1 to 50 Using a Loop
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

total_sum = 0
for i in range(1, 51):
    total_sum += i

print(f"The sum of integers from 1 to 50 is {total_sum}.")
