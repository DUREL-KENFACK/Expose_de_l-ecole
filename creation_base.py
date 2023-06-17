import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    # database="test"
    )
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE test")

# mycursor.execute("CREATE TABLE patient (id int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(20) NOT NULL, prenom VARCHAR(20) NOT NULL, sexe VARCHAR(20) NOT NULL, tel VARCHAR(20) NOT NULL, date VARCHAR(10) NOT NULL, age INT(6) NOT NULL)")
