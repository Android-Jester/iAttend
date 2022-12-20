
import os
import psycopg2
import sqlite3
from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
import mysql.connector as connector
from utils.sql import *
from database.ui_database import Ui_Database

class Database(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_database = Ui_Database()
        self.ui_database.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui_database.btn_close.clicked.connect(self.close)
        self.ui_database.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_database.frame.mouseMoveEvent = self.MoveWindow 

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.ui_database.frame.setGraphicsEffect(self.shadow)

        self.ui_database.btn_connect_test.clicked.connect(self.test_connection)
        self.ui_database.btn_connect.clicked.connect(self.my_cursor)
        self.set_database_properties()

    def get_details(self):
        path = 'C:\\ProgramData\\iVision\\data\\database_properties\\properties.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read().split(',')
            return details

    def set_database_properties(self):
        details = self.get_details()
        self.ui_database.username.setText(details[0])
        self.ui_database.password.setText(details[1])
        self.ui_database.hostname.setText(details[2])
        self.ui_database.port.setText(details[3])
        self.ui_database.database_name.setText(details[4])
        if str(details[3])=='3306':
            self.ui_database.mysql.setChecked(True)
        elif str(details[3])=='5432':
            self.ui_database.mysql.setChecked(True)
        
    def check_state(self):
        if self.ui_database.sqlite.isChecked():
            return True
        return False

    def get_field_text(self):
        username=self.ui_database.username.text()
        password=self.ui_database.password.text()
        hostname=self.ui_database.hostname.text()
        port=self.ui_database.port.text()
        database=self.ui_database.database_name.text()
        return username,password,hostname,port,database

    def my_cursor(self):
        details = self.get_field_text()
        user = details[0]
        password = details[1]
        host=details[2]
        port=details[3]
        database = details[4]
        if self.ui_database.mysql.isChecked() and self.ui_database.database_name.text() and self.ui_database.password.text():
            try:
                connection_status:str =("Connected to MySQL...")
                db=connector.connect(host=host,port=port,user=user,password=password,database=database)
                self.ui_database.label_notification.setText(connection_status) 
                return db,db.cursor(),connection_status 
            except Exception as e:
                return str(e)
        elif self.ui_database.postgresql.isChecked() and self.ui_database.database_name.text() and self.ui_database.password.text():
            try:
                connection_status:str =("Connected to PostgreSQL...")
                db=psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
                self.ui_database.label_notification.setText(connection_status)
                return db,db.cursor(),connection_status
            except Exception as e:
                return str(e)
        else:  
            try:
                connection_status:str =("Connected to SQLite3...")
                db = sqlite3.connect('D:\\Targets\\Commons\\backend\\sqlite\\attendance_system.db')
                self.ui_database.label_notification.setText(connection_status)
                return db, db.cursor(), connection_status
            except Exception as e:
               return str(e) 
          
    def test_connection(self):
        details = self.get_field_text()
        user = details[0]
        password = details[1]
        host=details[2]
        port=details[3]
        database = details[4]      
        if self.ui_database.mysql.isChecked():
            if self.ui_database.database_name.text() and self.ui_database.password.text():
                try:
                    db=connector.connect(host=host,port=port,user=user,password=password,database=database)
                    cursor = db.cursor()
                    cursor.execute(create_tb_students())
                    cursor.execute(create_tb_attendance())
                    cursor.execute(create_tb_images())
                    db.commit()
                    self.ui_database.label_notification.setText("Hey! you have MySQL working connection...")
                    return db,db.cursor() 
                except Exception as e:
                    self.ui_database.label_notification.setText(str(e))
            else:
                self.ui_database.label_notification.setText("Please provide your connection details")
        elif self.ui_database.postgresql.isChecked():
            if self.ui_database.database_name.text() and self.ui_database.password.text():
                try:
                    db=psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
                    cursor = db.cursor()
                    cursor.execute(create_tb_students_postgres())
                    cursor.execute(create_tb_attendance_postgres())
                    cursor.execute(create_tb_images_postgres())
                    db.commit()
                    self.ui_database.label_notification.setText("Hey! you have PostgreSQL working connection...")
                    return db,db.cursor()
                except Exception as e:
                    self.ui_database.label_notification.setText(str(e))
            else:
                self.ui_database.label_notification.setText("Please provide your connection details")
        elif self.ui_database.sqlite.isChecked():     
            try:
                db = sqlite3.connect('D:\\Targets\\Commons\\backend\\sqlite\\attendance_system.db')
                cursor = db.cursor()
                cursor.execute(create_tb_students_sqlite())
                cursor.execute(create_tb_attendance_sqlite())
                cursor.execute(create_tb_images_sqlite())
                db.commit()
                self.ui_database.label_notification.setText("Hey! you have SQLite3 working connection...")
                return db,db.cursor()
            except Exception as e:
                self.ui_database.label_notification.setText(str(e))    
    
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    
