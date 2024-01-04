# This Python script is written by Vinay Reddy B

print("Prepared by Vinay Reddy B")

#Here I have used string operations code as example as I have commented every step in this code of what I done

# Reversing String
Name = str(input("Provide string that need to be reversed and click on Enter button"))
print(Name[::-1])
#length of string
print("length of the string",(len(Name)))
#letters in a string which are in even count position
print("letters in a string which are in even count position by considering 0th Position as well>>", (Name[::2]))
#letters in a string which are in odd count position
print("letters in a string which are in odd count position by considering 0th Position as well>>", (Name[1::2]))
#Adding Text and variable
print("Good morning! " + Name)
#inserting variables and string
a = 2
b = 3
print("Hello {}, Hope you are doing well! Would you like to have {} apples or {} bread slices".format(Name, a, b))
#inserting variables and strings at the position we need
print("His Name is {fullname}, {first} has asked {fullname} to have some food . He would like to have {bread} slices of bread".format(fullname=Name, first="Vinay", bread=b))
#upper and lower case
print(f"Upper: ", Name.upper())
print(f"Lower: ", Name.lower())
print(f"Original: {Name}")
#text without space - strip with in the string does not work
spacetext = "   hey there!         "
print("Name without spaces", spacetext.strip())
