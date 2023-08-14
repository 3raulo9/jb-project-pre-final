import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'RauloAsadov',


)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE databaseforcrm")
print("data base created")