"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Plotting a Simple Line Graph - Calculating Data Automatically
"""
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()

# many points representing a x^2 curve
xs = range(1, 1001)
ys = [x ** 2 for x in xs]
ax.scatter(xs, ys, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)

# set the x and y range
ax.axis([-10, 1100, -20_000, 1_100_000])

plt.show()
