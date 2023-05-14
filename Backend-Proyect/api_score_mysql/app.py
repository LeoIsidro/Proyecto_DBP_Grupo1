from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_cors import CORS
import json

#Create an instance of Flask
app = Flask(__name__)

CORS(app)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'bd_api'
app.config['MYSQL_DATABASE_HOST'] = '44.194.187.135'
app.config['MYSQL_DATABASE_PORT'] = 8005 


#Initialize the MySQL extension
mysql.init_app(app)

@app.route("/score" , methods=["POST"])
def score():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        body = request.get_json()
        username=body["username"]
        points=body["points"]
        try:
            cursor.execute('SELECT user_username, points FROM Score WHERE user_username = %s', username)
            rows = cursor.fetchall()
        except Exception as e:
            return json.dumps({"success": False, "error": str(e)})

        if len(rows) == 0:
            cursor.execute('SELECT username FROM Usuario WHERE username = %s', username)
            rows = cursor.fetchall()
            if len(rows) != 0:
                cursor.execute('INSERT INTO Score (user_username, points) VALUES (%s, %s)', (username, points))
                try:
                    conn.commit()
                except Exception as e:
                    return json.dumps({"success": False, "error": str(e)})
                return json.dumps({"success": True, "username": username})
            else:
                return json.dumps({"success": False, "error": "Username does not exist"})
        else:
            if int(rows[0][1]) < int(points):
                cursor.execute('UPDATE Score SET points = %s WHERE user_username = %s', (points, username))
                try:
                    conn.commit()
                except Exception as e:
                    return json.dumps({"success": False, "error": str(e)})
                finally:
                    cursor.close() 
                    conn.close()
                return json.dumps({"success": True, "username": username})
            else:
                return json.dumps({"success": False, "error": "Points are not higher than the current score"})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004, debug=True)    

