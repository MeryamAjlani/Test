import sqlite3


def create_db():
    connection = sqlite3.connect('../data.db')
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS User")
    cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
    cur.execute(
        "CREATE TABLE User (ID INTEGER PRIMARY KEY, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL);")
    cur.execute(
        "INSERT INTO User (USERNAME,PASSWORD) VALUES ('admin','admin'),('root','root'),('Meryam','ajlani');")
    cur.execute(
        "CREATE TABLE EMPLOYEE (ID INTEGER PRIMARY KEY, NAME TEXT NOT NULL, EMAIL TEXT NOT NULL,PHONE TEXT INT NOT NULL);")
    cur.execute(
        "INSERT INTO EMPLOYEE (NAME,EMAIL,PHONE) VALUES ('mahdi','mahdi@gmail.com','88888888'),('mathis','mathis@gmail.com','88888888'),('joran','joran@gmail.com','88888888'),('paul','paul@gmail.com','88888888'),('paul','paul@gmail.com','88888888');")
    connection.commit()
    print("Done")
    connection.close()


create_db()