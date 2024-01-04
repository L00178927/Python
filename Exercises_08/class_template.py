# This Python script is written by Vinay Reddy B

class MyTemplate:

    # Define class object attributes
    class_object_attribute1 = None
    class_object_attribute2 = None 

    # Constructor
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        self.attr1 = attribute1
        self.attr2 = attribute2

    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")

    def my_method2(self, my_name: str = "Guest"):
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")

# Usage example
if __name__ == "__main__":
    # Create an instance of MyTemplate
    my_object = MyTemplate("Vinay", True)
    
    # Access class object attributes
    print(my_object.class_object_attribute1, my_object.class_object_attribute2)
    
    # Call methods
    my_object.my_method1()
    my_object.my_method2("Slartibartfast")
