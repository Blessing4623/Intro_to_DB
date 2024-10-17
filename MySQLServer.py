import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Baldwin90#"
)
mycursor = mydb.cursor()
try:
    query = "CREATE DATABASE alx_book_store"
    mycursor.execute(query)
    print("Database 'alx_book_store' created successfully!")
except mysqql.connector.Error as e:
    print(f"Error creating database as {e}")