# This Python script is written by Vinay Reddy B

def calculate_endurance(fuel, fuel_consumption):
    try:
        # Convert inputs to float
        fuel = float(fuel)
        fuel_consumption = float(fuel_consumption)

        # Check if fuel_consumption is zero (idling scenario)
        if fuel_consumption == 0:
            raise ValueError("Fuel consumption cannot be zero (idling scenario)")

        # Calculate endurance
        endurance = fuel / fuel_consumption
        return endurance

    except ValueError as err:
        print(f"Value Error: {err}")
        return None  # Return None to signify an error

    except ZeroDivisionError as err:
        print(f"Zero Division Error: {err}")
        return None  # Return None to signify an error

# Test the function
fuel_input = input("Enter fuel in litres: ")
fuel_consumption_input = input("Enter fuel consumption in litres per minute: ")

endurance = calculate_endurance(fuel_input, fuel_consumption_input)
if endurance is not None:
    print(f"Remaining endurance in minutes: {endurance}")
else:
    print("Error calculating endurance")

###During the function's execution, if any errors occur, such as a ValueError (for invalid inputs) or a ZeroDivisionError (for divide-by-zero), appropriate error messages are printed, and the function returns None to signify an error
