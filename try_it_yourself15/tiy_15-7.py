from die import Die
import plotly.express as px

#Create three D6 dice
d6_1 = Die()
d6_2 = Die()
d6_3 = Die()

#Make some rolls and store results in a list
results = []

for roll_num in range(5000):
    result = d6_1.roll() + d6_2.roll() + d6_3.roll()
    results.append(result)

#Analyze the results
frequencies = []
max_result = d6_1.num_sides + d6_2.num_sides + d6_3.num_sides
poss_results = range(3, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
title = "Results of Rolling three D6 dice 5,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

#Fruther customize chart
fig.update_layout(xaxis_dtick = 1)

fig.show()