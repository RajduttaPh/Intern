from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)

# MySQL configurations
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="codexp"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM codexptable")
    users = cursor.fetchall()
    cursor.close()
    print(users)
    return jsonify({"result":users})

if __name__ == '__main__':
    app.run(debug=True)
