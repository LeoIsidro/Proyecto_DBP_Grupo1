from flask import Flask, jsonify, request
#from flaskext.mysql import MySQL
#from flask_restful import Resource, Api
import json
import sqlite3
from flask_cors import CORS

#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
#db = MySQL()

#Create an instance of Flask RESTful API
#api = Api(app)

CORS(app)

def db_connection():
	conn = None
	try:
		conn = sqlite3.connect('game.sqlite')
	except sqlite3.error as e:
		print(e)
	return conn

"""
#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'bd_api'
app.config['MYSQL_DATABASE_HOST'] = '3.231.7.144'
app.config['MYSQL_DATABASE_PORT'] = 8005 
"""

#Initialize the MySQL extension
#db.init_app(app)

@app.route("/register" , methods=["POST"])
def register():
    conn = db_connection()
    cursor = conn.cursor()
    try:
        body = request.get_json()
        username_user=body["username"] 
        password_user=body["password"]
        age_user=body["age"]
        email_user=body["email"]
        try:
            #user = Usuario.query.filter(Usuario.username == username).first()
            cursor.execute('SELECT username FROM Usuario WHERE username = ?', (username_user,))
            rows_1= cursor.fetchall()
            cursor.execute('SELECT email FROM Usuario WHERE email = ?', (email_user,))
            rows_2= cursor.fetchall()
        except Exception as e:
                return json.dumps({"success": False, "error": str(e)})
        if len(rows_1) != 0:
            return "Username already exists"
        if len(rows_1) != 0:
            print(rows_2)
            return "Email already exists"

        cursor.execute('INSERT INTO Usuario (username, password, age, email) VALUES (?, ?, ?, ?)', (username_user, password_user, age_user, email_user))

        try:
            conn.commit()
        except:
            return json.dumps({"success": False, "username": username_user})
        finally:
            cursor.close() 
            conn.close()

        print(body)
        return json.dumps({"success": True, "username": username_user})
    except Exception as e:
            return json.dumps({"success": False, "error": str(e)})

              

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)