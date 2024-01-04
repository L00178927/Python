# This Python script is written by Vinay Reddy B

class MyClass():
    def __init__(self, my_value):
        print("Running constructor for MyClass")
        self.value = my_value

    def my_method(self):
        print(f"Value in MyClass: {self.value}")

# Create an instance of MyClass called MyClass1
my_class1 = MyClass(10)
my_class1.my_method()

# Create another instance of MyClass called MyClass2
my_class2 = MyClass(20)
my_class2.my_method()
