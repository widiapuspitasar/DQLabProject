# -*- coding: utf-8 -*-
"""hadeuh.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14NhSaAbMsloFQvzGYNyaGz7RRfnnqoOF
"""

# A.1 installing package
!pip install pandas
!pip install pandasql
!pip install --upgrade 'sqlalchemy <2.0'
!pip install plotly
#!pip install dash
!pip install jupyter-dash
#instal streamlit
!pip install streamlit

# Library data manipulation
import pandas as pd
import pandasql as ps
import numpy as np

# Library Data Visualization
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# Library Dashboarding
from jupyter_dash import JupyterDash
from dash import html, dcc, Input, Output
import streamlit as st

lingtings_data = pd.read_csv('/content/DQLab_listings(22Sep2022) (1).csv')
nieghbourhood_data = pd.read_csv('/content/DQLab_nieghbourhood(22Sep2022).csv')
reviews_data = pd.read_csv('/content/DQLab_reviews(22Sep2022).csv')

reviews_data.isnull().sum()

nieghbourhood_data.isnull().sum()

lingtings_data.isnull().sum()

# Mengubah kolom 'date' menjadi tipe data datetime
reviews_data['date'] = pd.to_datetime(reviews_data['date'])

# Membuat kolom baru 'year' yang hanya berisi tahun
reviews_data['year'] = reviews_data['date'].dt.year

reviews_data = reviews_data.rename(columns={'listing_id': 'id'})

merged_data = pd.merge(reviews_data,lingtings_data, on='id')

merged_data2 = pd.merge(nieghbourhood_data, merged_data, on='neighbourhood')

merged_data2.isnull().sum()

merged_data2['date'] = pd.to_datetime(merged_data2['date'])

merged_data2.info()

merged_data2[["price", "availability_365","minimum_nights"]].describe()

#grouped_data = merged_data2.groupby('neighbourhood')

reviews_data

import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the average price for each neighborhood
neighborhood_prices = merged_data2.groupby('neighbourhood')['price'].mean().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='price', data=neighborhood_prices)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Average Price')
plt.title('Average Price by Neighborhood')

# Add text labels on top of each bar
for index, row in neighborhood_prices.iterrows():
    plt.annotate(f"{row['price']:.0f}", (index, row['price']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.show()

median_prices = merged_data2.groupby('neighbourhood')['price'].median()
print(median_prices)

# Calculate the average price for each neighborhood
neighborhood_prices = merged_data2.groupby('neighbourhood')['price'].median().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='price', data=neighborhood_prices)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Average Price')
plt.title('Median Price by Neighborhood')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Add text labels on top of each bar
for index, row in neighborhood_prices.iterrows():
    plt.annotate(f"{row['price']:.0f}", (index, row['price']), ha='center', va='bottom')

# Display the plot
plt.show()

# Calculate the average price for each neighborhood
neighborhood_group_prices = merged_data2.groupby('neighbourhood_group')['price'].mean().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood_group', y='price', data=neighborhood_group_prices)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighbourhood group')
plt.ylabel('Average Price')
plt.title('Average Price by Neighborhood Group')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Add text labels on top of each bar
for index, row in neighborhood_group_prices.iterrows():
    plt.annotate(f"{row['price']:.0f}", (index, row['price']), ha='center', va='bottom')

# Display the plot
plt.show()



# Host dengan jumlah listing terbanyak
most_listings_host = merged_data2['host_id'].value_counts().idxmax()
most_listings_count = merged_data2['host_id'].value_counts().max()
most_listings_host_name = merged_data2.loc[merged_data2['host_id'] == most_listings_host, 'host_name'].iloc[0]

print(f"Host dengan jumlah listing terbanyak: {most_listings_host_name} (Host ID: {most_listings_host}), Total Listing: {most_listings_count}")

# Host dengan jumlah listing paling sedikit
least_listings_host = merged_data2['host_id'].value_counts().idxmin()
least_listings_count = merged_data2['host_id'].value_counts().min()
least_listings_host_name = merged_data2.loc[merged_data2['host_id'] == least_listings_host, 'host_name'].iloc[0]

print(f"Host dengan jumlah listing paling sedikit: {least_listings_host_name} (Host ID: {least_listings_host}), Total Listing: {least_listings_count}")

# Mengubah kolom 'tanggal' menjadi tipe data datetime jika belum
merged_data2['date'] = pd.to_datetime(merged_data2['date'])

# Membuat kolom baru 'tahun' yang hanya berisi tahun
merged_data2['date'] = merged_data2['date'].dt.year

# Menampilkan data dengan kolom 'tahun' yang hanya berisi tahun
print(merged_data2[['date', 'tahun']].head())

sorted_data = merged_data2.sort_values('date', ascending=True)

sorted_data

merged_data2.info()

# Mengambil tahun dari kolom tanggal (misalnya kolom "date")
#merged_data2['year'] = merged_data2['yeay'].dt.year

# Mengelompokkan data berdasarkan tahun dan menghitung jumlah listing
listing_counts_by_year = merged_data2.groupby('year')['id'].count()

# Memvisualisasikan perubahan tren menggunakan line plot
plt.figure(figsize=(10, 6))
listing_counts_by_year.plot(marker='o')
plt.xlabel('Year')
plt.ylabel('Jumlah Listing')
plt.title('Perubahan Trend Penyewaan Listing dari Tahun ke Tahun')
plt.grid(True)

# Mendapatkan nilai sumbu x saat ini
current_xticks = plt.gca().get_xticks()

# Mengatur label sumbu x dengan format yang diinginkan (tanpa koma di belakang angka)
plt.gca().set_xticklabels([int(xtick) for xtick in current_xticks])
plt.show()

lingtings_data

room_type_counts = lingtings_data['room_type'].value_counts()
print(room_type_counts)

average_reviews_by_room_type = merged_data2.groupby('room_type')['id'].count()

plt.figure(figsize=(10, 6))
sns.barplot(x=average_reviews_by_room_type.index, y=average_reviews_by_room_type.values)
plt.xlabel('Room Type')
plt.ylabel(' Number of Reviews')
plt.title(' Number of Reviews by Room Type')
plt.xticks(rotation=90)

#for index, row in average_reviews_by_room_type.iterrows():
#    plt.annotate(f"{row['price']:.0f}", (index, row['price']), ha='center', va='bottom')
plt.show()

import seaborn as sns

sns.boxplot(x='room_type', y='id', data=merged_data2)
plt.xlabel('Room Type')
plt.ylabel('Number of Reviews')
plt.title('Comparison of Number of Reviews by Room Type')
plt.show()

duplicated_data = merged_data2.duplicated()
if duplicated_data.any():
    print("Data contains duplicates")
else:
    print(0)

merged_data2

# Calculate the average review for each neighborhood
neighborhood_reviews = merged_data2.groupby('neighbourhood')['id'].count().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='id', data=neighborhood_reviews)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Number Review')
plt.title('Number Review by Neighborhood')

# Add text labels on top of each bar
#for index, row in neighborhood_reviews.iterrows():
#    plt.annotate(f"{row['host_id']:.0f}", (index, row['host_id']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.show()

nieghbourhood_data

# Calculate the average review for each neighborhood
neighborhood_reviews = merged_data2.groupby('neighbourhood_group')['id'].count().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood_group', y='id', data=neighborhood_reviews)

# Set x-axis label, y-axis label, and title
plt.xlabel('neighbourhood_group')
plt.ylabel('Number Review')
plt.title('Number Review by Neighborhood Group')

# Add text labels on top of each bar
#for index, row in neighborhood_reviews.iterrows():
#    plt.annotate(f"{row['host_id']:.0f}", (index, row['host_id']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.show()

merged_data2

nique_neighbourhood_groups = merged_data2['neighbourhood_group'].unique()
nique_neighbourhood_groups

new_table = merged_data2.loc[merged_data2['neighbourhood_group'] == 'Central Region', ['neighbourhood_group', 'neighbourhood', 'price','id']].copy()
new_table2 = merged_data2.loc[merged_data2['neighbourhood_group'] == 'East Region', ['neighbourhood_group', 'neighbourhood', 'price','id']].copy()
new_table3 = merged_data2.loc[merged_data2['neighbourhood_group'] == 'North Region', ['neighbourhood_group', 'neighbourhood', 'price','id']].copy()
new_table4 = merged_data2.loc[merged_data2['neighbourhood_group'] == 'West Region', ['neighbourhood_group', 'neighbourhood', 'price','id']].copy()
new_table5 = merged_data2.loc[merged_data2['neighbourhood_group'] == 'North-East Region', ['neighbourhood_group', 'neighbourhood', 'price','id']].copy()

Central_region = new_table.groupby('neighbourhood')['id'].count().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='id', data=Central_region)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Number of Views')
plt.title('Number of Views by Central Region')

# Add text labels on top of each bar
for index, row in Central_region.iterrows():
    plt.annotate(f"{row['id']:.0f}", (index, row['id']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.show()

East_region = new_table2.groupby('neighbourhood')['id'].count().reset_index()

# Set figure size
plt.figure(figsize=(7, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='id', data=East_region)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Number of Views')
plt.title('Number of Views by East Region')

# Add text labels on top of each bar
for index, row in East_region.iterrows():
    plt.annotate(f"{row['id']:.0f}", (index, row['id']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
#plt.xticks(rotation=90)

# Display the plot
plt.show()

# Calculate the average price for each neighborhood
north_region_prices = new_table3.groupby('neighbourhood')['id'].count().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='id', data=north_region_prices)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Number of Views')
plt.title('Number of Views by North Region')

# Add text labels on top of each bar
for index, row in north_region_prices.iterrows():
    plt.annotate(f"{row['id']:.0f}", (index, row['id']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
#plt.xticks(rotation=90)

# Display the plot
plt.show()

west_region_prices = new_table4.groupby('neighbourhood')['id'].count().reset_index()

# Set figure size
plt.figure(figsize=(13, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='id', data=west_region_prices)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Number of Views')
plt.title('Number of Views by West Region')

# Add text labels on top of each bar
for index, row in west_region_prices.iterrows():
    plt.annotate(f"{row['id']:.0f}", (index, row['id']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
#plt.xticks(rotation=90)

# Display the plot
plt.show()

NorthEast_region_prices = new_table5.groupby('neighbourhood')['id'].count().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='id', data=NorthEast_region_prices)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Number of Views')
plt.title('Number of Views by North East Region')

# Add text labels on top of each bar
for index, row in NorthEast_region_prices.iterrows():
    plt.annotate(f"{row['id']:.0f}", (index, row['id']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
#plt.xticks(rotation=90)

# Display the plot
plt.show()

# Calculate the average price for each neighborhood
central_region_prices = new_table.groupby('neighbourhood')['price'].mean().reset_index()

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(x='neighbourhood', y='price', data=central_region_prices)

# Set x-axis label, y-axis label, and title
plt.xlabel('Neighborhood')
plt.ylabel('Average Price')
plt.title('Average Price by Central Region')

# Add text labels on top of each bar
for index, row in central_region_prices.iterrows():
    plt.annotate(f"{row['price']:.0f}", (index, row['price']), ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.show()

"""## **pengaruh longitude dan latiitude**"""

mean_diff_location = merged_data2.groupby('neighbourhood')['longitude', 'latitude'].mean()
mean_diff_location

import matplotlib.pyplot as plt

# Membuat scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(merged_data2['longitude'], merged_data2['latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Location Scatter Plot')

# Menampilkan label nama neighborhood pada setiap titik
for i, neighbourhood in enumerate(merged_data2['neighbourhood']):
    plt.annotate(neighbourhood, (merged_data2['longitude'].iloc[i], merged_data2['latitude'].iloc[i]))

plt.show()

import matplotlib.pyplot as plt

# Mengelompokkan data berdasarkan neighborhood dan menghitung rata-rata longitude dan latitude
neighborhood_location = merged_data2.groupby('neighbourhood')['longitude', 'latitude'].mean()

# Menyiapkan data untuk tabel
neighborhood_names = neighborhood_location.index.tolist()
neighborhood_indices = range(1, len(neighborhood_names)+1)
table_data = list(zip(neighborhood_indices, neighborhood_names))

# Membuat subplots untuk grafik dan tabel
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot scatter plot
ax1.scatter(neighborhood_location['longitude'], neighborhood_location['latitude'])
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.set_title('Location Scatter Plot by Neighborhood')

# Menampilkan label nama neighborhood pada setiap titik
for i, neighbourhood in enumerate(neighborhood_names):
    ax1.annotate(neighbourhood, (neighborhood_location['longitude'].iloc[i], neighborhood_location['latitude'].iloc[i]), xytext=(5, 5), textcoords='offset points')

# Membuat tabel
table = ax2.table(cellText=table_data, colLabels=['Index', 'Neighborhood'], loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Menghilangkan grid pada tabel
ax2.axis('off')

plt.show()

import matplotlib.pyplot as plt

# Mengelompokkan data berdasarkan neighborhood dan menghitung rata-rata longitude dan latitude
neighborhood_location = merged_data2.groupby('neighbourhood_group')['longitude', 'latitude'].mean()

# Membuat scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(neighborhood_location['longitude'], neighborhood_location['latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Location Scatter Plot by Neighborhood')

# Menampilkan label nama neighborhood pada setiap titik
for neighbourhood_group, row in neighborhood_location.iterrows():
    plt.annotate(neighbourhood_group, (row['longitude'], row['latitude']), xytext=(3, 3), textcoords='offset points')

plt.show()

region= merged_data

unique_neighbourhood_groups = merged_data2['neighbourhood_group'].unique()
unique_neighbourhood_groups

import matplotlib.pyplot as plt

# Mengambil data longitude, latitude, dan price
longitude = merged_data2['longitude']
latitude = merged_data2['latitude']
price = merged_data2['price']

# Membuat scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(longitude, latitude, c=price, cmap='viridis', alpha=0.5)
plt.colorbar(label='Price')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Property Rental Rates by Location')

plt.show()

import matplotlib.pyplot as plt
import numpy as np


# Create a color dictionary to assign colors based on neighborhood_group
color_dict = {'Central Region': 'red', 'East Region': 'blue', 'North-East Region': 'green','North Region':'yellow','West Region':'black'}  # Add more colors if needed

# Get the colors for each data point based on neighborhood_group
colors = merged_data2['neighbourhood_group'].map(color_dict)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(merged_data2['longitude'], merged_data2['latitude'], c=colors)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Location Scatter Plot by Neighborhood Group')

# Show the legend for the neighborhood_group colors
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=group, markerfacecolor=color)
                   for group, color in color_dict.items()]
plt.legend(handles=legend_elements)

plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Calculate the mean longitude and latitude for each neighborhood
neighborhood_location = merged_data2.groupby('neighbourhood')[['longitude', 'latitude']].mean()

# Merge with the original dataset to retain the neighborhood_group information
neighborhood_location = pd.merge(neighborhood_location, merged_data2[['neighbourhood', 'neighbourhood_group']], on='neighbourhood')

# Create a color dictionary to assign colors based on neighborhood_group
color_dict = {'Central Region': 'red', 'East Region': 'blue', 'North-East Region': 'green','North Region':'yellow','West Region':'black'}  # Add more colors if needed

# Get the colors for each data point based on neighborhood_group
colors = neighborhood_location['neighbourhood_group'].map(color_dict)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(neighborhood_location['longitude'], neighborhood_location['latitude'], c=colors)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Location Scatter Plot by Neighborhood Group')

# Show the legend for the neighborhood_group colors
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=group, markerfacecolor=color)
                   for group, color in color_dict.items()]
plt.legend(handles=legend_elements)

plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Calculate the mean longitude and latitude for each neighborhood
neighborhood_location = merged_data2.groupby('neighbourhood')[['longitude', 'latitude']].mean()

# Merge with the original dataset to retain the neighborhood group information
neighborhood_location = pd.merge(neighborhood_location, merged_data2[['neighbourhood', 'neighbourhood_group']], on='neighbourhood')

# Define a color palette for the neighborhood_group
color_palette = {'Central Region': 'red', 'East Region': 'blue', 'North-East Region': 'green', 'North Region': 'yellow', 'West Region': 'purple'}

# Create the scatter plot with colors based on neighborhood_group
plt.figure(figsize=(21, 15))
for group, data in neighborhood_location.groupby('neighbourhood_group'):
    plt.scatter(data['longitude'], data['latitude'], c=color_palette[group], label=group)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Location Scatter Plot by Neighborhood')

# Show the legend for the neighborhood_group colors
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=group, markerfacecolor=color)
                   for group, color in color_palette.items()]
plt.legend(handles=legend_elements)

# Annotate neighborhood names
for i, row in neighborhood_location.iterrows():
    plt.annotate(row['neighbourhood'], (row['longitude'], row['latitude']), xytext=(3, 3), textcoords='offset points')

plt.show()

# A. create dash app
app = JupyterDash(__name__)

# B. Design Layout
app.layout = html.Div(children=[
    html.H1("Analyzing Airbnb Accommodations in Singapore: Optimizing Property Rental Revenue", 
            style={'textAlign':'center','font-family':'arial','font-size':50,'color':'yellow','background-color':'black'})
    ,html.P("Menampilkan Multiline chart dengan callback", style={'textAlign':'center','font-family':'arial','font-size':20,'color':'white','font-weight':'ligter'})
    
    # Filternya
    #,dcc.Dropdown(options=['Pilihan 1', 'Pilihan 2', 'Pilihan 3'])
    ,html.Div(children=[
        dcc.Dropdown(options=[{'label':k, 'value':k} for k in available_city], multi=True, value=['Surabaya','Malang'],id='dropdown-ku')
    ],style={'margin-left':200,'margin-right':200,'margin-top':50})
    # menampilkan chart
    ,html.Div(children=[
        #dcc.Graph(figure=fig_line)
        dcc.Graph(id='display-ku')
    ],style={'margin-left':200,'margin-right':200,'margin-top':30})
    ,html.Br()
],style={'background-color':'black'})

# C. Callback
# c.1 callback decoder
@app.callback(
    Output('display-ku', component_property='figure')
    ,Input('dropdown-ku',component_property='value')
)
# c.2 Callback Update Function
def layoutku(value):
  dataku = monthly_agg_city_df[monthly_agg_city_df['city'].isin(value)]
  fig_line = px.line(dataku,x="order_month",y="gmv",color="city",template="simple_white",color_discrete_sequence=["#D14D72","#569DAA","#89375F","#FF8400","#7AA874"], markers=True)
  fig_line.update_layout(title="<b>Total Gross Merchandise Value (GMV) by City</b>", title_font=dict(size=20,family="arial"))
  fig_line.update_xaxes(title="<b>Order Month</b>",title_font=dict(size=13,family="arial"))
  fig_line.update_yaxes(title="<b>Total GMV (Rp)</b>",title_font=dict(size=13,family="arial"))
  fig_line.update_traces(line=dict(width=3),marker=dict(size=8))
  return fig_line

# D. Run Application
if __name__ == '__main__':
  app.run_server()

"""## **pembuatan dasboard**"""

# Tulis aplikasi Streamlit Anda di sini
def main():
    st.title("Analyzing Airbnb Accommodations in Singapore: Optimizing Property Rental Revenue")
    st.write("Hello, world!")

if __name__ == '__main__':
    main()

!streamlit run <hadeuh>.py

"""## **JANGAN KEBAWAH LEMOT**"""

import plotly.express as px

fig = px.bar(merged_data2, x='neighbourhood', y='price', 
             title='Distribusi Harga Berdasarkan Lingkungan',
             labels={'neighbourhood': 'neighbourhood','price': 'price'},
             color='price', opacity=1)

fig.update_layout(title="<b>Distribusi Harga Berdasarkan Lingkungan</b>", title_font=dict(size=25, color="black"), title_x=0.5)

fig.update_xaxes(title="<b>neighbourhood</b>", title_font=dict(size=16, family="arial", color="black"), tickfont=dict(size=13, family="arial", color="black"))
fig.update_yaxes(title="<b>price</b>", title_font=dict(size=16, family="arial", color="black"), tickfont=dict(size=13, family="arial", color="black"))

# Menampilkan grafik
fig.show()



import plotly.express as px

fig = px.bar(merged_data2, x='neighbourhood', y='price', 
             title='Distribution of Prices by Neighborhood',
             labels={'neighbourhood': 'neighbourhood', 'price': 'price'},color='price', opacity=1, hover_data={'price': ':.2f'})

fig.update_layout(
    title="<b>Distribution of Prices by Neighborhood</b>",
    title_font=dict(size=25, color="black"),
    title_x=0.5,
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white'
)

fig.update_xaxes(
    title="<b>Price</b>",
    title_font=dict(size=16, family="arial", color="white"),
    tickfont=dict(size=13, family="arial", color="white")
)

fig.update_yaxes(
    title="<b>Neighbourhood</b>",
    title_font=dict(size=16, family="arial", color="white"),
    tickfont=dict(size=13, family="arial", color="white")
)

# Menampilkan grafik
fig.show()

