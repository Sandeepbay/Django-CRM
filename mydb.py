import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sandeepbay@9'
)

cursorObject = dataBase.cursor()

cursorObject.execute("Create Database elderco")

print("All done")