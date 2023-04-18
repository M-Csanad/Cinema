import pymysql
import mysql.connector

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS `cinema`")
connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    database="cinema"
)
cursor = connection.cursor()


# print(cursor.execute("SHOW DATABASES"))


try:
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS `cinema` CHARACTER SET utf8mb4 COLLATE utf8mb4_hungarian_ci"
    )
    #Deactivate Foreign_Key_Checks
    #cursor.execute(
    #    "SET FOREIGN_KEY_CHECKS=0"
    #)
    #cursor.execute(
    #    "SET GLOBAL FOREIGN_KEY_CHECKS=0"
    #)
    
    # ======= LowPrio ======= 

    TABLE_LowPrio = (
        '''CREATE TABLE IF NOT EXISTS Low_Prio (
    LP_ID INT NOT NULL PRIMARY KEY,
    YEAR CHAR(4) NOT NULL,
    CATEGORY VARCHAR(60) NOT NULL,
    PLAYTIME CHAR(3) NOT NULL,
    PRICE VARCHAR(4) NOT NULL)
    '''    
    )

    cursor.execute(TABLE_LowPrio)
    
    
    val = [
        (0, 2023, 'Krimi;Akciófilm;Thriller;Krimi', 169, 2680),
        (1, 2022, 'Kalandfilm,Fantasy', 122, 2500),
        (2, 2022, 'Fantasy;Sci-Fi;Akció', 192, 2100),
        (3, 2023, 'Akció;Kalandfilm;Vígjáték;Sci-Fi', 120, 2400),
        (4, 2023, 'Dráma;Fikció', 117, 1850),
        (5, 2023, 'Akció;Kalandfilm', 134, 1850)     
    ]

    INSERT_LowPrio = (
        "INSERT INTO `Low_Prio` VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE LP_ID = VALUES(LP_ID)"
    )

    cursor.executemany(INSERT_LowPrio, val)



    # ======= Termek ======= 

    TABLE_Termek = (
        '''CREATE TABLE IF NOT EXISTS Termek (
    TEREM_SZAM INT NOT NULL PRIMARY KEY,
    TEREM_FILM TEXT(50) NOT NULL,
    TEREM_MAXHELY CHAR(3) NOT NULL, 
    LOW_PRIO INT NOT NULL, 
     
    FOREIGN KEY (LOW_PRIO) REFERENCES Low_Prio(LP_ID))'''
    )  # Amikor egy TABLE-t szeretnénk létrehozni, az adattípust kötelező megadni a hosszával együtt!!

    cursor.execute(TABLE_Termek)
    
    val = [
        (1, 'John Wick: 4. felvonás', 250, 0),
        (2, 'Suzume',  150, 1),
        (3, 'Avatar',  150, 2),
        (4, 'A galaxis őrzői: 3. rész', 250, 3),
        (5, 'A bálna',  100, 4),
        (6, 'Dungeons and Dragons: Betyárbecsület', 250, 5)
    ]

    INSERT_Termek = (
        "INSERT INTO `Termek` VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE TEREM_SZAM = VALUES(TEREM_SZAM)"
    )

    cursor.executemany(INSERT_Termek, val)



    # ======= Foglalasok ======= 

    TABLE_Foglalasok = (
        '''CREATE TABLE IF NOT EXISTS Foglalasok (
    FOGLAL_SORSZAM CHAR(12) NOT NULL PRIMARY KEY,
    KERESZTNEV TEXT(25) NOT NULL,
    VEZETEKNEV TEXT(25) NOT NULL,
    SZEKSZAM VARCHAR(50) NOT NULL,
    TEREMSZAM INT NOT NULL,
    
    FOREIGN KEY (TEREMSZAM) REFERENCES Termek(TEREM_SZAM))'''
    )
    cursor.execute(TABLE_Foglalasok)

    
    #Activate Foreign_Key_Checks
    #cursor.execute(
    #    "SET FOREIGN_KEY_CHECKS=1"
    #)
    #cursor.execute(
    #    "SET GLOBAL FOREIGN_KEY_CHECKS=1"
    #)

except Exception as e:
    print(f"-----------------{str(e)}-----------------")

else:
    TABLE_Foglalasok = TABLE_Foglalasok
    TABLE_LowPrio = TABLE_LowPrio
    TABLE_Foglalasok = TABLE_Foglalasok
    cursor = cursor