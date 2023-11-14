# Fill list_x and list_y with string numbers divided by " " and a graph is plotted.

import matplotlib.pyplot as plt
import numpy as np

# Fill numbers by user input and split (not important)
numberx = input("Enter numbers of x separated by a space: ")
list_x = numberx.split()
numbery = input("Enter same amount numbers of y separated by a space: ")
list_y = numbery.split()

# Convert string numbers to int numbers
int_list_x = [int(x) for x in list_x]
int_list_y = [int(x) for x in list_y]

# Convert to array so matplotlib will work
graphx = np.array(int_list_x)
graphy = np.array(int_list_y)

# Plot graph
plt.plot(graphx, graphy)
plt.show()