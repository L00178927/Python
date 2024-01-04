# This Python script is written by Vinay Reddy B

###This code defines a function find_num that iterates through a list to check if a specified number is present

def find_num(number_list: list, number: int) -> bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass

result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(result)

###The function checks if the number 9 is present in the list [1, 2, 3, 4, 5, 6, 7, 8]. However, it iterates through the list but doesn't find the number 9. When the function completes its loop without finding the number, it doesn't explicitly return anything (using return None by default). Hence, the result printed is None

###To modify the function to return False instead of None if the value is not found, you can adjust it like this

def find_num(number_list: list, number: int) -> bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
    return False

result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(result)