# This Python script is written by Vinay Reddy B

# A function to add 10 to a number
def add_ten(n):
    return n + 10

# Create a list of numbers for testing
my_numbers = [1, 2, 3, 4, 5]

# Using map() with a defined function
result_function = map(add_ten, my_numbers)
print("Using function:", list(result_function))  # Convert map object to a list

# Using map() with a lambda function
result_lambda = map(lambda x: x + 10, my_numbers)
print("Using lambda:", list(result_lambda))  # Convert map object to a list
