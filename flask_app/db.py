import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="12345678",
    database="myappdb"
    )
    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print(err)
    input()
    exit


def addrow(number):
    sql = "INSERT INTO counter (count) VALUES (%s)"
    val = (number)
    mycursor.execute(sql, val)
    mydb.commit()
