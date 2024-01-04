# This Python script is written by Vinay Reddy B

print("Prepared by Vinay Reddy B")

#Create a initial dictionary
my_dictionary = {"fname":"vinay", "sname":"Bhimireddy", "occupation":"student"}
print(my_dictionary)
print(type(my_dictionary))

#Adding a key and value for existing dictionary
my_dictionary["salary"] = "No Income!"
print(my_dictionary)

#Edit one of the key and value in the existing dictionary
my_dictionary["occupation"] = "IT Employee"
print(my_dictionary)

#Exercise
mykeys = my_dictionary.keys()
print(mykeys)

myvalues = my_dictionary.values()
print(myvalues)

myitems = my_dictionary.items()
print(myitems)

