import pandas as pd
import numpy as np

# Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=['A', 'B', 'C', 'D'])
print("Original DataFrame:")
print(df)

# Set the index to be the first column
df.set_index('A', inplace=True)
print("DataFrame with new index:")
print(df)
