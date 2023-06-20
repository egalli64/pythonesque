"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Rolling Dice with Plotly - Rolling Dice of Different Sizes
"""
import plotly.express as px
from e3a_die import Die

dice = (Die(), Die(10))

results = []
for roll_num in range(50_000):
    results.append(dice[0].roll() + dice[1].roll())

frequencies = []
values = range(2, dice[0].num_sides + dice[1].num_sides + 1)
for value in values:
    frequencies.append(results.count(value))

title = "Results of Rolling Two Dice 6/10 Values 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=values, y=frequencies, title=title, labels=labels)
# each column has its tick
fig.update_layout(xaxis_dtick=1)

fig.show()
# or, save it
# fig.write_html('sample.html')
