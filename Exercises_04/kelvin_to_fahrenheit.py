# This Python script is written by Vinay Reddy B

# Creating a list of 10 values in Kelvin
kelvin_temperatures = [300, 305, 310, 315, 320, 325, 330, 335, 340, 345]

# Converting Kelvin to Celsius and Fahrenheit using list comprehensions
celsius_temperatures = [temp - 273.15 for temp in kelvin_temperatures]
fahrenheit_temperatures = [(temp * 9/5) - 459.67 for temp in kelvin_temperatures]

# Printing the Kelvin, Celsius, and Fahrenheit temperatures
print("Kelvin:", kelvin_temperatures)
print("Celsius:", celsius_temperatures)
print("Fahrenheit:", fahrenheit_temperatures)
