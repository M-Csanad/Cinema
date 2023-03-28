import pymysql
import mysql.connector




try:
    connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root", 
    passwd="", 
    database="cinema")
    cursor = connection.cursor()
    
    if(connection):
        print("-----------------Connection Successful-----------------")
    
    connection.close()
except Exception as e:
    print(f"-----------------Connection Failed-----------------")
    print(f"-----------------{str(e)}-----------------")

    


