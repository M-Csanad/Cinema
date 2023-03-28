import pymysql
import mysql.connector

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root", 
    passwd=""
    )
cursor = connection.cursor()

#print(cursor.execute("SHOW DATABASES"))

try:
    cursor.execute("CREATE DATABASE cinema")
    
except Exception as e:
    print(f"-----------------{str(e)}-----------------")