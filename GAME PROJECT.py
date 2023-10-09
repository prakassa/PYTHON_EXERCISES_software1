import random

import mysql.connector
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='game',
         user='root',
         password='mariadidi',
         autocommit=True
         )

from math import radians, sin, cos, sqrt, atan2
def consumption(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    two_way_fuel_need = (distance * 0.91) * 2
    return two_way_fuel_need


lat1 =  27.6966
lon1 =  85.3591

lon2 = float(input("Enter the longitude of the airport"))
lat2 = float(input("Enter the latitude of the airport"))

print(f"the required fuel is {consumption(lat1, lon1, lat2, lon2)} kgs")