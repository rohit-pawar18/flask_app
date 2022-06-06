from ctypes.wintypes import INT
from sqlalchemy import BOOLEAN, FLOAT, TEXT
import mysql.connector
username = "banksearchbi-dash"

password = "secure123QAZ"

server = "banksearchdbserver.database.windows.net"

database = "banksearchbi"

print("dfdsf")
mydb = mysql.connector.connect(
  host=server,
  user=username,
  password=password
)


CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

CREATE TABLE UserInfo (
CompanyName VARCHAR(255),
CompanyNumber INT,
AddressCountry VARCHAR(255),
AddressCounty VARCHAR(255),
AddressTown VARCHAR(255),
AddressPostCode VARCHAR(255),
AddressLine1 VARCHAR(255),
CompanyStatusId INT,
AddressLine2 VARCHAR(255),
CompanyCategoryId INT,
CountryOfOriginId INT,
BusinessActivityId INT,
FullAddress TEXT,
ReportingDate DATETIME,
CashBankInHand FLOAT,
TotalAssets FLOAT,
FixedAssets FLOAT,
Liabilities FLOAT,
NetWorth FLOAT,
Creditors FLOAT,
Debtors FLOAT,
DistrictId INT,
IncorporationDate DATE,
HasAccountData BOOLEAN,
Exporter FLOAT,
DissolutionDate DATE,
CompanySizeId INT,
HasPatent BOOLEAN,
HasGrant BOOLEAN,
AssetsLessCurrentLiabilities FLOAT,
Equity FLOAT,
AddressPostCodeValue VARCHAR(255));



CREATE USER 'rohit'@'localhost' IDENTIFIED BY 'Download@1';

GRANT PRIVILEGE ON *.* TO 'rohit'@'host';

GRANT ALL PRIVILEGES ON *.* TO 'rohit'@'localhost' WITH GRANT OPTION;

CompanyName,CompanyNumber, AddressCountry, AddressCounty, AddressTown,	AddressPostCode, AddressLine1,	AddressLine2,	CompanyStatusId	CompanyCategoryId	CountryOfOriginId	BusinessActivityId	FullAddress	ReportingDate	CashBankInHand	TotalAssets	FixedAssets	Liabilities	NetWorth	Creditors	Debtors	DistrictId	IncorporationDate	HasAccountData	Exporter	DissolutionDate	CompanySizeId	HasPatent	HasGrant	AssetsLessCurrentLiabilities	Equity	AddressPostCodeValue

INSERT INTO table_name ()


LOAD DATA INFILE '/var/lib/mysql-files/export_250.csv'
INTO TABLE UserInfo
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'c:/tmp/discounts.csv' 
INTO TABLE discounts 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA INFILE '/var/lib/mysql-files/export_250.csv'
INTO TABLE UserInfo
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;


ALTER TABLE UserInfo MODIFY CompanyStatusId BIGINT;


CompanyName, CompanyNumber, CompanyStatusId, CompanyCategoryId, DistrictId, CompanyCategoryId, BusinessActivityId, IncorporationDate, CountryOfOriginId, CompanySizeId, Exporter, HasPatent,HasGrant


