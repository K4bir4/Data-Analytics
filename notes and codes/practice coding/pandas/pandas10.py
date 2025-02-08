# Create a Pandas DataFrame with a datetime index ranging from '2021-01-01' to '2021-12-31'
date_rng = pd.date_range(start='2021-01-01', end='2021-12-31', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(0, 100, size=(len(date_rng)))
df.set_index('date', inplace=True)
print("Original DataFrame:")
print(df)

# Compute the rolling mean with a window of 7 days
rolling_mean = df.rolling(window=7).mean()
print("Rolling mean DataFrame:")
print(rolling_mean)
