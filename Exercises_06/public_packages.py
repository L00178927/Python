# This Python script is written by Vinay Reddy B

###Open command prompt in windows machine and run the command 'pip install matplot lib' which is used for the execution of this current script

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting the data
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()

###This script uses the matplotlib package to create a simple plot of x versus y values