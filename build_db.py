import sqlite3 as sql
import pymongo as mongo
import csv
import os

# dbPath stores the file location of sqlite3's db file.
dbPath = './db/sql/Recipe.db'

# These variables store the path location of the raw data files in csv format.
recipeMainPath = './raw_data/raw-data_recipe.csv'
recipeRatingsPath = './raw_data/raw-data_interaction.csv'

# Connection to MongoDB assumes that an instance of mongod is running on the localhost over the default port.
# To make moving the resulting database easier, mongod is set to use the path ./db/mongo as its primary folder.

# remove old sql db
if (os.path.exists(dbPath)):
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

# create tables
cursor = sqlConn.cursor()

createRecipeMain = """CREATE TABLE RecipeMain (
    recipe_id INTEGER PRIMARY KEY,
    recipe_name TEXT NOT NULL,
    avg_rate REAL NOT NULL,
    num_review INTEGER NOT NULL,
    ingredients TEXT NOT NULL,
    directions TEXT NOT NULL,
    nutrition TEXT);"""

createRecipeRatings = """CREATE TABLE RecipeRatings (
    user_id INTEGER,
    recipe_id INTEGER,
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
mongoConn = mongo.MongoClient()

# remove old mongo collections, if they exist
if ('Recipe' in mongoConn.list_database_names()):
    if ('RecipeMain' in mongoConn.Recipe.list_collection_names()):
        mongoConn.Recipe.RecipeMain.drop()
    
    if ('RecipeRatings' in mongoConn.Recipe.list_collection_names()):
        mongoConn.Recipe.RecipeRatings.drop()

# create new mongo db
mongoRecipeMain = mongoConn.Recipe.RecipeMain
mongoRecipeRatings = mongoConn.Recipe.RecipeRatings

# populate RecipeMain table/collection
with open(recipeMainPath, newline='') as csvFile:
    dictReader = csv.DictReader(csvFile)
    for line in dictReader:
        # add line to sql db
        sqlInsert = f"""INSERT INTO RecipeMain (recipe_id, recipe_name, avg_rate, num_review, ingredients, directions, nutrition)
            VALUES ({int(line['recipe_id'])}, {line['recipe_name']}, {float(line['aver_rate'])}, {int(line['review_nums'])}, 
                {line['ingredients']}, {line['cooking_directions']}, {line['nutritions']});"""
        cursor.execute(sqlInsert)
        sqlConn.commit()

        # add line to mongo db
        mongoInsert = {
            'recipe_id': int(line['recipe_id']),
            'recipe_name': line['recipe_name'],
            'avg_rate': float(line['aver_rate']),
            'num_review': int(line['review_nums']),
            'ingredients': line['ingredients'],
            'directions': line['cooking_directions'],
            'nutrition': line['nutritions']
        }
        mongoRecipeMain.insert_one(mongoInsert)

print('RecipeMain SQL table and Mongo collection populated successfully.')
    
# populate RecipeRatings table/collection
with open(recipeRatingsPath, newline='') as csvFile:
    dictReader = csv.DictReader(csvFile)
    for line in dictReader:
        # add line to sql db
        sqlInsert = f"""INSERT INTO RecipeRatings (user_id, recipe_id, rate, last_modified)
            VALUES ({int(line['user_id'])}, {int(line['recipe_id'])}, {int(line['rating'])}, {line['dateLastModified']});"""
        cursor.execute(sqlInsert)
        sqlConn.commit()

        # add line to mongo db
        mongoInsert = {
            'user_id': int(line['user_id']),
            'recipe_id': int(line['recipe_id']),
            'rating': int(line['rating']),
            'last_modified': line['dateLastModified']
        }
        mongoRecipeMain.insert_one(mongoInsert)

# close connections after finished
cursor.close()
sqlConn.close()
mongoConn.close()
print('RecipeRatings SQL table and Mongo collection populated successfully.')