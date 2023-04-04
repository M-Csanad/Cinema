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
        "CREATE DATABASE IF NOT EXISTS `cinema` CHARACTER SET utf8mb4 COLLATE utf8mb4_hungarian_ci")

    TABLE_LowPrio = ('''CREATE TABLE IF NOT EXISTS Low_Prio (
    LP_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    EV CHAR(4) NOT NULL,
    CATEGORY VARCHAR(50) NOT NULL,
    PLAYTIME CHAR(3) NOT NULL,
    MAXHELY CHAR(3) NOT NULL)''')
    
    cursor.execute(TABLE_LowPrio)
    
    TABLE_Termek = ('''CREATE TABLE IF NOT EXISTS Termek (
    TEREM_SZAM CHAR(2) NOT NULL PRIMARY KEY,
    TEREM_FILM TEXT(50) NOT NULL,
    TEREM_MAXHELY CHAR(3) NOT NULL, 
    LOW_PRIO INT NOT NULL,  
    FOREIGN KEY (LOW_PRIO) REFERENCES Low_Prio(LP_ID))''')  # Amikor egy TABLE-t szeretnénk létrehozni, az adattípust kötelező megadni a hosszával együtt!!

    cursor.execute(TABLE_Termek)

    TABLE_Foglalasok = ('''CREATE TABLE IF NOT EXISTS Foglalasok (
    FOGLAL_SORSZAM CHAR(12) NOT NULL PRIMARY KEY,
    KERESZTNEV TEXT(25) NOT NULL,
    VEZETEKNEV TEXT(25) NOT NULL,
    SZEKSZAM VARCHAR(50) NOT NULL,
    TEREMSZAM CHAR(2) NOT NULL,
    
    FOREIGN KEY (TEREMSZAM) REFERENCES Termek(TEREM_SZAM))''')
    cursor.execute(TABLE_Foglalasok)

    

    INSERT_Termek = ("INSERT `Termek` (`TEREM_SZAM`, `TEREM_FILM`, `LOW_PRIO`, `TEREM_MAXHELY`) VALUES (%d,%s,%d,%d)",(1, 'John Wick: 4. felvonás',  250),(2, 'Super Mario Bros.: A film',  150),(3, 'Avatar',  150),(4, 'A galaxis őrzői: 3. rész', '120perc', 250),(5, 'A bálna',  100),(6, 'Dungeons and Dragons: Betyárbecsület', 250))
        
    cursor.execute(INSERT_Termek)


except Exception as e:
    print(f"-----------------{str(e)}-----------------")
    
"""INSERT `Termek` (`TEREM_SZAM`, `TEREM_FILM`, `LOW_PRIO`, `TEREM_MAXHELY`) VALUES (%d,%s,%d,%d)",(1, 'John Wick: 4. felvonás', 'd', 250),(2, 'Super Mario Bros.: A film', '', 150),(3, 'Avatar', '2022;(Fantasy;Sci-Fi;Akció);192perc', 150),(4, 'A galaxis őrzői: 3. rész', '2023;(Akció;Kalandfilm;Vígjáték;Sci-Fi);120perc', 250),(5, 'A bálna', '2023;(Dráma);117perc', 100),(6, 'Dungeons and Dragons: Betyárbecsület', '2023;(Akció;Kalandfilm);134perc', 250))"""