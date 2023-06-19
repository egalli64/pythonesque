"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Plotting the Random Walk
"""
import matplotlib.pyplot as plt
from e2a_walk import RandomWalk

# Make a random walk
rw = RandomWalk(50_000)

# Plot the points in the walk
plt.style.use('classic')

fig, ax = plt.subplots()
sz = range(rw.num_points)

# darken the point color when proceeding in plotting
ax.scatter(rw.xs, rw.ys, c=sz, cmap=plt.cm.Blues, edgecolors='none', s=1)
ax.set_aspect('equal')

# from green to red
ax.scatter(0, 0, c='green', s=30)
ax.scatter(rw.xs[-1], rw.ys[-1], c='red', s=30)

# no axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
