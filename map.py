import pandas as pd
import altair as alt
from vega_datasets import data

countries = alt.topo_feature(data.world_110m.url, 'countries')

data_df = pd.read_excel('data.xlsx')
print(data_df.head())

chart = alt.layer(
  alt.Chart(countries)
    .mark_geoshape(fill='lightgray', stroke='white'),
  alt.Chart(data_df)
    .mark_circle(color='green', opacity=0.3)
    .encode(
      longitude='Long:Q',
      latitude='Lat:Q', 
      size=alt.value(2))
).project(
    'equirectangular'
).properties(width=600, height=600).configure_view(stroke=None)

chart.save('chart.html')