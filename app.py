from flask import Flask
import pymysql

app = Flask(__name__)

connection = pymysql.connect(host="db", user="root", password="root",
                             db="course", port=3307, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def hello_world():
    # Creating a connection cursor
    cursor = connection.cursor()
    # Executing SQL Statements
    cursor.execute(''' SELECT * FROM course_users ''')
    course_users = cursor.fetchall()
    # Closing the cursor
    cursor.close()
    print(str(course_users))
    return str(course_users)
