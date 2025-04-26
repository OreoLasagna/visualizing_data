import matplotlib.pyplot as plt

#input_values = [1, 2, 3, 4, 5]
#cubes = [1, 8, 27, 64, 125]

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c= y_values, cmap = plt.cm.Blues, s = 10)
#Hmm. So I can't just go ax.plot. This only works for 

#Set title and label axes
ax.set_title('Cubed Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Cubed Value', fontsize = 14)

ax.tick_params(labelsize = 14)

plt.show()

