"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Plotting a Simple Line Graph - Changing the Label Type and Line Thickness
"""
import matplotlib.pyplot as plt

ys = [0, 1, 4, 9, 16, 25]

fig, ax = plt.subplots()
# set the line thickness
ax.plot(ys, linewidth=3)

# improved readability
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# tick label size
ax.tick_params(labelsize=14)

plt.show()
