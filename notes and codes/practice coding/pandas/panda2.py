# Create a Pandas DataFrame with specified columns and index
df = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])
print("Original DataFrame:")
print(df)

# Access the element at row 'Y' and column 'B'
element = df.at['Y', 'B']
print("Element at row 'Y' and column 'B':", element)
