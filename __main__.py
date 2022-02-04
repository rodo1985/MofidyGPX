import gpxpy
import gpxpy.gpx
import folium

# open gpx file
gpx_file = open('input.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

# get coordinates
coord = []
for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coord.append([point.latitude, point.longitude])

# select point where you want to cut the track
middle_index = 3016
first_half = coord[:middle_index]
second_half = coord[middle_index:]

# change the order
out = second_half + first_half

# creating a view in folium
myMap = folium.Map(location=[coord[0][0],coord[0][1]],zoom_start=11)
folium.Marker(out[0]).add_to(myMap)
folium.Marker(out[len(out)-1]).add_to(myMap)
folium.PolyLine(coord, color="blue", weight=2.5, opacity=1).add_to(myMap)
myMap.save("index.html")


# Creating a new file:
# --------------------

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

for o in out:
    # Create points:
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(o[0], o[1]))

with open("output.gpx", "w") as f:
    f.write( gpx.to_xml())