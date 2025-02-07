## plot sales trend over time
sales_trend=sales_data_df.groupby('Date')['Total Revenue'].sum().reset_index()
plt.plot(sales_trend['Date'],sales_trend['Total Revenue'])
