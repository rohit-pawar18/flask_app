
class DB(object):

    def __init__(self, mysql) -> None:
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor()

    def get(self, comp_id):

        try:
            self.cursor.execute(f'select * from UserInfo where id = {comp_id}')
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
     

    
    def getCompanyList(self, request):

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
            self.cursor.execute(f"""select * from UserInfo where {str} LIMIT {offset}, {limit};""")
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
       

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
