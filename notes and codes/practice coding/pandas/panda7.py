# Create a Pandas DataFrame with 2 columns: 'Category' and 'Value'
df = pd.DataFrame({'Category': np.random.choice(['A', 'B', 'C'], size=10), 'Value': np.random.randint(1, 100, size=10)})
print("Original DataFrame:")
print(df)

# Group the DataFrame by 'Category' and compute the sum and mean of 'Value' for each category
grouped = df.groupby('Category')['Value'].agg(['sum', 'mean'])
print("Grouped DataFrame:")
print(grouped)
