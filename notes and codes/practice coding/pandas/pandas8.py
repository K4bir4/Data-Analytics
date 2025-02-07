# Create a Pandas DataFrame with 3 columns: 'Product', 'Category', and 'Sales'
df = pd.DataFrame({'Product': np.random.choice(['Prod1', 'Prod2', 'Prod3'], size=10), 'Category': np.random.choice(['A', 'B', 'C'], size=10), 'Sales': np.random.randint(1, 100, size=10)})
print("Original DataFrame:")
print(df)

# Group the DataFrame by 'Category' and compute the total sales for each category
grouped = df.groupby('Category')['Sales'].sum()
print("Grouped DataFrame:")
print(grouped)
