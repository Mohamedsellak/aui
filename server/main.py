import folium
import geocoder
import webbrowser

# Get the location using the IP address
g = geocoder.ip('me')
my_location = g.latlng


# create the map
m = folium.Map(location=[33.747180448149855, -5.007019042968751], zoom_start=13)

# create the Marker for distination
folium.Marker(
    [33.747180448149855, -5.007019042968751], popup="<i>Mt. Hood Meadows</i>", tooltip="taxi 5",
    icon=folium.CustomIcon('img/taxi.png', icon_size=(40,40))
).add_to(m)

# create Marker for my location
folium.Marker(
    my_location, popup="<i>Mt. Hood Meadows</i>", tooltip="Me"
).add_to(m)
m.save('index.html')

# open the html file in the browser
webbrowser.open_new_tab("index.html")
