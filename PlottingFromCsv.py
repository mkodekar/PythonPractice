from builtins import print
from matplotlib import pyplot as plt
from matplotlib import style as stl
import numpy as np
import csv

stl.use('ggplot')

plt.title('Epic chart')
plt.xlabel('X axis')
plt.ylabel('Y label')

x, y = np.loadtxt('plotting.csv', unpack=True, delimiter=',')

plt.plot(x, y, 'r', label='line 1')

plt.legend()

plt.show()
