import json

# 2.24
infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# load function takes json file and converts to usable python object
# which is a giant dictionary
eq_data = json.load(infile)

# dump puts it in outfile
json.dump(eq_data, outfile, indent=4)
# eq_data is the object

mags, lons, lats = [], [], []

list_of_eqs = eq_data["features"]
# print(json.dump(eq_data["frequency"]))
for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# print(eq_data["features"][i]["properties"]["mag"])
print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="globale_earthquakes.html")
