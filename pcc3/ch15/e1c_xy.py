"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Plotting a Simple Line Graph
"""
import matplotlib.pyplot as plt

# instead of relying on indices, give explicit x-y match
xs = [1, 2, 3, 4, 5]
ys = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(xs, ys, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()
