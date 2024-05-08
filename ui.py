# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import pathlib
from Profile import Profile
import ui as ui
import admin as admin
administrator = False
temp_path = ''

def command_list():
    pass

def commands():
    while True:
        
        user_input = input("input command: ").split()
        command = user_input[0:1]
        directory = user_input[1] if len(user_input) > 1 else None
        options = user_input[2] if len(user_input) > 2 else None
        name = user_input[3] if len(user_input) > 3 else None
        if command == "admin":
            admin.start()
        else:
            if command == 'Q':
                print("Quitting the program.")
                break
            elif command == 'R':
                if directory:
                    read_file(directory)
                else:
                    print("ERROR")
            elif command == 'C':
                if len(user_input) < 4:
                    print('ERROR')
                else:
                    create_file(directory, options, name)
            elif command == 'D':
                if directory:
                    delete_file(directory)
            elif command == 'O':
                if directory:
                    open_file(directory)
                else:
                    print("ERROR")
            elif command == 'E':
                edit_file(directory)
            else:
                print("Invalid command")


def user():
    user_type = input("admin or user?: ")
    temp = 0
    if user_type == "admin":
        temp = 1
    else:
        temp = 0
    return temp

def adminis(num):
    global administrator
    if num == 1:
        administrator = True
    else:
        administrator = False
    return administrator

def open_file(file_path):
    pass

def edit_file(file_path):
    pass

def create_file(directory, options, name):
    file = name + ".dsu"
    filepath = pathlib.Path(directory) / file
    if options == '-n':
        
        username = input("Enter username: ")
        password = input("Enter password: ")
        bio = input("Enter bio: ")
        
        profile = Profile(username = username, password = password, bio = bio)
        
        with open(filepath, 'w') as f:
            print('')
        f = open(filepath, 'w')
        profile.save_profile(path = filepath)
        print(f"Profile for {username} created and saved to {filepath}")
    else:
        print("ERROR")


def delete_file(file_path):
    suffix = ".dsu"
    if file_path.endswith(suffix):
        path = pathlib.Path(file_path)
        if path.exists():
            path.unlink()
            print(f"{file_path} DELETED")
        else:
            print(f"File '{file_path}' not found")
    else:
        print("File in directory not found")


def read_file(file_path):
    if file_path.endswith('.dsu'):
        path = pathlib.Path(file_path)
        if path.exists() and path.is_file():
            with open(path, 'r') as file:
                content = file.read()[:-1]
                if not content:
                    print("EMPTY")
                else:
                    print(content)
        else:
            print(f"File '{file_path}' not found")
    else:
        print("ERROR")