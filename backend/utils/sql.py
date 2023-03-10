
def create_tb_students():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(
            id INT PRIMARY KEY AUTO_INCREMENT,
            reference INT NOT NULL UNIQUE,
            index_ INT NOT NULL UNIQUE,
            firstname varchar(25) NOT NULL,
            lastname varchar(25) NOT NULL,
            college varchar(25) NOT NULL,
            program varchar(30) NOT NULL,
            nationality varchar(30) NOT NULL,
            startdate varchar(30) NOT NULL,
            enddate varchar(30) NOT NULL
            )
        """
    return sql

def create_tb_attendance():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(
            id INT PRIMARY KEY AUTO_INCREMENT,
            program varchar(30) NOT NULL,
            date_stamp varchar(30) NOT NULL,
            time_in varchar(30) NOT NULL,
            time_out varchar(30) NOT NULL,
            duration varchar(30) NOT NULL,
            st_reference INT NOT NULL
            )
        """
    return sql

def create_tb_images():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_images(
            id INT PRIMARY KEY AUTO_INCREMENT,
            st_reference INT NOT NULL, 
            image BLOB NOT NULL,
            FOREIGN KEY(st_reference) REFERENCES tb_students(reference)
            )
        """
    return sql

def create_tb_cameras():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_cameras(
            id INT PRIMARY KEY AUTO_INCREMENT,
            camera_id varchar(40) NOT NULL UNIQUE,
            camera_url varchar(100) NOT NULL
            )
        """
    return sql

def create_tb_user_details():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_details(
            id INT PRIMARY KEY AUTO_INCREMENT, 
            user_reference varchar(25) NOT NULL UNIQUE,
            user_firstname varchar(70) NOT NULL, 
            user_lastname varchar(35) NOT NULL, 
            user_contact varchar(25) NOT NULL UNIQUE,
            user_role varchar(10) NOT NULL,
            user_mail varchar(40) NOT NULL UNIQUE
        )
    """
    return sql

def create_tb_user_credentials():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_credentials(
            id INT PRIMARY KEY AUTO_INCREMENT,
            user_reference varchar(25) NOT NULL,
            user_username varchar(40) NOT NULL UNIQUE,
            user_password varchar(255) NOT NULL,
            user_status varchar(10) NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_profile():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_user_profile(
            id INT PRIMARY KEY AUTO_INCREMENT,
            user_reference varchar(25) NOT NULL, 
            user_image BLOB NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_sessions():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_session(
            id INT PRIMARY KEY AUTO_INCREMENT,
            user_reference varchar(20) NOT NULL,  
            user_username varchar(25) NOT NULL,
            user_date varchar(25) NOT NULL,
            user_login varchar(35) NOT NULL, 
            user_logout varchar(25) NOT NULL,
            user_duration varchar(25) NOT NULL
        )
    """
    return sql

def create_database(database_name:str):
    return "CREATE DATABASE IF NOT EXISTS "+database_name

def user_database(database_name:str):
    return "USE "+database_name 

############################################################################################

def create_tb_students_postgres():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(
            id SERIAL PRIMARY KEY ,
            reference int NOT NULL UNIQUE,
            index_ int NOT NULL UNIQUE,
            firstname varchar(25) NOT NULL,
            lastname varchar(25) NOT NULL,
            college varchar(25) NOT NULL,
            program varchar(30) NOT NULL,
            nationality varchar(30) NOT NULL,
            startdate varchar(30) NOT NULL,
            enddate varchar(30) NOT NULL
            )
        """
    return sql

def create_tb_attendance_postgres():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(
            id SERIAL PRIMARY KEY,
            program varchar(30) NOT NULL,
            date_stamp varchar(30) NOT NULL,
            time_in varchar(30) NOT NULL,
            time_out varchar(30) NOT NULL,
            duration varchar(30) NOT NULL,
            st_reference INT NOT NULL
            )
        """
    return sql

def create_tb_images_postgres():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_images(
            id SERIAL PRIMARY KEY,
            st_reference int NOT NULL UNIQUE, 
            image BYTEA NOT NULL,
            FOREIGN KEY(st_reference) REFERENCES tb_students(reference)
            )
        """
    return sql

def create_tb_cameras_postgres():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_cameras(
            id SERIAL PRIMARY KEY,
            camera_id varchar(40) NOT NULL UNIQUE,
            camera_url varchar(100) NOT NULL
            )
        """
    return sql

def create_tb_user_details_postgres():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_details(
            id SERIAL PRIMARY KEY, 
            user_reference varchar(25) NOT NULL UNIQUE,
            user_firstname varchar(70) NOT NULL, 
            user_lastname varchar(35) NOT NULL, 
            user_contact varchar(25) NOT NULL UNIQUE,
            user_role varchar(10) NOT NULL,
            user_mail varchar(40) NOT NULL UNIQUE
        )
    """
    return sql

def create_tb_user_credentials_postgres():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_credentials(
            id SERIAL PRIMARY KEY,
            user_reference varchar(25) NOT NULL,
            user_username varchar(40) NOT NULL UNIQUE,
            user_password varchar(255) NOT NULL,
            user_status varchar(10) NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_profile_postgres():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_user_profile(
            id SERIAL PRIMARY KEY,
            user_reference varchar(25) NOT NULL, 
            user_image BYTEA NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_sessions_postgres():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_session(
            id SERIAL PRIMARY KEY,
            user_reference varchar(20) NOT NULL,  
            user_username varchar(25) NOT NULL,
            user_date varchar(25) NOT NULL,
            user_login varchar(35) NOT NULL, 
            user_logout varchar(25) NOT NULL,
            user_duration varchar(25) NOT NULL
        )
    """
    return sql

#########################################################################################################

def create_tb_students_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference int NOT NULL UNIQUE,
            index_ int NOT NULL UNIQUE,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL, 
            college TEXT NOT NULL,
            program TEXT NOT NULL,
            nationality TEXT NOT NULL,
            startdate TEXT NOT NULL, 
            enddate TEXT NOT NULL
            )
        """
    return sql

def create_tb_attendance_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program TEXT NOT NULL,
            date_stamp TEXT NOT NULL,
            time_in TEXT NOT NULL,
            time_out TEXT NOT NULL,
            duration TEXT NOT NULL,
            st_reference INT NOT NULL
            )
        """
    return sql

def create_tb_images_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_images(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            st_reference int NOT NULL,
            image BLOB NOT NULL,
            FOREIGN KEY(st_reference) REFERENCES tb_students(reference)
            )
        """
    return sql

def create_tb_cameras_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_cameras(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera_id TEXT NOT NULL,
            camera_url TEXT NOT NULL
            )
        """
    return sql

def create_tb_user_details_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_details(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_reference varchar(25) NOT NULL UNIQUE,
            user_firstname varchar(70) NOT NULL, 
            user_lastname varchar(35) NOT NULL, 
            user_contact varchar(25) NOT NULL UNIQUE,
            user_role varchar(10) NOT NULL,
            user_mail varchar(40) NOT NULL UNIQUE
        )
    """
    return sql

def create_tb_user_credentials_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_credentials(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_reference varchar(25) NOT NULL,
            user_username varchar(40) NOT NULL UNIQUE,
            user_password varchar(255) NOT NULL,
            user_status varchar(10) NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_profile_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_user_profile(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_reference varchar(25) NOT NULL, 
            user_image BLOB NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_sessions_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_session(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_reference varchar(20) NOT NULL,  
            user_username varchar(25) NOT NULL,
            user_date varchar(25) NOT NULL,
            user_login varchar(35) NOT NULL, 
            user_logout varchar(25) NOT NULL,
            user_duration varchar(25) NOT NULL
        )
    """
    return sql
