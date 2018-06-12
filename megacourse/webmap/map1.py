import folium
map = folium.Map(location=[45.43, -122.54], zoom_start=6, tiles="Mapbox Bright")

#map.add_child(folium.Marker(location=[45.43, -122.54], popup="Hi I am a Marker",icon=folium.Icon(color='green')))
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[45.43, -122.54], popup="Hi I am a Marker",icon=folium.Icon(color='green')))
map.add_child(fg)



map.save("Map1.html")
