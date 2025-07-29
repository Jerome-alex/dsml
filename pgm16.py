import matplotlib.pyplot as plt
import numpy as np
x=np.array(["java","python","php","javascript","c#","c++"])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
colors=["red", "blue", "green", "orange", "purple", "cyan"]
plt.xlabel("prgram_languages")
plt.ylabel("popularity")
plt.title("bar chart")
plt.barh(x,y,color=colors)
plt.show()
