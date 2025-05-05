from pathlib import Path
import json

import plotly.express as px

#Read data as a string and convert it to a Python object
#path = Path('eq_data/eq_data_1_day_m1.geojson')
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding = 'utf-8')
all_eq_data = json.loads(contents)

#Homework Title
meta_header = all_eq_data['metadata']['title']

#Create a more readable version of the data file
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_contents)

#Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']
print (len(all_eq_dicts))

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    #mag = eq_dict['properties']['mag']
    #lon = eq_dict['geometry']['coordinates'][0]
    #lat = eq_dict['geometry']['coordinates'][1]
    #eq_title = eq_dict['properties']['title']
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

print(mags[:10], lons[:5], lats[:5])

fig = px.scatter_geo(lat = lats, lon = lons, size = mags, title = all_eq_data['metadata']['title'],
                     color = mags,
                     color_continuous_scale = 'Viridis',
                     labels = {'color': 'Magnitude'},
                     projection = 'natural earth',
                     hover_name = eq_titles,
                     )
fig.show()
#print(px.colors.named_colorscales())