# This Python script is written by Vinay Reddy B

class MyTemplate():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

# Instantiate the class with required arguments
my_object = MyTemplate("Vinay", True)
# Check the object and type
print(type(my_object))
