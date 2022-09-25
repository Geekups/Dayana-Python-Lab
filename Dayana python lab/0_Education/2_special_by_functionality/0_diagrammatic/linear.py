# ----------------------------------------------------------- simple linear diagram with matplotlib.pyplot
from audioop import lin2alaw
import matplotlib.pyplot as plt

x = [4,5,6,7,8,9,10,12,13,15]
y = [5,6,7,8,9,10,15,16,7,1]

plt.plot(x,y)
plt.show()

# ----------------------------------------------------------- simple linear diagram with matplotlib.pyplot and numpy as data provider
import numpy as np

x = np.random.randint(low=1, high=15, size=30)
plt.plot(x, linewidth=3)
plt.show()

# ----------------------------------------------------------- sample of using plot options 
x = [7,14,21,28,35,42,49]
y = [8,13,21,30,31,44,50]
# option " o-- " show plot points on chart
plt.plot(x, y, 'o--', linewidth=2)
plt.show()