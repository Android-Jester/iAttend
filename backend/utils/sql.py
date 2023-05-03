
def create_tb_students():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(
            generated_id BIGINT PRIMARY KEY AUTO_INCREMENT,
            student_reference varchar(100) NOT NULL UNIQUE,
            student_index varchar(100) NOT NULL UNIQUE,
            student_firstname varchar(50) NOT NULL,
            student_lastname varchar(25) NOT NULL,
            student_nationality varchar(80) NOT NULL,
            student_gender varchar(15) NOT NULL,
            student_disability varchar(5) NOT NULL,
            card_issued_date varchar(15) NOT NULL,
            card_expiry_date varchar(15) NOT NULL
            )
        """
    return sql

def create_tb_student_study_details():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_student_study_details(
            generated_id BIGINT PRIMARY KEY AUTO_INCREMENT,
            student_reference varchar(100) NOT NULL UNIQUE,
            student_college varchar(20) NOT NULL,
            student_faculty varchar(25) NOT NULL,
            student_program varchar(255) NOT NULL,
            student_category varchar(255) NOT NULL,
            FOREIGN KEY(student_reference) REFERENCES tb_students(student_reference) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """
    return sql

def create_tb_student_profile():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_student_images(
            generated_id BIGINT PRIMARY KEY AUTO_INCREMENT,
            student_reference varchar(100) NOT NULL UNIQUE, 
            student_image BLOB NOT NULL
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
            user_status varchar(12) NOT NULL,
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

def create_database(database_name:str):
    return "CREATE DATABASE IF NOT EXISTS "+database_name

def user_database(database_name:str):
    return "USE "+database_name 

############################################################################################

def create_tb_students_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference varchar NOT NULL UNIQUE,
            student_index varchar(100) NOT NULL UNIQUE,
            student_firstname varchar(50) NOT NULL,
            student_lastname varchar(25) NOT NULL,
            student_nationality varchar(80) NOT NULL,
            student_gender varchar(15) NOT NULL,
            student_disability varchar(5) NOT NULL,
            card_issued_date varchar(15) NOT NULL,
            card_expiry_date varchar(15) NOT NULL 
            )
        """
    return sql

def create_tb_student_study_details_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_student_study_details(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference varchar(100) NOT NULL UNIQUE,
            student_college varchar(20) NOT NULL,
            student_faculty varchar(25) NOT NULL,
            student_program varchar(255) NOT NULL,
            student_category varchar(255) NOT NULL,
            FOREIGN KEY(student_reference) REFERENCES tb_students(student_reference) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """
    return sql

def create_tb_attendance_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference INT NOT NULL,
            student_college TEXT NOT NULL,
            student_faculty TEXT NOT NULL,
            student_program TEXT NOT NULL,
            student_category TEXT NOT NULL,
            student_nationality TEXT NOT NULL,
            student_gender TEXT NOT NULL,
            student_disability TEXT NOT NULL,
            date_stamp TEXT NOT NULL,
            time_in TEXT NOT NULL,
            time_out TEXT NOT NULL,
            duration TEXT NOT NULL
            )
        """
    return sql

def create_tb_images_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_student_images(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference varchar(100) NOT NULL UNIQUE, 
            student_image BLOB NOT NULL
            )
        """
    return sql

def create_tb_cameras_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_cameras(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera_id TEXT NOT NULL,
            camera_url TEXT NOT NULL
            )
        """
    return sql

def create_tb_user_details_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_details(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT, 
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
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_reference varchar(25) NOT NULL,
            user_username varchar(40) NOT NULL UNIQUE,
            user_password varchar(255) NOT NULL,
            user_status varchar(12) NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_profile_sqlite():
    sql = """
        CREATE TABLE IF NOT EXISTS tb_user_profile(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_reference varchar(25) NOT NULL, 
            user_image BLOB NOT NULL,
            FOREIGN KEY(user_reference) REFERENCES tb_user_details(user_reference)
            )
        """
    return sql

def create_tb_user_sessions_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_session(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_reference varchar(20) NOT NULL,  
            user_username varchar(25) NOT NULL,
            user_date varchar(25) NOT NULL,
            user_login varchar(35) NOT NULL, 
            user_logout varchar(25) NOT NULL,
            user_duration varchar(25) NOT NULL
        )
    """
    return sql

def create_tb_attendance_central_database():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance(
            generated_id BIGINT PRIMARY KEY AUTO_INCREMENT,
            student_college varchar(20) NOT NULL,
            student_faculty varchar(25) NOT NULL,
            student_program varchar(255) NOT NULL,
            student_category varchar(255) NOT NULL,
            student_nationality varchar(80) NOT NULL,
            student_gender varchar(15) NOT NULL,
            student_disability varchar(5) NOT NULL,
            facility_used varchar(30)
            )
        """
    return sql
############################################################################################################

def create_tb_attendance_last_seen_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance_last_seen(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference TEXT NOT NULL,
            date_stamp TEXT NOT NULL,
            time_in TEXT NOT NULL,
            time_out TEXT NOT NULL,
            duration TEXT NOT NULL
            )
        """
    return sql

def create_tb_attendance_temp_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_attendance_temp(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference INT NOT NULL,
            student_college TEXT NOT NULL,
            student_faculty TEXT NOT NULL,
            student_program TEXT NOT NULL,
            student_category TEXT NOT NULL,
            student_nationality TEXT NOT NULL,
            student_gender TEXT NOT NULL,
            student_disability TEXT NOT NULL,
            date_stamp TEXT NOT NULL,
            time_in TEXT NOT NULL,
            time_out TEXT NOT NULL,
            duration TEXT NOT NULL
            )
        """
    return sql

def create_tb_user_sessions_last_seen_sqlite():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_user_session_last_seen(
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