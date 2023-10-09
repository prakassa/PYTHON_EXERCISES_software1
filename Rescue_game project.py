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

# estimated consumption of a small aircraft
    two_way_fuel_need = (distance * 0.91) * 2
    return two_way_fuel_need

# Hub airport location
lat1 =  27.6966
lon1 =  85.3591
#Fuel_quota = 2 tons
ICAO2 = input("Enter the ICAO code of airport you want to go")

sql = 'select ident,name as "airport name",longitude_deg as "lon2", latitude_deg as "lat2" from airport where iso_country = "NP" and type = "small_airport"'
cursor = connection.cursor()
cursor.execute(sql)
data = cursor.fetchall()

if data:
    for ident,name,lon2,lat2 in data:
        if ICAO2 == ident:
            print(f" longitude 0f the airport = {lon2}, latitude of the airport  = {lat2})")

fuel_Spent = print(f" you spent  {consumption(lat1,lon1,lat2,lon2)} KGs of fuel")

fuel_left = print(f"remaining fuel is {(2000-consumption(lat1, lon1, lat2, lon2))} kgs")


