import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Rabbits', 'Cats', 'Dogs', 'Hamsters'
sizes = [15, 30, 45, 10]
explode = (0, 0, 0.1, 0)  # only "explode" the 3rd slice (i.e. 'Dogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
