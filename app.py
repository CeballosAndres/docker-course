from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'course'
 
mysql = MySQL(app)



@app.route('/')
def hello_world():
    #Creating a connection cursor
    cursor = mysql.connection.cursor()
    #Executing SQL Statements
    cursor.execute(''' SELECT * FROM course_users ''')
    course_users = cursor.fetchall()
    #Closing the cursor
    cursor.close()
    print(str(course_users))
    return str(course_users)