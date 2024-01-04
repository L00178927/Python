# This Python script is written by Vinay Reddy B

print("Prepared by Vinay Reddy B")

#First case scenario

print("Here is the scenario where a,b,c are true")

a = True
b = True
c = True

if a:
    print("a was true")
elif b:
    print("b was true")
elif c:
    print("c was true")
else:
    print("None of our boolean variables were true")
    
#Second scenario where a is false and b,c are true
print("Here is the scenario where a is false and b,c are true")

a = False
b = True
c = True

if a:
    print("a was true")
elif b:
    print("b was true")
elif c:
    print("c was true")
else:
    print("None of our boolean variables were true")
    
#Third scenario where a,b are false and c is true

print("Here is the scenario where a,b are false and c is true")

a = False
b = False
c = True

if a:
    print("a was true")
elif b:
    print("b was true")
elif c:
    print("c was true")
else:
    print("None of our boolean variables were true")

#Fourth scenario where a,b,c are false

print("Here is the scenario where a,b,c are false")

a = False
b = False
c = False

if a:
    print("a was true")
elif b:
    print("b was true")
elif c:
    print("c was true")
else:
    print("None of our boolean variables were true")


#One more example with boolean conditions

print("firsr case where one of the statement is wrong")
if (10<8) and (4<8):
    print("Yup!")
else:
    print("Nope!")
    
print("second case where both the statements are true")
if (10>8) and (5<9):
    print("Yup!")
else:
    print("Nope!")


