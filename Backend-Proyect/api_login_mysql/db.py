import sqlite3
#create db connection
conn = sqlite3.connect("game.sqlite")
#create the db cursor object
cursor = conn.cursor()
#create sql table creation query
sql_query_1 = """ CREATE TABLE Usuario (
	id INTEGER PRIMARY KEY,
	username TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)"""
cursor.execute(sql_query_1)
conn.commit()

sql_query_2 = """ CREATE TABLE Score (
    id INTEGER PRIMARY KEY,
    user_username TEXT NOT NULL,
    points INTEGER NOT NULL,
    FOREIGN KEY (user_username) REFERENCES Usuario (username));
"""
cursor.execute(sql_query_2)
conn.commit()

sql_query_3 =""" INSERT INTO Usuario (username, age, email, password) VALUES ('jose', 20, 'josesito2023@utec.edu.pe', '1234')"""

cursor.execute(sql_query_3)
conn.commit()