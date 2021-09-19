import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyC3KO4bSvKS81aNgRAR4ysQXrHAfJp-Bw4')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')


def between_lat_long_driving(lat1, lon1, lat2, lon2):
    matrix = gmaps.distance_matrix((lat1, lon1), (lat2, lon2), mode="driving", units="metric")
    return (int(matrix["rows"][0]["elements"][0]["distance"]["value"]))

between_lat_long_driving(41.43206, -81.38992, 42.43206, -82.38992)