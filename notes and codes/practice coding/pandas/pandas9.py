# Create two Pandas DataFrames with a common column
df1 = pd.DataFrame({'Key': ['A', 'B', 'C', 'D'], 'Value1': np.random.randint(1, 100, size=4)})
df2 = pd.DataFrame({'Key': ['A', 'B', 'C', 'E'], 'Value2': np.random.randint(1, 100, size=4)})
print("DataFrame 1:")
print(df1)
print("DataFrame 2:")
print(df2)

# Merge the DataFrames using the common column
merged = pd.merge(df1, df2, on='Key')
print("Merged DataFrame:")
print(merged)
