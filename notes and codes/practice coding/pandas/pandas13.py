# Create a Pandas DataFrame with columns 'Date', 'Category', and 'Value'
date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
df = pd.DataFrame({'Date': np.random.choice(date_rng, size=20), 'Category': np.random.choice(['A', 'B', 'C'], size=20), 'Value': np.random.randint(1, 100, size=20)})
print("Original DataFrame:")
print(df)

# Create a pivot table to compute the sum of 'Value' for each 'Category' by 'Date'
pivot_table = df.pivot_table(values='Value', index='Date', columns='Category', aggfunc='sum')
print("Pivot Table:")
print(pivot_table)
