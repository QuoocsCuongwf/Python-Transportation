import pyodbc

DRIVER = 'ODBC Driver 17 for SQL Server'
SERVER = 'localhost,1433'  # Địa chỉ IP của container Docker và cổng đã ánh xạ
DATABASE = 'management_stransparttions'
USERNAME = 'sa'
PASSWORD = 'Admin123@'

connect_string = f"""
    DRIVER={{{DRIVER}}};
    SERVER={SERVER};
    DATABASE={DATABASE};
    UID={USERNAME};
    PWD={PASSWORD};
    Connection Timeout=30
"""

class Database:
    def __init__(self):
        try:
            self.connection = pyodbc.connect(connect_string)
            self.cursor = self.connection.cursor()
            print("Connection successful")
        except pyodbc.Error as e:
            print(f"Database connection failed: {e}")

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

# Tạo đối tượng Database và kiểm tra kết nối
db = Database()

#create table
db.insert("""
        CREATE TABLE students (
            id INT PRIMARY KEY,
            name NVARCHAR(50),
            age INT,
            address NVARCHAR(255)
        )
    """)
