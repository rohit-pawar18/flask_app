from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

import pandas as pd


#username = "banksearchbi-dash"
username = "rohit"

#password = "secure123QAZ"
password = "Download@1"

#server = "banksearchdbserver.database.windows.net"
server = "localhost"

database = "banksearchbi"


#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = username
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = database
app.config['MYSQL_DATABASE_HOST'] = server

#Initialize the MySQL extension
mysql.init_app(app)

conn = mysql.connect()

class UserList(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from otg_demo_users""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = request.form['name']
            _age = request.form['age']
            _city = request.form['city']
            insert_user_cmd = """INSERT INTO otg_demo_users(name, age, city) 
                                VALUES(%s, %s, %s)"""
            cursor.execute(insert_user_cmd, (_name, _age, _city))
            conn.commit()
            response = jsonify(message='User added successfully.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add user.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)