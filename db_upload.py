import pandas as pd
import random

def upload(mysql):
    df = pd.read_csv('export_250.csv')
    conn = mysql.connect()
    cursor = conn.cursor()
    for index , row in df.iterrows():
        print("dff")
        CompanyName = row['CompanyName'] if row['CompanyName'] else " "
        CompanyNumber = row['CompanyNumber'] if row['CompanyNumber']  and str(row['CompanyNumber']) != 'nan' else random.randint(0,300)
        CompanyStatusId = row['CompanyStatusId'] if row['CompanyStatusId'] and str(row['CompanyStatusId']) != 'nan' else random.randint(0,300)
        CompanyCategoryId = row['CompanyCategoryId'] if row['CompanyCategoryId'] and str(row['CompanyCategoryId']) != 'nan' else random.randint(0,300)
        BusinessActivityId = row['BusinessActivityId'] if row['BusinessActivityId'] and str(row['BusinessActivityId']) != 'nan' else random.randint(0,300)
        DistrictId = row['DistrictId'] if row['DistrictId'] and str(row['DistrictId']) != 'nan' else random.randint(0,300)
        IncorporationDate = row['IncorporationDate'] if row['IncorporationDate'] and str(row['IncorporationDate']) != 'nan' else ''
        CountryOfOriginId = row['CountryOfOriginId'] if row['CountryOfOriginId'] and str(row['CountryOfOriginId']) != 'nan' else random.randint(0,300)
        Exporter = row['Exporter'] if row['Exporter'] and str(row['Exporter']) != 'nan' else 0
        CompanySizeId = row['CompanySizeId'] if row['CompanySizeId'] and str(row['CompanySizeId']) != 'nan' else 0
        HasPatent = row['HasPatent'] if row['HasPatent'] and str(row['HasPatent']) != 'nan' else random.randint(0,1)
        HasGrant = row['HasGrant'] if row['HasGrant'] and str(row['HasGrant']) != 'nan' else random.randint(0,1)


        sql = f"""INSERT INTO UserInfo (CompanyName, CompanyNumber, CompanyStatusId, CompanyCategoryId, DistrictId, BusinessActivityId, IncorporationDate, CountryOfOriginId, CompanySizeId, Exporter, HasPatent,HasGrant) VALUES ('{CompanyName}',{CompanyNumber}, {CompanyStatusId}, {CompanyCategoryId}, {DistrictId}, {BusinessActivityId}, '{IncorporationDate}', {CountryOfOriginId}, {CompanySizeId}, {Exporter}, {HasPatent}, {HasGrant})"""
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            print(CompanyName)