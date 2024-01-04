# This Python script is written by Vinay Reddy B

def divisible(numerator: int, denominator: int) -> bool:
    return numerator % denominator == 0

print(divisible(30, 4))

###In this case, the function divisible checks if 30 is divisible by 4, which it is (30 % 4 == 0), so it returns True