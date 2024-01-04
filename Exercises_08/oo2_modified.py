# This Python script is written by Vinay Reddy B

class MyTemplate():
    # Define class object attributes, the same for any instance of the class
    class_object_attribute1 = 178927
    class_object_attribute2 = 161944

    # Constructor, called whenever an instance of the class is created
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

# Instantiate the class
my_object = MyTemplate("vinay", True)
# Check the object's class object attributes
print(my_object.class_object_attribute1, my_object.class_object_attribute2)
