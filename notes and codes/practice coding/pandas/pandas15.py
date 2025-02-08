# Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])
print("Original DataFrame:")
print(df)

# Apply a function that doubles the values of the DataFrame
df_doubled = df.applymap(lambda x: x * 2)
print("Doubled DataFrame:")
print(df_doubled)
