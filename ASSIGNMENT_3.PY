
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

sample_number = int(input("Enter a number to calculate its factorial: "))

print(f"The factorial of {sample_number} is {factorial(sample_number)}.")



import math

number = float(input("Enter a number: "))

sqrt_result = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)

# Step 3: Display the results
print(f"\nResults for the number {number}:")
print(f"Square Root: {sqrt_result}")
print(f"Natural Logarithm (log base e): {log_result}")
print(f"Sine (in radians): {sine_result}")
