# This Python script is written by Vinay Reddy B

from datetime import datetime as dt

# The current time
current_time = dt.now()

#Using the strftime() method to format the datetime object into the desired string representations

# Human-readable values for time
current_hour = current_time.strftime("%H")  # Hour in 24-hour format
current_minute = current_time.strftime("%M")  # Minutes
current_second = current_time.strftime("%S")  # Seconds

# Human-readable values for date
current_year = current_time.strftime("%Y")  # Year
current_month = current_time.strftime("%B")  # Full month name
current_day = current_time.strftime("%d")  # Day of the month

# Printing human-readable time and date
print("Current Time:")
print(f"Hour: {current_hour}")
print(f"Minute: {current_minute}")
print(f"Second: {current_second}")

print("\nCurrent Date:")
print(f"Year: {current_year}")
print(f"Month: {current_month}")
print(f"Day: {current_day}")
