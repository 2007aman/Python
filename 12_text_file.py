import os
import time

file_name = input("Enter the file name to create:- ")

def write_to_file(file_name):
    # Check if file exists
    if os.path.exists(file_name):
        print(f"Error: {file_name} already exists.")
        return # Exits the function early

    # Write to file section
    with open(file_name, "a") as F:
        while True:
            text = input("Enter any text to add in the file:- ")
            F.write(f"{text}\n")
            choice = input("Do you want to enter more, y/n: ").lower()
            if choice == "n":
                break # Breaks the while loop, but stays in the function

    # Reading/Checking section (Now correctly indented inside the function)
    print("Want to check what you have written?")
    time.sleep(2)
    print("------running-----")
    time.sleep(2)
    
    choose = input("Say yes or no? ").lower()
    if choose == "yes":
        with open(file_name, "r", encoding="utf-8") as k:
            r_ead = k.read()
            print(r_ead)
    else:
        print("We understand your hurry, thanks!")
        return # Exits the function

# To actually run the function, you must call it:
write_to_file(file_name)
