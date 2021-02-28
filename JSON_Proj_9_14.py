import json

# 2.27

infile2 = open("US_fires_9_14.json", "r")
outfile2 = open("readable_US_fires_9_14.json", "w")

# load function takes json file and converts to usable python object
# which is a giant dictionary
fires_9_14 = json.load(infile2)

# dump puts it in outfile
json.dump(fires_9_14, outfile2, indent=4)
# eq_data is the object

brights2, lons2, lats2 = [], [], []

# Loop through the fires and store the ones with the correct brightness
for fire in fires_9_14:
    if fire["brightness"] >= 450:
        bright = fire["brightness"]
        # print("Brightness: ", bright)
        lon = fire["longitude"]
        lat = fire["latitude"]
        brights2.append(bright)
        lons2.append(lon)
        lats2.append(lat)

"""
print(brights[:10])
print(lons[:10])
print(lats[:10])
"""

# Graph
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data2 = [
    {
        "type": "scattergeo",
        "lon": lons2,
        "lat": lats2,
        "marker": {
            "size": [
                0.03 * bright for bright in brights2
            ],  # list comprehension, blows it up
            "color": brights2,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="Fires 9/14/2020 through 9/20/2020")

fig = {"data": data2, "layout": my_layout}
offline.plot(fig, filename="US_Fires_9_1.html")