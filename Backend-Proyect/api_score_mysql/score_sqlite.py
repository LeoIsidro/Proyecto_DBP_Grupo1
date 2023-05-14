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

@app.route("/score" , methods=["POST"])
def score():
    conn = db_connection()
    cursor = conn.cursor()
    try:
        body = request.get_json()
        username=body["username"]
        points=body["points"]
        try:
            cursor.execute('SELECT user_username, points FROM Score WHERE user_username = ?', (username,))
            rows = cursor.fetchall()
        except Exception as e:
            return json.dumps({"success": False, "error": str(e)})

        if len(rows) == 0:
            cursor.execute('SELECT username FROM Usuario WHERE username = ?', (username,))
            rows = cursor.fetchall()
            if len(rows) != 0:
                cursor.execute('INSERT INTO Score (user_username, points) VALUES (?, ?)', (username, points))
                try:
                    conn.commit()
                except Exception as e:
                    return json.dumps({"success": False, "error": str(e)})
                return json.dumps({"success": True, "username": username})
            else:
                return json.dumps({"success": False, "user": "user not found"})
        else:
            if int(rows[0][1]) < int(points):
                cursor.execute('UPDATE Score SET points = ? WHERE user_username = ?', (points, username))
                try:
                    conn.commit()
                except Exception as e:
                    return json.dumps({"success": False, "error": str(e)})
                return json.dumps({"success": True, "msg":"update","username": username})
            else:
                return json.dumps({"success": True, "user": "score didn't increase"})
            
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})

              

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)