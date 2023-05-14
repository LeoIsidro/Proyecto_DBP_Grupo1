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

@app.route("/login" , methods=["POST"])
def login():
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            body = request.get_json()
            username_user=body["username"] 
            password_user=body["password"]
            print(username_user)
            try:
                #user = Usuario.query.filter(Usuario.username == username).first()
                cursor.execute('SELECT username,password FROM Usuario WHERE username = %s', username_user)
                rows = cursor.fetchall()
                if rows[0][0] == None or password_user != rows[0][1]  or rows[0][1] == None or password_user==None or username_user==None:
                    return json.dumps({"success": False})
                else:
                    return json.dumps({"success": True, "username": username_user})
            except Exception as e:
                return json.dumps({"success": False, "error": str(e)})
            finally:
                cursor.close() 
                conn.close()
        except Exception as e:
            return json.dumps({"success": False, "error": str(e)})
               
              
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8002, debug=True)    