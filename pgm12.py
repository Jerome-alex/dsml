import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("line diagram")
plt.plot(x,y, color = 'red',linestyle = 'dotted',marker = 'o',markerfacecolor = 'green',mec='green')
plt.show()
