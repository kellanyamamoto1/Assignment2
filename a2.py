# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import ui as ui
import Profile as Profile

# PATH: C:\Users\kella\OneDrive\Desktop\ICS32Again\Assignment2

def main():
    while True:

        user_input = input().split()
        command = user_input[0]
        directory = user_input[1] if len(user_input) > 1 else None
        options = user_input[2] if len(user_input) > 2 else None
        name = user_input[3] if len(user_input) > 3 else None
        if command == 'Q':
            print("Quitting the program.")
            break
        elif command == 'R':
            if directory:
                ui.read_file(directory)
            else:
                print("ERROR")
        elif command == 'C':
            if len(user_input) < 4:
                print('ERROR')
            else:
                ui.create_file(directory, options, name)
        elif command == 'D':
            if directory:
                ui.delete_file(directory)
        elif command == 'O':
            if directory:
                ui.open_file(directory)
            else:
                print("ERROR")
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
