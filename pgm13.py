import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2])
y=np.array([4,5])
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("legend")
plt.plot(x,y, color = 'red',linestyle = 'solid',marker = 'o',mfc= 'green',mec='green', label='line1')
plt.plot(y,x, color = 'orange',linestyle = 'solid',marker = 'o',mfc= 'blue',mec='blue',label='line2')
plt.legend()
plt.show()

