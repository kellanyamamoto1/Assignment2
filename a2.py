# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import ui as ui
import Profile as Profile
import admin as admin
import user as user
from pathlib import Path

# PATH: C:\Users\kella\OneDrive\Desktop\ICS32Again\Assignment2



if __name__ == "__main__":
    if ui.user() == 1:
        admin.start()
    else:
        #print list of commands
        user.start()    
