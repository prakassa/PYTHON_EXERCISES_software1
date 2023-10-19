
import random
from geopy.distance import geodesic as GD
from geopy import distance
import mysql.connector
connection =mysql.connector.connect (
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='mariadidi',
    autocommit= True
)

#getting all small airports of Nepal needed for the game
def get_airports():
    sql= """SELECT ident, airport.name as airport_name, type, latitude_deg, longitude_deg
         FROM airport
         Where iso_country='NP'
         AND type = 'small_airport'
         ORDER by RAND()
         """
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def calculate_distance(lat2, lon2):
    result= GD((lat2,lon2),(27.6966, 85.3591)).km
    return result

def consumption(distance):
    two_way_fuel = (distance * 0.91)*2
    return two_way_fuel

name = input("Please enter your name: ")

if name != "":
    print(f"Captain {name}. Thank you for coming to TIA in this hard time. Welcome to the rescue mission.")

    print("Enter 1 - to Show the destinations menu")
    print("Enter 2 - to Launch the rescue flights")
    rescue = []
    option = input()

    if option == "1":
        for airport in get_airports():
            print(airport)

            print("Relaunch to play the game!")

    elif option =="2":
        ICAO2 = input("Enter the ICAO code of the airport you want to fly: ")
        if ICAO2 != "":
            sql = 'select ident,name as "airport name",longitude_deg as "lon2", latitude_deg as "lat2" from airport where iso_country = "NP" and type = "small_airport"'
            cursor = connection.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()

            if data:
                for ident, name, lon2, lat2 in data:
                    if ICAO2 == ident:
                        print(f" The airport is {name}. Longitude: {lon2}, Latitude:{lat2})")

                        distance_covered = calculate_distance(lat2, lon2)
                        print(f"Flight distance: {distance_covered: .2f} Kilometers ")

                        rescued_tourists = random.randint(1,20)
                        print(f"Good job! You rescued {rescued_tourists} tourists. Keep going")
                        rescue.append(rescued_tourists)

                        print(f"you rescued {sum(rescue)} tourists till now")


                        fuel_spent = consumption(distance_covered)
                        print(f"Fuel spent: {fuel_spent: .2f} liters")

                        fuel_left = 3000-fuel_spent
                        print(f"Remaining Fuel: {fuel_left: .2f}")

                        while fuel_left > 200:
                            ICAO2 = input("Enter the ICAO code of the airport you want to fly: ")
                            if ICAO2 != "":
                                sql = 'select ident,name as "airport name",longitude_deg as "lon2", latitude_deg as "lat2" from airport where iso_country = "NP" and type = "small_airport"'
                                cursor = connection.cursor()
                                cursor.execute(sql)
                                data = cursor.fetchall()

                                if data:
                                    for ident, name, lon2, lat2 in data:
                                        if ICAO2 == ident:
                                            print(f" The airport is {name}. Longitude: {lon2}, Latitude:{lat2})")

                                            distance_covered = calculate_distance(lat2, lon2)
                                            print(f"Flight distance: {distance_covered: .2f} Kilometers ")

                                            rescued_tourists = random.randint(1, 20)
                                            print(f"Good job! You rescued {rescued_tourists} tourists. Keep going")
                                            rescue.append(rescued_tourists)

                                            print(f"you rescued {sum(rescue)} tourists till now")


                                            fuel_spent = consumption(distance_covered)
                                            print(f"Fuel spent: {fuel_spent: .2f} liters")

                                            fuel_left = fuel_left-fuel_spent
                                            if fuel_left >= 200:
                                                print(f"Remaining Fuel: {fuel_left}")
                                            else:
                                                print("LOW FUEL")
                                                break


                        if sum(rescue) > 50:
                            print(f"EXCELLENT JOB CAPTAIN. YOU GOT THE MEGA REWARD FOR SAVING {sum(rescue)} TOURISTS. YOU ARE GRANTED INTERNATIONAL RESCUE PILOT LISCENCE")
                        elif sum(rescue) < 15:
                            print(f"Your flying liscence is ceased for lacking ethics during these hard times. You just rescued {sum(rescue)} tourists. You could have done much better")
                        else:
                            print(f"Thank you for your effort, Captain. You saved {sum(rescue)} tourists all together.")
                        break


else:
    print("Program ENDED")