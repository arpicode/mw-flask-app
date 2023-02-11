import mariadb
import os


class DataBase():
    Credentials = dict[str, str | int | None]

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.config: DataBase.Credentials = {
            'host': os.getenv('DB_HOST'),
            'port': int(str(os.getenv('DB_PORT'))),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'database': os.getenv('DB_NAME')
        }

    def connect(self):
        self.connection = mariadb.connect(**self.config)
        if (self.connection is not None):
            self.cursor = self.connection.cursor()
        else:
            print("Error: Couldn't connect to database.")

    def query(self, sql: str, params: tuple):
        result = None

        if (self.connection is not None and self.cursor is not None):
            result = self.cursor.execute(sql, params)
            self.connection.commit()
        else:
            print("Error: Not connected to database.")

        return result

    def close(self):
        if (self.connection is not None and self.cursor is not None):
            self.cursor.close()
            self.connection.close()
        else:
            print("Error: No database connection.")
