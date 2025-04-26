from die import Die
import plotly.express as px

#Create two D6 dice
d6 = Die()
d10 = Die(10)

#Make some rolls and store results in a list
results = []

for roll_num in range(50000):
    result = d6.roll() + d10.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = d6.num_sides + d10.num_sides
poss_results = range(2, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

#Fruther customize chart
fig.update_layout(xaxis_dtick = 1)

fig.show()
fig.write_html('dice_visual_d6d10.html')