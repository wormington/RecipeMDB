# RecipeMDB
A repository for testing out MongoDB. Dataset will be a subset of recipes from [AllRecipes](https://www.allrecipes.com/).
The dataset is a bit large to send to Github, so I will provide a link to it. [Dataset](https://www.kaggle.com/code/yyzz1010/content-based-filtering-recipe-recommender/data)

The purpose of this project is to learn more about the usage and effectiveness of NoSQL (non-relational) databases as compared to SQL (relational) databases. I have previously learned about and used relational databases in college classes, but I was never taught anything about non-relational databases. A friend of mine who took the same relational database class suggested I try MongoDB, as he was quite pleased with its flexibility and ease of use. I plan to extend this README as I continue work on this project. 
---
## Update
After learning about MongoDB, there are a few different goals I want to accomplish for this project.

1. Create matching databases in SQLite and Mongo with our Recipe dataset. 
I will use Python with its PyMongo and sqlite3 modules to load the dataset into fresh databases for testing. This will be accomplished by a simple script. These databases will be the precursor to the following goals. In the future, I may switch SQLite with MySQL and check its performance. For now, SQLite will do the trick since the primary focus of this project is learning about MongoDB.

2. Run performance comparisons between the SQLite and Mongo databases.
A C# program will run equivalent queries on the databases and test their execution speed. It will perform multiple tests, each testing more complex queries, with and without indexes. To maintain fairness in the tests, the indexes used will also be equivalent. 

3. Create a GUI which allows the execution of custom queries on the databases.
Another C# program will show the data in the Mongo database. It will be extended to have a simple GUI which will work like the 'filter' function on many websites. It will take the filter settings and generate a query. This query - along with performance statistics pertaining to the query - will also be displayed in the GUI. For the GUI, I am planning on using Blazor from the ASP.NET library, as it will provide a GUI through the web browser which will work on most platforms.
