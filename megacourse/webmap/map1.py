import folium
#map = folium.Map(location=[45.43, -122.54], zoom_start=6, tiles="Mapbox Bright")
map = folium.Map(location=[45.43, -122.54], zoom_start=7)

import pandas as pd
coords = pd.read_csv("Volcanoes.txt")
lat = list(coords["LAT"])
lon = list(coords["LON"])
elev = list(coords["ELEV"])

def color_picker(elevation):
    if elevation < 2000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

#map.add_child(folium.Marker(location=[45.43, -122.54], popup="Hi I am a Marker",icon=folium.Icon(color='green')))
fg = folium.FeatureGroup(name="My Map")
for lt,ln,el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + 'm',
    icon=folium.Icon(color=color_picker(el))))
map.add_child(fg)



map.save("Map1.html")
