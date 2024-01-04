# This Python script is written by Vinay Reddy B

##This function checks for the presence of an even number in a list of numbers

def has_even_number(numbers: list) -> bool:
    for num in numbers:
        if num % 2 == 0:
            return True
    return False

##For the lambda function to calculate the volume of a cylinder, you can use

cylinder_volume = lambda radius, height: 3.14159 * radius ** 2 * height

###This lambda function takes in the radius and height of the cylinder and computes its volume using the formula: π * radius^2 * height