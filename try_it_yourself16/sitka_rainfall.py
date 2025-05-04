from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

path = Path('sitka_weather_2021_full.csv')
lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, rainfall = [], []

for row in reader: 
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(rain)

print(rainfall)

#Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color = 'blue', alpha = 0.5)

#Format plot
ax.set_title('Daily Rainfall, 2021\n Sitka, AK', fontsize = 24)
ax.set_xlabel('', fontsize = 20)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall (Inches)', fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()