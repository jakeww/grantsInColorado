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

# Find the average and count of grants for each restaurant type
grouped_data = df_CO.groupby('GroupedRestaurantType')['GrantAmount'].agg(['mean', 'count'])

N = 10 
grouped_data = grouped_data.sort_values(by='mean', ascending=True).tail(N)

fig, ax = plt.subplots(figsize=(12, 8))

bar_colors = plt.cm.viridis(np.linspace(0, 1, N))
bar_plot = ax.barh(grouped_data.index.str.title(), grouped_data['mean'], color=bar_colors, edgecolor='black', linewidth=1.2, alpha=0.85)

# Display the average grant amount for each restaurant type at the end of the bar graph
for i, v in enumerate(grouped_data['count']):
    offset = grouped_data['mean'].max() * 0.01
    ax.text(grouped_data['mean'][i] + offset, i - 0.1, '${:,.0f}'.format(grouped_data['mean'][i]), fontsize=12)


ax.grid(axis='x', linestyle='--', alpha=0.7)
ax.set_ylabel('Restaurant Type', fontsize=14, labelpad=12)
ax.set_xlabel('Average Grant Amount', fontsize=14, labelpad=12)
ax.set_title('Average Grant Amount by Restaurant Type in CO', fontsize=18, pad=20)
ax.set_xlim([0, grouped_data['mean'].max() * 1.1])

# Format x-axis as dollar amounts
formatter = ticker.FuncFormatter(lambda x, pos: '${:,.0f}'.format(x))
ax.xaxis.set_major_formatter(formatter)
plt.xticks(fontsize=12)

# Capitalize y-axis labels
plt.yticks(fontsize=12)

# Save the plot as an image file
plt.savefig('restaurant_type_grant_amount_CO.png')

plt.show()
