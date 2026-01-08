import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\princ\Downloads\archive\Swiggy Bangalore.csv",usecols=[0,1,2,3,4,5,6])

data_cleaned=data.drop(['Offer','URL'],axis=1)
data_cleaned.replace(to_replace=['NA'],value=0)

data_cleaned['Main Cuisine'] = data_cleaned['Category'].str.split(',').str[0]
data_cleaned['Cuisine Count'] = data_cleaned['Category'].apply(lambda x: len(x.split(',')))


area_summary = data_cleaned.groupby('Area').agg({
    'Cost for Two (in Rupees)': 'mean',
    'Restaurant Name': 'count',
    'Rating': 'mean'
}).rename(columns={
    'Restaurant Name': 'Total Restaurants', 
    'Rating': 'Average Rating', 
    'Cost for Two (in Rupees)': 'Average Cost'
})


top_10_areas = area_summary.sort_values(by='Total Restaurants', ascending=False).head(10)
print(top_10_areas)


plt.figure(figsize=(10, 5))
plt.bar(top_10_areas.index, top_10_areas['Total Restaurants'])
plt.title('Top 10 Busiest Areas for Food in Bangalore')
plt.xticks(rotation=45)
plt.show()



data_cleaned.to_csv(r"C:\Users\princ\Downloads\archive\Swiggy_Bangalore_Cleaned.csv", index=False)


top_10_areas.to_csv(r"C:\Users\princ\Downloads\archive\Area_Summary_Report.csv")

