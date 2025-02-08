# Create a Pandas DataFrame with MultiIndex consisting of 'Category' and 'SubCategory'
arrays = [['A', 'A', 'B', 'B', 'C', 'C'], ['one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'SubCategory'))
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 3)), index=index, columns=['Value1', 'Value2', 'Value3'])
print("MultiIndex DataFrame:")
print(df)

# Compute the sum of values for each 'Category' and 'SubCategory'
sum_values = df.groupby(['Category', 'SubCategory']).sum()
print("Sum of values:")
print(sum_values)
