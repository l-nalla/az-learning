import pandas as pd

df = pd.read_csv("/workspaces/az-learning/Pandas/datasets/HDFC.csv")


# print(df.describe())
print(df)

# print(df.isna())

# print(df.isnull())

# print(df.isna().sum())

# print(df.isnull().sum())

# print(pd.to_datetime(df['Date'], utc=True, ))

# print(pd.to_datetime(1738546156, unit='s'))


print(df.count())

print(df['Series'].unique())

print(df.columns)

print(type(df.columns))

df2 = pd.DataFrame(df.columns)

# print(df2)


print(df.info())

print(df.dtypes)

df3 = df.drop(3, axis=0) # to drop entire row axis=0
df4 = df.drop('Trades', axis=1)

print(df3)
print(df4)