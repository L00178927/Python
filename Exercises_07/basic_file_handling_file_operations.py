# This Python script is written by Vinay Reddy B

###Running this script will showcase how different errors are handled when performing file read and write operations in different modes

my_filename = "datafile.txt"

try:
    # Writing to a file in "w" mode
    with open(my_filename, "w") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.write("Test line for writing")

    # Reading from the file in "r" mode
    with open(my_filename, "r") as file_handle:
        print(f"Reading from {my_filename}")
        content = file_handle.read()
        print("File content:", content)

except IOError as err:
    print(f"IOError occurred: {err}")
except OSError as err:
    print(f"OS Error occurred: {err}")
except Exception as err:
    print(f"General Error occurred: {err}")
else:
    print("File operations successful")
finally:
    print("Finishing up!")