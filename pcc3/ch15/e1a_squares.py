"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Plotting a Simple Line Graph

python -m pip install -U pip
python -m pip install -U matplotlib
"""
import matplotlib.pyplot as plt

# values on y, indices are the xs
ys = [0, 1, 4, 9, 16, 25]

# generate a figure with a single plot
fig, ax = plt.subplots()
# uses ys to generate the line on the ax plot
ax.plot(ys)
# open the plot viewer
plt.show()
