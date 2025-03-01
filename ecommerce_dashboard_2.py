# eCommerce Dashboard
# A project to analyze and visualize sales data from an online store

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample sales data (replace with real CSV file or database connection)
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Sales': [150, 200, 250, 180, 220, 300, 280, 260, 310, 400]
}
df = pd.DataFrame(data)

# Display the first few rows of the dataset
print("Sample Sales Data:")
print(df.head())

# Create a sales trend visualization
plt.figure(figsize=(10, 5))
sns.lineplot(x='Date', y='Sales', data=df, marker='o', linewidth=2)
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales (€)')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Save the dataset as a CSV file for future analysis
df.to_csv('sales_data.csv', index=False)

print("Sales data successfully saved to 'sales_data.csv'.")
