namespace RecipeMDB {
    using System;
    using System.Data.SQLite;
    using MongoDB.Driver;
    using MongoDB.Bson;
    /*
        TODO: a lot. 
        1) make methods to easily query each database and return results.
        2) write tests for the databases, measure performance in ms.
        3) write code for gui queries. (different file?)
    */
    public class MongoInst {

        private MongoClient mongoConn;

        public MongoInst() {
            mongoConn = new MongoClient();
        }

        public bool ExecuteQuery(BsonDocument a) {
            // todo
            return true;
        }

    }

    public class SQLiteInst {

        private SQLiteConnection sqlConn;

        public SQLiteInst(string dbPath) {
            sqlConn = new SQLiteConnection("Data Source=" + dbPath);
            sqlConn.Open();
        }


        public bool ExecuteQuery(string queryString) {
            // todo
            return true;
        }

        ~SQLiteInst() {
            sqlConn.Close();
        }
    }


    internal class Tests {

        // Test 1: single field equality query
        static string Test1(MongoInst mon, SQLiteInst sql) {
            // Get all ratings of 1 for all recipes.
            string sqlQuery = "SELECT * FROM RecipeRatings WHERE rate = 1;";
            BsonDocument mongoQuery = null; // todo

            long sqlStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sql query
            long sqlDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - sqlStart;

            long mongoStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sync mongo query
            long mongoDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - mongoStart;

            return $"Test 1:\n\t SQL Query Time = {sqlDiff}\n\tMongoDB Query Time = {mongoDiff}";
        }

        // Test 2: single field range query
        static string Test2(MongoInst mon, SQLiteInst sql) {
            // Get all recipes with an average rating between 4 and 5.
            string sqlQuery = "SELECT * FROM RecipeMain WHERE avg_rate >= 4 AND avg_rate <= 5;";
            BsonDocument mongoQuery = null; // todo

            long sqlStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sql query
            long sqlDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - sqlStart;

            long mongoStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sync mongo query
            long mongoDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - mongoStart;

            return $"Test 1:\n\t SQL Query Time = {sqlDiff}\n\tMongoDB Query Time = {mongoDiff}";
        }

        // Test 3: text field query
        static string Test3(MongoInst mon, SQLiteInst sql) {
            // Get all recipes where the recipe_name contains the word 'chicken'.
            string sqlQuery = "SELECT * FROM RecipeMain WHERE recipe_name LIKE '%chicken%';";
            BsonDocument mongoQuery = null; // todo

            long sqlStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sql query
            long sqlDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - sqlStart;

            long mongoStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sync mongo query
            long mongoDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - mongoStart;

            return $"Test 1:\n\t SQL Query Time = {sqlDiff}\n\tMongoDB Query Time = {mongoDiff}";
        }

        // Test 4: multi-field range query
        static string Test4(MongoInst mon, SQLiteInst sql) {
            // Get all recipes with at least an avg_rate of 4 and at least 100 reviews.
            string sqlQuery = "SELECT * FROM RecipeMain WHERE rate >=4 AND num_review >= 100;";
            BsonDocument mongoQuery = null; // todo

            long sqlStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sql query
            long sqlDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - sqlStart;

            long mongoStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sync mongo query
            long mongoDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - mongoStart;

            return $"Test 1:\n\t SQL Query Time = {sqlDiff}\n\tMongoDB Query Time = {mongoDiff}";
        }

        // Test 5: cross-table/cross-collection equality query
        static string Test5(MongoInst mon, SQLiteInst sql) {
            // Get all reviews with a rating of 4 for all recipes.
            string sqlQuery = "SELECT * FROM RecipeMain INNER JOIN RecipeRatings WHERE RecipeRatings.rate = 4;";
            BsonDocument mongoQuery = null; // todo

            long sqlStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sql query
            long sqlDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - sqlStart;

            long mongoStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sync mongo query
            long mongoDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - mongoStart;

            return $"Test 1:\n\t SQL Query Time = {sqlDiff}\n\tMongoDB Query Time = {mongoDiff}";
        }

        // Test 6: cross-table/cross-collection range query
        static string Test6(MongoInst mon, SQLiteInst sql) {
            // Get all recipes with at more than 100 reviews.
            string sqlQuery = "SELECT * FROM RecipeMain INNER JOIN RecipeRatings WHERE RecipeMain.num_review > 100";
            BsonDocument mongoQuery = null; // todo

            long sqlStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sql query
            long sqlDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - sqlStart;

            long mongoStart = DateTimeOffset.Now.ToUnixTimeMilliseconds();
            // execute sync mongo query
            long mongoDiff = DateTimeOffset.Now.ToUnixTimeMilliseconds() - mongoStart;

            return $"Test 1:\n\t SQL Query Time = {sqlDiff}\n\tMongoDB Query Time = {mongoDiff}";
        }

        static void Main(string[] args) {
            MongoInst mon = new MongoInst();
            SQLiteInst sql = new SQLiteInst("./../db/sql/Recipe.db");
 
            // Test 1
            Console.WriteLine(Test1(mon, sql));
            // Test 2
            Console.WriteLine(Test2(mon, sql));
            // Test 3
            Console.WriteLine(Test3(mon, sql));
            // Test 4
            Console.WriteLine(Test4(mon, sql));
            // Test 5
            Console.WriteLine(Test5(mon, sql));
            // Test 6
            Console.WriteLine(Test6(mon, sql));
        }
    }
}
