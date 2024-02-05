#Name : WebMapFolium
#About : Web Map created with the folium library
#Created by : Chantel Williams
#Date : February 2024

import folium

#https://leaflet-extras.github.io/leaflet-providers/preview/
m = folium.Map(location=(35.857026938566015, -78.75119470710982),
               control_scale=True,
               zoom_start=13,
               min_lat=35.85701,
               max_lat=35.85702,
               min_lon=-78.7511,
               max_lon=-78.7512)
m.save("index.html")
