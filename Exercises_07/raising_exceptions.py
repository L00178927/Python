# This Python script is written by Vinay Reddy B

def validate_positive_integer():
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input <= 0:
            raise ValueError("Value must be greater than 0")
        else:
            print("Validation checks passed")
    except ValueError as err:
        print(f"Error: {err}")

validate_positive_integer()
