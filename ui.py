# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import pathlib
from Profile import Profile

def open_file(file_path):
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