
def create_tb_students():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(id INT PRIMARY KEY AUTO_INCREMENT, reference int NOT NULL UNIQUE, index_ int NOT NULL UNIQUE,
        firstname varchar(25) NOT NULL, lastname varchar(25) NOT NULL, college varchar(25) NOT NULL,program varchar(30) NOT NULL,nationality varchar(30) NOT NULL,
        startdate varchar(30) NOT NULL, enddate varchar(30) NOT NULL)
    """
    return sql

def create_tb_attendance():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(id INT PRIMARY KEY AUTO_INCREMENT,program varchar(30) NOT NULL,date_stamp varchar(30) NOT NULL,
        time_in varchar(30) NOT NULL,time_out varchar(30) NOT NULL,duration varchar(30) NOT NULL,st_reference INT NOT NULL)
    """
    return sql

def create_tb_images():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_images(id INT PRIMARY KEY AUTO_INCREMENT, st_reference int NOT NULL, image BLOB NOT NULL)
    """
    return sql

def create_tb_cameras():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_cameras(id INT PRIMARY KEY AUTO_INCREMENT, camera_id varchar(40) NOT NULL UNIQUE, camera_url varchar(100) NOT NULL)
    """
    return sql


def create_tb_students_postgres():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(id SERIAL PRIMARY KEY , reference int NOT NULL UNIQUE, index_ int NOT NULL UNIQUE,
        firstname varchar(25) NOT NULL, lastname varchar(25) NOT NULL, college varchar(25) NOT NULL,program varchar(30) NOT NULL,nationality varchar(30) NOT NULL,
        startdate varchar(30) NOT NULL, enddate varchar(30) NOT NULL)
    """
    return sql

def create_tb_attendance_postgres():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(id SERIAL PRIMARY KEY,program varchar(30) NOT NULL,date_stamp varchar(30) NOT NULL,
        time_in varchar(30) NOT NULL,time_out varchar(30) NOT NULL,duration varchar(30) NOT NULL,st_reference INT NOT NULL)
    """
    return sql

def create_tb_images_postgres():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_images(id SERIAL PRIMARY KEY, st_reference int NOT NULL UNIQUE, image BYTEA NOT NULL)
    """
    return sql

def create_tb_cameras_postgres():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_cameras(id SERIAL PRIMARY KEY, camera_id varchar(40) NOT NULL UNIQUE, camera_url varchar(100) NOT NULL)
    """
    return sql


def create_tb_students_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(id INTEGER PRIMARY KEY AUTOINCREMENT, reference int NOT NULL UNIQUE, index_ int NOT NULL UNIQUE,
        firstname TEXT NOT NULL, lastname TEXT NOT NULL, college TEXT NOT NULL,program TEXT NOT NULL,nationality TEXT NOT NULL,
        startdate TEXT NOT NULL, enddate TEXT NOT NULL)
    """
    return sql

def create_tb_attendance_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(id INTEGER PRIMARY KEY AUTOINCREMENT,program TEXT NOT NULL,date_stamp TEXT NOT NULL,
        time_in TEXT NOT NULL,time_out TEXT NOT NULL,duration TEXT NOT NULL,st_reference INT NOT NULL)
    """
    return sql

def create_tb_images_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_images(id INTEGER PRIMARY KEY AUTOINCREMENT, st_reference int NOT NULL, image BLOB NOT NULL)
    """
    return sql

def create_tb_cameras_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_cameras(id INTEGER PRIMARY KEY AUTOINCREMENT, camera_id TEXT NOT NULL, camera_url TEXT NOT NULL)
    """
    return sql



