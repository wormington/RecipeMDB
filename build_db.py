import sqlite3 as sql
from pymongo import MongoClient
import csv
import os

# dbPath stores the file location of sqlite3's db file.
dbPath = './db/sql/recipe.db'

# csvPath stores the file location of the raw data file in csv format.
csvPath = './raw_data/raw-data_recipe.csv'

# Connection to MongoDB assumes that an instance of mongod is running on the localhost over the default port.
# To make moving the resulting database easier, mongod is set to use the path ./db/mongo as its primary folder.

# remove old sql db
if (os.path.exists('./db/sql/recipe.db')):
    print('Removing old SQLite database.')
    os.remove('./db/sql/recipe.db')

# connect to sql and create new db
sqlConn = sql.connect(dbPath)
cursor = sqlConn.cursor()

# connect to mongo

# remove old mongo db

# create new mongo db

# populate dbs
with open(csvPath, newline='') as csvFile:
    dictReader = csv.DictReader(csvFile)
    for line in dictReader:
        # add line to sql db
        # add line to mongo db
        break
    