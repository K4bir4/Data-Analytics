# Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])
print("Original DataFrame:")
print(df)

# Add a new column that is the product of the first two columns
df['D'] = df['A'] * df['B']
print("DataFrame with new column:")
print(df)
