# This Python script is written by Vinay Reddy B

def most_expensive(price_list):
    """
    Iterate through a list and find the most expensive item
    """
    # Set up the variables
    max_price = 0
    max_price_item = ""
    max_availability = 0  # Added availability tracking
    # Iterate, unpacking the tuple
    for description, price, availability in price_list:
        # If this is the maximum price, record that in our variables
        if price > max_price:
            max_price = price
            max_price_item = description
            max_availability = availability  # Update max availability
        # If it is not the maximum price, do nothing
        else:
            pass
    # Return the maximum prices item, its price, and availability
    return max_price_item, max_price, max_availability

# Provide the data (including availability)
price_list = [("Pineapple", 1.0, 10), ("Apples", 0.5, 20), ("Pears", 0.7, 15), ("Peaches", 0.8, 8)]
# Call the function and unpack its return values
product, price, availability = most_expensive(price_list)
print(product, price, availability)

###The error happens when trying to unpack three values from a tuple that contains only two elements. To fix this error, ensure that the tuples in the price_list match the unpacking expectations in the function.