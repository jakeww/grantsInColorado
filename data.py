import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Group alcohol related restaurant types
def group_restaurant_types(restaurant_type):
    alcohol_related = ['brewpub', 'distillery', 'bar restaurant', 'brewery and/or microbrewery', 'licensed alcohol producer', 'bar', 'winery']
    restaurant_type = ' '.join(restaurant_type.lower().split())

    if restaurant_type in alcohol_related:
        return 'Alcohol Related'
    else:
        return restaurant_type

file_path = '/Users/jakewatembach/Desktop/datavis/rrf_foia.csv'
df = pd.read_csv(file_path)

df_CO = df[df['BusinessState'] == 'CO']
df_CO['GroupedRestaurantType'] = df_CO['RestaurantType'].apply(group_restaurant_types)

# Find the average
grouped_data = df_CO.groupby('GroupedRestaurantType')['GrantAmount'].mean()

N = 10 
grouped_data = grouped_data.sort_values(ascending=True).tail(N)

plt.figure(figsize=(12, 8))
bar_colors = plt.cm.viridis(np.linspace(0, 1, N))
bar_plot = plt.barh(grouped_data.index.str.title(), grouped_data.values, color=bar_colors, edgecolor='black', linewidth=1.2, alpha=0.85)

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.ylabel('Restaurant Type', fontsize=14, labelpad=12)
plt.xlabel('Average Grant Amount', fontsize=14, labelpad=12)
plt.title('Average Grant Amount by Restaurant Type in CO', fontsize=18, pad=20)

# Format x-axis as dollar amounts
ax = plt.gca()
formatter = ticker.FuncFormatter(lambda x, pos: '${:,.0f}'.format(x))
ax.xaxis.set_major_formatter(formatter)
plt.xticks(fontsize=12)

# Capitalize y-axis labels
plt.yticks(fontsize=12)

# Save the plot as an image file
plt.savefig('restaurant_type_grant_amount_CO.png')

plt.show()
