from passlib.hash import sha256_crypt

from flask_app.classes.RegisterForm import RegisterForm
from ..DataBase import DataBase


class User():
    @staticmethod
    def insert_user(form: RegisterForm):
        name = str(form.name.data)
        email = str(form.email.data)
        username = str(form.username.data)
        password = sha256_crypt.encrypt(str(form.password.data))

        db = DataBase()
        db.connect()
        sql = "INSERT INTO users (name, email, username, password) VALUES(?, ?, ?, ?);"
        params = (name, email, username, password)
        db.query(sql=sql, params=params)
        db.close()

    @staticmethod
    def get_user_by_username(username: str):
        db = DataBase()
        db.connect()
        sql = "SELECT * FROM users WHERE username = ?;"
        params = [username]
        record = None
        if db.cursor is not None:
            db.cursor.execute(sql, params)
            record = db.cursor.fetchone()
        db.close()

        return record

# def getAllRows():
#     try:
#         connection = sqlite3.connect('SQLite_Python.db')
#         cursor = connection.cursor()
#         print("Connected to SQLite")

#         sqlite_select_query = """SELECT * from database_developers"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Total rows are:  ", len(records))
#         print("Printing each row")
#         for row in records:
#             print("Id: ", row[0])
#             print("Name: ", row[1])
#             print("Email: ", row[2])
#             print("Salary: ", row[3])
#             print("\n")

#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read data from table", error)
#     finally:
#         if connection:
#             connection.close()
#             print("The Sqlite connection is closed")
