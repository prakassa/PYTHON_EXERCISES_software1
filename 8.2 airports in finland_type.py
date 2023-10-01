import mysql.connector
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='game',
         user='root',
         password='mariadidi',
         autocommit=True
         )
area_code = input("enter the area code")

sql = 'select name,type,iso_country from airport order by type asc '
cursor = connection.cursor()
cursor.execute(sql)
data = cursor.fetchall()


if data:
    for name, type,iso_country in data:
        if iso_country == area_code:
            print(f"{name} {type}")



cursor.close()
connection.close()