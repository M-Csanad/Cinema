import pymysql
import mysql.connector

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="rot", 
    passwd="", 
    database="cinema")
cursor = connection.cursor()

try:
    if(connection):
        print("-----------------Connection Successful-----------------")
except Exception as e:
    print("-----------------Problem with Connection-----------------")
    print(f"-----------------{str(e)}-----------------")

connection.close()