from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

path = Path('sitka_weather_2021_simple.csv')
lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

TMAX = 0
TMIN = 0

#Homework for TIY 16-4
for index, column_header in enumerate(header_row):
    print(index, column_header)

    if column_header == 'TMAX':
        TMAX = index
        print(TMAX)

    if column_header == 'TMIN':
        TMIN = index
        print(TMIN)

#Extract dates and high temperatures
dates, highs, lows = [], [], []

for row in reader: #This is heady but because of the line above, line 8, we have already read the very first line in the file
                    #So the for loop starts on the second line technically. The first line of real data
    #current_date = datetime.strptime(row[2], '%Y-%m-%d')
    #high = int(row[4]) Index for simple csv file
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[TMAX])
    low = int(row[TMIN])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

print(highs)

#Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

#Format plot
ax.set_title('Daily High and Low Temperatures, 2021\n Sitka, AK', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)

#HOMEWORK. This is how you manually set the values of your y-axis. Identical to the death valley chart so we can compare/contrast now
plt.ylim(10, 140)

plt.show()