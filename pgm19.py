import pandas as pd
name=["Alice", "Bob", "Charlie"]
age=[25,30,35]
score=[88,76,91]
df=pd.DataFrame({"Name":name,"Age":age,"Score":score})
print(df)
print("first two rows")
print(df.head(2))
