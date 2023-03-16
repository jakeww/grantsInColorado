import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

plt.figure(figsize=(10, 6))
bar_plot = plt.barh(grouped_data.index, grouped_data.values)
plt.ylabel('Restaurant Type')
plt.xlabel('Average Grant Amount')
plt.title('Average Grant Amount by Restaurant Type in CO')
plt.yticks(fontsize=10)

# Save the plot as an image file
plt.savefig('restaurant_type_grant_amount_CO.png')

plt.show()
