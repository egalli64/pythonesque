"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Plotting a Simple Line Graph - More customizations
"""
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()

xs = range(1, 1001)
ys = [x ** 2 for x in xs]

# chosing a color
# by name
# ax.scatter(xs, ys, color='red', s=10)
# by RGB percentage
# ax.scatter(xs, ys, color=(0, 0.8, 0), s=10)
# by colormap - varying by ys
ax.scatter(xs, ys, c=ys, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Square of Value", fontsize=10)
ax.tick_params(labelsize=10)
ax.axis([-10, 1100, -20_000, 1_100_000])

# do not use scientific notation
ax.ticklabel_format(style='plain')

plt.show()
# show or save
# plt.savefig('squares_plot.png', bbox_inches='tight')
