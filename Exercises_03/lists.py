# This Python script is written by Vinay Reddy B

print("Prepared by Vinay Reddy B")

#Here are some exmaples and operations on Lists data structure

#Defining variables
mylist1 = ["a","b","c","d",1,2,3]
mylist2 = [8,"water","fish",9,10]
mystring = "15/10/2023, 11:29, System server, Windows machine"

#list operations

a = len(mylist1)
print("length of mylist1 is ", a)

slice_1 = mylist1[1:3:1]
print(slice_1)

my_character = mylist1[-1]
print(my_character)

concatenated_list1 = mylist1 + mylist2
print(concatenated_list1)

concatenated_list2 = [mylist1, mylist2]
print(concatenated_list2)

print(mylist2)
mylist2[2]="shark"
print(mylist2)

print(mylist1)
mylist1.append(4)
print(mylist1)

print(mystring)
list_of_values = mystring.split(",")
print(list_of_values)

print(mylist1)
mylist1.reverse()
print(mylist1)

print(mylist2)
del mylist2[:]
print(mylist2)

