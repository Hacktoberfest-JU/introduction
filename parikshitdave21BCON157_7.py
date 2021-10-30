import pandas as pd
df = pd.DataFrame([[10, 20, 30, 40],
[7, 14, 21, 28], [55, 15, 8, 12],
[15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
columns=['Apple', 'Orange', 'Banana', 'Pear'],
index=['Basket1', 'Basket2', 'Basket3','Basket4','Basket5', 'Basket6'])
print(df)
print("\n------ Calculate Mean ---\n")
print(df.mean(axis=0))
print("\n----- Calculate Median ---\n")
print(df.median())
print("\n------ Calculate Mode ----\n")
print(df.mode())
