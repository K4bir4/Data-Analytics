# Create a Pandas DataFrame with columns 'Year', 'Quarter', and 'Revenue'
df = pd.DataFrame({'Year': np.random.choice([2020, 2021, 2022], size=12), 'Quarter': np.random.choice(['Q1', 'Q2', 'Q3', 'Q4'], size=12), 'Revenue': np.random.randint(1, 1000, size=12)})
print("Original DataFrame:")
print(df)

# Create a pivot table to compute the mean 'Revenue' for each 'Quarter' by 'Year'
pivot_table = df.pivot_table(values='Revenue', index='Year', columns='Quarter', aggfunc='mean')
print("Pivot Table:")
print(pivot_table)
