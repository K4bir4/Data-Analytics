# Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(4, 3)), columns=['A', 'B', 'C'])
print("Original DataFrame:")
print(df)

# Compute the row-wise and column-wise sum
row_sum = df.sum(axis=1)
column_sum = df.sum(axis=0)

print("Row-wise sum:")
print(row_sum)
print("Column-wise sum:")
print(column_sum)
