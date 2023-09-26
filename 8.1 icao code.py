#Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)

import mysql.connector
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='game',
         user='root',
         password='mariadidi',
         autocommit=True
         )
icao = input("enter the icao code")

sql = 'select ident,name,municipality from airport;'
cursor = connection.cursor()
cursor.execute(sql)
data = cursor.fetchall()

if data:
    for ident , name , municipality, in data:
        if icao == ident:
            print(f" The airport is {name}. It is located in {municipality}")


cursor.close()
connection.close()
