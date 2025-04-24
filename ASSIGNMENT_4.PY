try:
    with open("sample.txt", "r") as file:
        print("Contents of sample.txt:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.\n")



# Task 2: Write and Append Data to a File

# Step 1: Take user input and write to the file
user_input = input("Enter text to the file : ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("Data successfully written to output.txt\n")

# Step 2: Append additional data to the same file
additional_input = input("Enter more text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
print("Data successfully appended \n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

