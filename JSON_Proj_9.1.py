import json

# 2.24
infile = open("US_fires_9_1.json", "r")
outfile = open("readable_US_fires_9_1.json", "w")

# load function takes json file and converts to usable python object
# which is a giant dictionary
fires_9_1 = json.load(infile)

# dump puts it in outfile
json.dump(fires_9_1, outfile, indent=4)
# eq_data is the object

brights, lons, lats = [], [], []

# Loop through the fires and store the ones with the correct brightness
for fire in fires_9_1:
    if fire["brightness"] >= 450:
        bright = fire["brightness"]
        # print("Brightness: ", bright)
        lon = fire["longitude"]
        lat = fire["latitude"]
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

"""
print(brights[:10])
print(lons[:10])
print(lats[:10])
"""

# Graph
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [
                0.03 * bright for bright in brights
            ],  # list comprehension, blows it up
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="Fires 9/1/2020 through 9/13/2020")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="US_Fires_9_1.html")
