import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, request, jsonify,make_response
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from flaskext.mysql import MySQL
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields



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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rohit:Download#1@localhost:3306/banksearchbi'
db = SQLAlchemy(app)


###Models####
class Bankinfo(db.Model):
    __tablename__ = "bankinfo"

    id = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(255))
    CompanyNumber = db.Column(db.Integer)
    AddressCountry = db.Column(db.String(255))
    AddressCounty = db.Column(db.String(255))
    AddressTown = db.Column(db.String(255))
    AddressPostCode = db.Column(db.String(255))
    AddressLine1 = db.Column(db.String(255))
    CompanyStatusId = db.Column(db.Integer)
    AddressLine2 = db.Column(db.String(255))
    CompanyCategoryId = db.Column(db.Integer)
    CountryOfOriginId = db.Column(db.Integer)
    BusinessActivityId = db.Column(db.Integer)
    FullAddress = db.Column(db.String(500))
    ReportingDate = db.Column(db.Date)
    CashBankInHand = db.Column(db.Float)
    TotalAssets = db.Column(db.Float)
    FixedAssets = db.Column(db.Float)
    Liabilities = db.Column(db.Float)
    NetWorth= db.Column(db.Float)
    Creditors = db.Column(db.Float)
    Debtors = db.Column(db.Float)
    DistrictId = db.Column(db.Integer)
    IncorporationDate = db.Column(db.Date)
    HasAccountData = db.Column(db.Boolean)
    Exporter = db.Column(db.Float)
    DissolutionDate = db.Column(db.Float)
    CompanySizeId = db.Column(db.Float)
    HasPatent = db.Column(db.Boolean)
    HasGrant = db.Column(db.Boolean)
    AssetsLessCurrentLiabilities = db.Column(db.Float)
    Equity = db.Column(db.Float)
    AddressPostCodeValue = db.Column(db.String(250))


    def create(self):
      db.session.add(self)
      db.session.commit()
      return self

    def __repr__(self):
        return '' % self.id


#db.create_all()

class BankinfoSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Bankinfo
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    CompanyName = fields.String()
    CompanyNumber = fields.Number()
    AddressCountry = fields.String()
    AddressCounty = fields.String()
    AddressTown = fields.String()
    AddressPostCode = fields.String()
    AddressLine1 = fields.String()
    CompanyStatusId = fields.Number()
    AddressLine2 = fields.String()
    CompanyCategoryId = fields.Number()
    CountryOfOriginId = fields.Number()
    BusinessActivityId = fields.Number()
    FullAddress = fields.String()
    ReportingDate = fields.Date()
    CashBankInHand = fields.Float()
    TotalAssets = fields.Float()
    FixedAssets = fields.Float()
    Liabilities = fields.Float()
    NetWorth= fields.Float()
    Creditors = fields.Float()
    Debtors = fields.Float()
    DistrictId = fields.Number()
    IncorporationDate =  fields.Date()
    HasAccountData = fields.Boolean()
    Exporter = fields.Float()
    DissolutionDate = fields.Float()
    CompanySizeId = fields.Float()
    HasPatent = fields.Boolean()
    HasGrant = fields.Boolean()
    AssetsLessCurrentLiabilities = fields.Float()
    Equity = fields.Float()
    AddressPostCodeValue = fields.String()




# app.config['MYSQL_DATABASE_USER'] = "rohit"
# app.config['MYSQL_DATABASE_PASSWORD'] = "Download@1"
# app.config['MYSQL_DATABASE_DB'] = "banksearchbi"
# app.config['MYSQL_DATABASE_HOST'] = "localhost"
# mysql = MySQL()
# #Initialize the MySQL extension
# mysql.init_app(app)

# API VIEWS 

class CompanyList(Resource):

    def get(self):
        page = int(request.args.get('offset',10))
        per_page = int(request.args.get('limit',200))
        if len(request.args.keys()) < 3:
            bankList = Bankinfo.query.paginate(page,per_page,error_out=False).items
        else:
            str = ''
            first = True
            for key, val in request.args.items():
                if val and key not in ['limit','offset']:

                    if not first:
                        str+=", "
                    else:
                        first =False

                    if key in ['CompanyName', 'IncorporationDate']:
                        str+=f"Bankinfo.{key} == '{val}'"
                    else:
                        str+=f"Bankinfo.{key} == {val}"
            query = f'Bankinfo.query.filter({str}).paginate({page},{per_page},error_out=False).items'
            bankList = eval(query)

        bank_schema = BankinfoSchema(many=True)
        banks = bank_schema.dump(bankList)
        return make_response(jsonify({"bankinfo": banks}))


class Company(Resource):

    def get(self, comp_id):
        bank = Bankinfo.query.get(comp_id)
        bank_schema = BankinfoSchema()
        banks = bank_schema.dump(bank)
        return make_response(jsonify({"bankinfo": banks}))


api.add_resource(CompanyList, '/api/company/', endpoint='companies')
api.add_resource(Company, '/api/company/<int:comp_id>/', endpoint='company')

if __name__ == "__main__":
    app.run(debug=True)
