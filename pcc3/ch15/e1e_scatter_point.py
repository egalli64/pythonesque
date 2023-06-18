"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Plotting a Simple Line Graph - Plotting and Styling Individual Points with scatter()
"""
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
# a single point with a specified size
ax.scatter(2, 4, s=200)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()
