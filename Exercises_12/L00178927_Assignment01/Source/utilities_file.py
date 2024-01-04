# This Python script is written by Vinay Reddy B

import os
import platform

# Define global variables
current_working_directory = None

def detect_os() -> str:
    # Detect the OS in use
    return platform.system()

def detect_working_directory() -> str:
    # Returns the directory this script was run from
    return os.getcwd()

def list_directory_contents(path='.'):
    # List directory contents based on the OS
    if detect_os().lower() == "windows":
        os.system(f"dir {path}")
    elif detect_os().lower() == "linux":
        os.system(f"ls {path}")
    else:
        print("Cannot list directory contents for this OS.")

if __name__ == '__main__':
    print("This module executes as a standalone script")

    # Check the OS in use
    my_os = detect_os().lower()

    # Parse the response, only check for Windows and Linux
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        exit()

    # Get the current working directory
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")

    # List directory contents
    list_directory_contents()
else:
    print(f"This module is called {__name__} and is being called by another script")

###When executed as a standalone script, it checks the operating system, prints information about it, fetches the current working directory, and then lists the contents of the directory

