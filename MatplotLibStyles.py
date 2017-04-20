from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

plt.grid(True, color='k')

plt.plot([4, 5, 6, 7], [3, 7, 8, 9], 'r', linewidth=5, label='line 1')
plt.plot([5, 6, 7, 8, 9], [4, 87, 98, 109, 100], 'g', linewidth=5, label='line 2')
plt.scatter([4, 5, 6, 7], [27, 58, 48, 56],  color='c', label='line 3')
plt.bar([7, 8, 9], [90, 60, 78],  color='c', label='line 4', align='center')
plt.bar([10,11, 12], [90, 60, 78],  color='g', label='line 5', align='center')
plt.title('Example chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()


plt.show()
