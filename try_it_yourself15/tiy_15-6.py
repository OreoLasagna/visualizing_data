from die import Die
import plotly.express as px

#Create one D6 dice and one D8 dice
d8_1 = Die(8)
d8_2 = Die(8)

#Make some rolls and store results in a list
results = []

for roll_num in range(5000):
    result = d8_1.roll() + d8_2.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = d8_1.num_sides + d8_2.num_sides
poss_results = range(2, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
title = "Results of Rolling two D8 dice 5,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

#Fruther customize chart
fig.update_layout(xaxis_dtick = 1)

fig.show()