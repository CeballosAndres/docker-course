from flask import Flask, jsonify
import pymysql

application = app = Flask(__name__)


def get_connection():
    connection = pymysql.connect(host="mysql-db", user="root", password="root",
                                 db="course", port=3306, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return connection


@app.route('/', methods=["GET"])
def index():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM curse_users")
    data = cur.fetchall()
    cur.close()
    con.close()
    return jsonify(data), 200


if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)