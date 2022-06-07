from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
#from routes import request_api

# sweger setup 
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Company"
    }
)
#import pandas as pd

#username = "banksearchbi-dash"
username = "rohit"

#password = "secure123QAZ"
password = "Download@1"

#server = "banksearchdbserver.database.windows.net"
server = "localhost"

database = "banksearchbi"


#Create an instance of Flask
app = Flask(__name__)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
#app.register_blueprint(request_api.get_blueprint())

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
conn = ''#mysql.connect()

class CompanyList(Resource):
    def get(self):
        offset = request.args.get('offset', 10)
        limit = request.args.get('limit', 10)
        str = ''
        first = True
        for key, val in request.args.items():
            if val and key not in ['limit','offset']:
                if first == False:
                    str+=" AND "
                else:
                    first =False
                if key in ['CompanyName', 'IncorporationDate']:
                    str+=f"{key}='{val}'"
                else:
                    str+=f"{key}={val}"
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(f"""select * from UserInfo where {str} LIMIT {offset}, {limit};""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

class Company(Resource):
    def get(self, comp_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from UserInfo where id = %s',comp_id)
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


api.add_resource(CompanyList, '/api/company/', endpoint='companies')
api.add_resource(Company, '/api/company/<int:comp_id>/', endpoint='company')

if __name__ == "__main__":
    app.run(debug=True)
