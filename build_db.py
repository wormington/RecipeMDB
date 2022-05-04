import sqlite3 as sql
from pymongo import MongoClient
import csv
import os

# dbPath stores the file location of sqlite3's db file.
dbPath = './db/sql/recipe.db'

# These variables store the path location of the raw data files in csv format.
recipeMainPath = './raw_data/raw-data_recipe.csv'
recipeRatingsPath = './raw_data/raw-data_interaction.csv'

# Connection to MongoDB assumes that an instance of mongod is running on the localhost over the default port.
# To make moving the resulting database easier, mongod is set to use the path ./db/mongo as its primary folder.

# remove old sql db
if (os.path.exists('./db/sql/recipe.db')):
    print('Removing old SQLite database.')
    os.remove('./db/sql/recipe.db')

# connect to sql and create new db
sqlConn = None
try:
    sqlConn = sql.connect(dbPath)
except Exception as e:
    print('Error connecting to sql database: ' + e)
    quit()
else:
    print('Connection to SQLite successful. DB created.')

# create tables/collections
cursor = sqlConn.cursor()

createRecipeMain = """CREATE TABLE RecipeMain (
    recipe_id BLOB PRIMARY KEY,
    recipe_name TEXT NOT NULL,
    avg_rate REAL NOT NULL,
    num_review INTEGER NOT NULL,
    ingredients TEXT NOT NULL,
    directions TEXT NOT NULL,
    nutrition TEXT);"""

createRecipeRatings = """CREATE TABLE RecipeRatings (
    user_id BLOB,
    recipe_id BLOB,
    rate INTEGER NOT NULL,
    last_modified TEXT NOT NULL,
    PRIMARY KEY (user_id, recipe_id),
    FOREIGN KEY (recipe_id)
        REFERENCES RecipeMain (recipe_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE);"""

cursor.execute(createRecipeMain)
cursor.execute(createRecipeRatings)
cursor.commit()

print('SQL tables created successfully.')

# connect to mongo

# remove old mongo db

# create new mongo db

# populate RecipeMain table/collection
with open(recipeMainPath, newline='') as csvFile:
    dictReader = csv.DictReader(csvFile)
    for line in dictReader:
        # add line to sql db
        sqlInsert = f"""INSERT INTO RecipeMain (recipe_id, recipe_name, avg_rate, num_review, ingredients, directions, nutrition)
            VALUES ({line['recipe_id']}, {line['recipe_name']}, {line['aver_rate']}, {line['review_nums']}, 
                {line['ingredients']}, {line['cooking_directions']}, {line['nutritions']});"""
        cursor.execute(sqlInsert)
        sqlConn.commit()
        # add line to mongo db

print('RecipeMain SQL table and Mongo collection populated successfully.')
    
# populate RecipeRatings table/collection
with open(recipeRatingsPath, newline='') as csvFile:
    dictReader = csv.DictReader(csvFile)
    for line in dictReader:
        # add line to sql db
        sqlInsert = f"""INSERT INTO RecipeRatings (user_id, recipe_id, rate, last_modified)
            VALUES ({line['user_id']}, {line['recipe_id']}, {line['rating']}, {line['dateLastModified']});"""
        cursor.execute(sqlInsert)
        sqlConn.commit()
        # add line to mongo db

cursor.close()
sqlConn.close()
print('RecipeRatings SQL table and Mongo collection populated successfully.')