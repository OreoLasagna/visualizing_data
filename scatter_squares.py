import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

#Set chart title and label axes.
ax.set_title('Square Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square', fontsize = 14)

#Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
#Four Arguments
#Minimum and maximum values for x-values: x is from 0 to 1100
#Minimum and maximum values for y-values: y is 0 to 1,100,000

ax.ticklabel_format(style = 'plain')

#Set the size of tick labels
ax.tick_params(labelsize = 14)

plt.show()