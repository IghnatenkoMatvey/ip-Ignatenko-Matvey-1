import sqlite3

conn = sqlite3.connect('Chinook_Sqlite.sqlite')

cursor = conn.cursor()

cursor.execute("SELECT Name FROM artists ORDER BY Name")
result = cursor.fetchall()

print(result)

coon.close

>>> sudo apt install python3-pip


