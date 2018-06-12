import folium
#map = folium.Map(location=[45.43, -122.54], zoom_start=6, tiles="Mapbox Bright")
map = folium.Map(location=[45.43, -122.54], zoom_start=7)

import pandas as pd
coords = pd.read_csv("Volcanoes.txt")
lat = list(coords["LAT"])
lon = list(coords["LON"])

#map.add_child(folium.Marker(location=[45.43, -122.54], popup="Hi I am a Marker",icon=folium.Icon(color='green')))
fg = folium.FeatureGroup(name="My Map")
for lt,ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Volcano",icon=folium.Icon(color='green')))
map.add_child(fg)



map.save("Map1.html")
