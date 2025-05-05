from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

import plotly.express as px

#Read data as a string and convert it to a Python object
#path = Path('eq_data/eq_data_1_day_m1.geojson')
path = Path('fire_data/world_fires_1_day.csv')
lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

lat = 0
lon = 0
bright = 0

for index, column_header in enumerate(header_row):
    print(index, column_header)

    if column_header == 'latitude':
        lat = index

    elif column_header == 'longitude':
        lon = index

    elif column_header == 'brightness':
        bright = index

lats, lons, brights = [], [], []
for row in reader: 
    
    try:
        latitude = float(row[lat])
        longitude = float(row[lon])
        brightness = float(row[bright])
    except ValueError:
        print(f"Missing data for row {row}")
    else:
        lats.append(latitude)
        lons.append(longitude)
        brights.append(brightness)

fig = px.scatter_geo(lat = lats, lon = lons, size = brights, title = 'World Fires',
                     color = brights,
                     color_continuous_scale = 'agsunset',
                     labels = {'color': 'Brightness'},
                     projection = 'natural earth',
                     )
fig.show()
