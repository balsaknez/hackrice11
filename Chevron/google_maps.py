import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyC3KO4bSvKS81aNgRAR4ysQXrHAfJp-Bw4')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')


def between_lat_long_driving(lat1, lon1, lat2, lon2):
    reverse_geocode_result1 = gmaps.reverse_geocode((lat1, lon1))
    reverse_geocode_result2 = gmaps.reverse_geocode((lat2, lon2))
    matrix = gmaps.distance_matrix_test(reverse_geocode_result1, reverse_geocode_result2)
    print(matrix)

between_lat_long_driving(41.43206, -81.38992, 42.43206, -82.38992)