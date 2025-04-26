from die import Die
import plotly.express as px

#Create two D6 dice
d6_1 = Die()
d6_2 = Die()

#Make some rolls and store results in a list
results = []

#for roll_num in range(5000):
#    result = d6_1.roll() * d6_2.roll()
#    results.append(result)

#List comprehension version of results
results = [(d6_1.roll() * d6_2.roll()) for roll_num in range(5000)]

#Analyze the results
frequencies = []
max_result = d6_1.num_sides * d6_2.num_sides
poss_results = range(1, max_result + 1)

#for value in poss_results:
#    frequency = results.count(value)
#    frequencies.append(frequency)

#List comprehension version of frequencies
frequencies = [results.count(value) for value in range(1, max_result + 1)]

#Visualize the results
title = "Results of Rolling two D6 dice 5,000 Times and Multiplying the results"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)

#Fruther customize chart
fig.update_layout(xaxis_dtick = 1)

fig.show()