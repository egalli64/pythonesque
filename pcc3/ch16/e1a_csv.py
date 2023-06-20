"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 16 - Downloading Data - The CSV File Format
"""
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import csv

# run the script from the current folder
# see github.com/ehmatthes/pcc_3e chapter_16/the_csv_file_format/weather_data
path = Path('sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

# the CSV header
header_row = next(reader)
print(header_row)

# enumerating the column names in the header
# for index, column_header in enumerate(header_row):
#    print(index, column_header)

# Extract dates (2) and high temperatures (4)
dates, highs = [], []
for row in reader:
    dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
    highs.append(int(row[4]))

# Plot them
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=8)

plt.show()
