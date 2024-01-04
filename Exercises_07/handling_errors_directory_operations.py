# This Python script is written by Vinay Reddy B

import os

def create_directory(directory_name: str) -> int:
    # Check if the directory already exists
    if os.path.isdir(directory_name):
        return 2  # Directory already exists
    else:
        try:
            os.mkdir(directory_name)
            return 0  # Directory created successfully
        except OSError as e:
            print(f"Error creating directory {directory_name}: {e}")
            return 1  # Error occurred while creating directory

if __name__ == '__main__':
    print("Trying to create directories")

    # Try to create directories with different statuses
    result1 = create_directory("NewDir")
    if result1 == 0:
        print("Creating 'NewDir' worked")
    elif result1 == 1:
        print("Couldn't create 'NewDir'")
    elif result1 == 2:
        print("'NewDir' already existed")

    result2 = create_directory("NewDir")
    if result2 == 0:
        print("Creating 'NewDir' worked")
    elif result2 == 1:
        print("Couldn't create 'NewDir'")
    elif result2 == 2:
        print("'NewDir' already existed")

    result3 = create_directory("ExistingDir")
    if result3 == 0:
        print("Creating 'ExistingDir' worked")
    elif result3 == 1:
        print("Couldn't create 'ExistingDir'")
    elif result3 == 2:
        print("'ExistingDir' already existed")

###The script then attempts to create different directories, handles the return values accordingly, and prints appropriate messages based on the outcome