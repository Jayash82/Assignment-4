text_to_write = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append additional data to the same file
text_to_append = input("\nEnter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())