import pandas as pd
df = pd.read_csv("happy.csv")
country = input("Enter country:")
a = df.loc[df['country'] == country, 'happiness'].squeeze()
b = df.loc[df['country'] == country, 'gdp'].squeeze()
print(a)
print(b)