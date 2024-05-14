import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)
    
    def create_table_lesson(self):
        sql = """
        CREATE TABLE Lessons (
            id varchar(255) NOT NULL,
            videoId varchar(255),
            CountOfLesson varchar(255),
            info varchar(255),
            youtube varchar(255),
            telegram varchar(255),
            category varchar(255),
            subcategory varchar(255),
            PRIMARY KEY (id)
            );"""
        
        self.execute(sql , commit=True)
    
    # Category jadvali
    def create_table_category(self):
        sql = """
        CREATE TABLE Category (
            id varchar(255) NOT NULL,
            name varchar(255),
            PRIMARY KEY (id)

            );
        """
        self.execute(sql , commit=True)

    # SubCategory jadvali
    def create_table_subcategory(self):
        sql = """
        CREATE TABLE SubCategory (
            id varchar(255) NOT NULL,
            name varchar(255),
            category varchar(255),
            PRIMARY KEY (id)

            );"""
        self.execute(sql , commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    # dars qo'shish
    def add_lesson(self, id: str, videoId:str , CountOfLesson: str, info: str , youtube: str , telegram: str , category:str , subcategory: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Lessons(id, CountOfLesson, videoId, info, youtube , telegram , category , subcategory) VALUES(?, ?,? , ?, ? ,? ,? ,?)
        """

        self.execute(sql, parameters=(id, videoId, CountOfLesson, info, youtube , telegram , category , subcategory), commit=True)
    #  category qo'shish
    def add_category(self, id: str, name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Category(id, name) VALUES(?, ?)
        """

        self.execute(sql, parameters=(id, name), commit=True)
    
    # subcategory qo'shish
    def add_subcategory(self, id: str, name: str, category):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO SubCategory(id, name, category) VALUES(?, ?, ?)
        """

        self.execute(sql, parameters=(id, name, category), commit=True)
    
    
    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)
    # category barchasini tanlash
    
    def select_all_Categorys(self):
        sql = """
        SELECT * FROM Category
        """
        return self.execute(sql, fetchall=True)
    
    def select_all_SubCategorys(self):
        sql = f"SELECT * FROM SubCategory"
        return self.execute(sql, fetchall=True)

    
    
    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    # select category
    
    
    def select_category(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Category WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    
    # def select_Subcategory(self, category):
    #     # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
    #     sql = f"SELECT * FROM SubCategory WHERE category={category} "

    #     return self.execute(sql,  fetchone=True)
     
    def select_Subcategory(self, category):
        sql = "SELECT * FROM SubCategory WHERE category = ?"
        parameters = (category,)  # Tuple with one element, the category value

        return self.execute(sql, parameters, fetchall=True)


    def select_lesson(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Lessons WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    
    
    def select_all_lesson(self):
        return self.execute("SELECT DISTINCT CountOfLesson FROM Lessons",fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
    def delete_one_category(self , name):

        self.execute(f"DELETE FROM Category WHERE name='{name}'", commit=True)
    
    def delete_table_lesson(self):
        self.execute("DROP TABLE Lessons" , commit=True)

    def delete_Subcategory_lesson(self):
        self.execute("DROP TABLE SubCategory" , commit=True)

    def delete_Category_lesson(self):
        self.execute("DROP TABLE Category" , commit=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
