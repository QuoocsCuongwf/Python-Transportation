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

create_table="""

CREATE TABLE ChuXe (
    soCCCD VARCHAR(12) PRIMARY KEY,
    ten VARCHAR(50),
    ho VARCHAR(50),
    queQuan VARCHAR(50),
    gioiTinh CHAR(1),
    ngaySinh DATE

);

CREATE TABLE TinhThanhPho (
    maTinh VARCHAR(10) PRIMARY KEY,
    tenTinhThanhPho VARCHAR(50)
);

CREATE TABLE DangKyXe (
    bienSo VARCHAR(10) PRIMARY KEY,
    soKhung VARCHAR(50),
    soMay VARCHAR(50),
    mauSac VARCHAR(50),
    namSanXuat INT,
    ngayDangKy DATE,
    ngayHetHan DATE,
    tenXe VARCHAR(50),
    hangXe VARCHAR(50),
    soCho INT,
    soCCCD VARCHAR(12),
    maTinh VARCHAR(10),
    FOREIGN KEY (soCCCD) REFERENCES ChuXe(soCCCD),
    FOREIGN KEY (maTinh) REFERENCES TinhThanhPho(maTinh),
);
CREATE TABLE XeViPham (
    bienSo VARCHAR(10),
    thoiGian DATETIME,
    trangThai VARCHAR(20),
    hinhAnhViPham VARCHAR(255),
    PRIMARY KEY (bienSo, thoiGian),
    FOREIGN KEY (bienSo) REFERENCES DangKyXe(bienSo)
);;"""
data=db.query("select * from chuXe")
print(data[0][2])

vi_pham = """
INSERT INTO XeViPham (bienSo, thoiGian, trangThai, hinhAnhViPham)
VALUES ('29A12345', '2021-10-10 10:00:00', 'Chua xu ly', '29A12345_20211010_100000.jpg');
"""
db.insert(vi_pham)