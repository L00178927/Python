# This Python script is written by Vinay Reddy B

# Function with an argument
def greet(name):
    """
    Simple greeting function
    """
    print(f"Hello, {name}!")

greet("Alice")  # Calling the function with an argument

# Function returning a value based on an argument
def calculate_circumference(radius):
    """
    Calculate the circumference of a circle based on its radius
    """
    return 2 * 3.142 * radius 

a = calculate_circumference(5)
print(a)

# Function with a default argument
def calculate_circumference_default(radius=1):
    """
    Calculate the circumference of a circle based on its radius
    """
    return 2 * 3.142 * radius 

a_default = calculate_circumference_default()
print(a_default)

# Function using input and conversion
def calculate_circumference_input():
    """
    Calculate the circumference of a circle based on user input for radius
    """
    r = input("Provide a radius value: ")
    r_float = float(r)
    return 2 * 3.142 * r_float

a_input = calculate_circumference_input()
print(a_input)

# Function handling unknown number of arguments
def auto_adder(*my_numbers):
    return sum(my_numbers)

print(auto_adder(12, 34, 23, 66, 8, 99))
