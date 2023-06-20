"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Rolling Dice with Plotly

python -m pip install -U pip
python -m pip install -U plotly
python -m pip install -U pandas
"""
import plotly.express as px

from e3a_die import Die

die = Die()
results = []
for roll_num in range(1_000):
    results.append(die.roll())

frequencies = []
values = range(1, die.num_sides+1)
for value in values:
    frequencies.append(results.count(value))

title = "Results of Rolling One Die 6 Values 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=values, y=frequencies, title=title, labels=labels)
fig.show()
