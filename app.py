from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from flaskext.mysql import MySQL
from flask_api import status
from db import DB
app = Flask(__name__)

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

#Create an instance of Flask
app = Flask(__name__)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


api = Api(app)
app.config['MYSQL_DATABASE_USER'] = "rohit"
app.config['MYSQL_DATABASE_PASSWORD'] = "Download@1"
app.config['MYSQL_DATABASE_DB'] = "banksearchbi"
app.config['MYSQL_DATABASE_HOST'] = "localhost"
mysql = MySQL()
#Initialize the MySQL extension
mysql.init_app(app)

# API VIEWS 

class CompanyList(Resource):

    def get(self):
        db = DB(mysql)
        response = db.getCompanyList(request)
        return jsonify(response), status.HTTP_200_OK

class Company(Resource):

    def get(self, comp_id):
        db = DB(mysql)
        response = db.get(comp_id)
        return jsonify(response)

api.add_resource(CompanyList, '/api/company/', endpoint='companies')
api.add_resource(Company, '/api/company/<int:comp_id>/', endpoint='company')

if __name__ == "__main__":
    app.run(debug=True)
