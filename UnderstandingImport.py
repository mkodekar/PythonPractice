import statistics

exampleList = [4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]

x = statistics.variance(exampleList)
y = statistics.mean(exampleList)

print(x)
print(y)

from statistics import variance, mean

exampleList = [4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]

x = variance(exampleList)
y = mean(exampleList)
print(x)
print(y)

from statistics import variance as v, mean as m

exampleList = [4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]

x = v(exampleList)
y = m(exampleList)
print(x)
print(y)

from statistics import *

exampleList = [4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]

x = variance(exampleList)
y = mean(exampleList)

print(x)
print(y)
