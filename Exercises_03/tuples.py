# This Python script is written by Vinay Reddy B

print("Prepared by Vinay Reddy B")

#Defining list and tuple
my_list=[1,2,"list"]
my_tuple=(1,2,1,"tuple",1)

print(type(my_list))
print(type(my_tuple))

#How many times does '1' repeat in my_tuple
print(my_tuple.count(1))

#At what position can we find the first '1' in my_tuple
print(my_tuple.index(1))

#Exercise
my_tupletolist = list(my_tuple)
my_tupletolist[2]="value changed"
my_tuple=tuple(my_tupletolist)
print(my_tuple)

