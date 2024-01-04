# This Python script is written by Vinay Reddy B

print("Prepared by Vinay Reddy B")

#Example 1 of operations on integers

iterable_variable = [1,2,3,4,5,6]
total = 0

for item in iterable_variable:
    # For each item, execute this code block
    print(item)
 
#Example to print odd numbers in a given list of numbers 
for item in iterable_variable:
    if item %2 != 0:
        print(item)

#Example to print total sum of numbers
for item in iterable_variable:
    total = total + item
print(total)


#Example 2 of operations  on strings

# Define a string to iterate over
for this_letter in "Vinay Reddy":
    # Specify which letter to test for
    if this_letter == "R":
        # Found the test letter
        print(f"Woo hoo, found a {this_letter}!")
        # Exit the current loop
        break
    else:
        # Didn't find the test letter
        print(f"Aww man, I didn't want a {this_letter}!")


#Example 3 of operations on list

my_list = ["hey","Hi","hello","bye"]

for my_word in my_list:
    if my_word == "hey":
        pass
    if my_word == "Hi":
        continue
    if my_word == "hello":
        print(f"Found the number {my_word}")
    if my_word == "bye":
        break
        
#Example 4 of operations on tuples

list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
    print(item)
    
# Tuple unpacking
for a,b in list_of_tuples:
    print(a)  
    print(b)

#getting range
for index in range(0, 100, 5):
    print(index)

#Exercise in Loops tutorial

#create a dictionary
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}

#Iterate through scan
for ipv4 in scan:
    port = scan[ipv4]
    print(f"IP Address: {ipv4}, Port: {port}")
"""When iterating through the dictionary keys, we can access the corresponding values, but not directly iterating through key-value pairs"""

#Iterating through scan.items() instead of scan
for ipv4, port in scan.items():
    print(f"IP Address: {ipv4}, Port: {port}")
"""When we iterate through scan.items(), we directly get access to both the IP address and the port number in each iteration"""







