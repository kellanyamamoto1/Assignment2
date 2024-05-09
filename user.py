# Kellan Yamamoto
# 28388886
# kellany@uci.edu

#add user commands

from pathlib import Path
import admin as admin
import ui as ui

command_list = """
L -- List all files in a specified path
Q -- Quit the program entirely
C -- Create a new file in a specified path
D -- Deleted a file
R -- Read a file
O -- Open a file
Help -- Relist commands
"""


def start():
    ui.adminis(0)
    ui.commands()