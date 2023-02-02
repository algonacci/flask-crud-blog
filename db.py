import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="php-crud-blog"
)

cursor = db.cursor()
