import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('olypics2016.csv',index_col='country')
gold = df.loc['goldmedal']
plt.pie(gold,labels=gold.index)
plt.title('Gold Medals by Country - Olympics 2016')
plt.show()

