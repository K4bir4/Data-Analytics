# Create a Pandas DataFrame with a MultiIndex (hierarchical index)
arrays = [['A', 'A', 'B', 'B'], ['one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'SubCategory'))
df = pd.DataFrame(np.random.randint(1, 100, size=(4, 3)), index=index, columns=['Value1', 'Value2', 'Value3'])
print("MultiIndex DataFrame:")
print(df)

# Basic indexing and slicing operations
print("Indexing at Category 'A':")
print(df.loc['A'])

print("Slicing at Category 'B' and SubCategory 'two':")
print(df.loc[('B', 'two')])
