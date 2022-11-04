################################################################################
##
## BY: Asamani Redolf
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import os
import sys
import cv2
import wget
import json
import time
import shutil
import requests
import winsound
import numpy as np
import pandas as pd

import pyshine as ps
from pyzbar.pyzbar import *
from datetime import datetime as dt

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import (QPoint,Qt, QTimer)
from PySide2.QtGui import (QColor, QPixmap, QImage)

from report.piechart.piechart import Canvas
from report.barchart.barchart import Barchart
from report.line_graph.line_plot import Line_plot


from model.student import Student
from model.attendance import Attendance

from launcher.ui_launcher import Ui_MainWindow
from camera_one.ui_surveillance_cam_one import *
from camera_two.surveillance_camera_two import *
from dashboard.ui_dashoboard import Ui_dashboard
from camera_four.surveillance_camera_four import * 
from exit_camera.exit_camera import ExitCameraFeed
from database.database import Database
from camera_three.surveillance_camera_three import * 
from camera_one.surveillance_camera_one import Surveilliance_One

GLOBAL_STATE = 0
counter = 0

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_dashboard()
        self.saveTimer = QTimer()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        #########################################################################################
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())    
        #########################################################################################

        #########################################################################################
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        # self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        self.ui.btn_clear_label.clicked.connect(self.loadUi_file)
        #########################################################################################

        #########################################################################################################
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_camera.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.database))
        self.ui.btn_help.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))
        self.ui.btn_report.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report))
        ##########################################################################################################

        #########################################################################################################
        self.piechart = Canvas()
        self.barchart = Barchart()
        self.line_graph = Line_plot()
        ########################################################################################################
    
        #########################################################################################
        self.open_exit_camera = ExitCameraFeed()
        self.ui.btn_open_exit_camera_ui.clicked.connect(lambda: self.open_exit_camera.show())
        

        self.database = Database()
        self.ui.btn_open_database.clicked.connect(lambda: self.database.show())
        ############################################################################################

        ############################################################################################
        self.open_surveillance_camera_one = Surveilliance_One()
        self.ui.btn_cast_cam_one.clicked.connect(lambda: self.open_surveillance_camera_one.show())

        self.surveillance_camera_two = Surveilliance_Two()
        self.ui.btn_cast_cam_one_2.clicked.connect(lambda: self.surveillance_camera_two.show())

        self.surveillance_camera_three = Surveilliance_Three()
        self.ui.btn_cast_cam_three.clicked.connect(lambda: self.surveillance_camera_three.show())

        self.surveillance_camera_four = Surveilliance_Four()
        self.ui.btn_cast_cam_four.clicked.connect(lambda: self.surveillance_camera_four.show())
        ############################################################################################

        ############################################################################################
        self.ui.btn_connect_detect.clicked.connect(self.start_webcam)
        self.ui.btn_disconnect.clicked.connect(self.stop_webcam)

        self.ui.btn_camera_reg_connect.clicked.connect(self.start_webcam_registration)
        self.ui.btn_camera_reg_disconnect.clicked.connect(self.stop_webcam_registration)
        ############################################################################################

        #############################################################################################
        self.ui.btn_search_page.clicked.connect(self.query_database_for_data)
        self.ui.calendarWidget.selectionChanged.connect(self.get_date_on_search_page)
        self.ui.calendarWidget_report.selectionChanged.connect(self.get_report_start_date)
        self.ui.calendarWidget_report_2.selectionChanged.connect(self.get_report_end_date)
        self.ui.btn_reload.clicked.connect(self.clear_fields_on_search_page)
        ##############################################################################################

        ##############################################################################################
        self.ui.btn_search_reg.clicked.connect(self.search_student)
        self.ui.calendarWidget_reg.selectionChanged.connect(self.get_registration_start_date)
        self.ui.calendarWidget_reg_2.selectionChanged.connect(self.get_registration_end_date)
        self.ui.btn_register.clicked.connect(self.register_student)
        self.ui.btn_clear.clicked.connect(self.resets_fileds)
        self.ui.btn_update.clicked.connect(self.update_student)
        self.ui.btn_remove.clicked.connect(self.remove_student)
        self.ui.btn_browse_reg.clicked.connect(self.browse_image_files)
     
        ##############################################################################################
        
        #####################################################################################################
        self.ui.calendarWidget.selectionChanged.connect(self.get_date_on_search_page)
        self.ui.btn_csv.clicked.connect(self.export_data_to_csv)
        self.ui.btn_json.clicked.connect(self.export_data_to_json)
        #####################################################################################################

        ###############################################################################################
        self.ui.brigthness.valueChanged.connect(self.update_brigthness)
        self.ui.sharpness.valueChanged.connect(self.update_sharpness)
        self.ui.contrast.valueChanged.connect(self.update_contrast)

        self.ui.reg_bright_value.setText(str(self.ui.brigthness.value()))
        self.ui.reg_sharpness_value.setText(str(self.ui.sharpness.value()))
        self.ui.reg_contrast_value.setText(str(self.ui.contrast.value()))

        self.ui.reg_brigthness_slider.valueChanged.connect(self.update_reg_brigthness)
        self.ui.reg_sharpness_slider.valueChanged.connect(self.update_reg_sharpness)
        self.ui.reg_contrast_slider.valueChanged.connect(self.update_reg_contrast)

        self.ui.brightness_value.setText(str(self.ui.brigthness.value()))
        self.ui.sharp_value.setText(str(self.ui.sharpness.value()))
        self.ui.contrast_value.setText(str(self.ui.contrast.value()))
        ##################################################################################################

        #################################################################################################

        self.ui.btn_camera_one_connect.clicked.connect(self.start_webcam_cam_one)
        self.ui.btn_camera_one_disconnect.clicked.connect(self.stop_webcam_cam_one)

        self.ui.btn_camera_two_connect.clicked.connect(self.start_webcam_cam_two)
        self.ui.btn_camera_two_disconnect.clicked.connect(self.stop_webcam_cam_two)

        self.ui.btn_camera_three_connect.clicked.connect(self.start_webcam_cam_three)
        self.ui.btn_camera_three_disconnect.clicked.connect(self.stop_webcam_cam_three)

        self.ui.btn_camera_four_connect.clicked.connect(self.start_webcam_cam_four)
        self.ui.btn_camera_four_disconnect.clicked.connect(self.stop_webcam_cam_four)
        ##################################################################################################
        self.ui.btn_load.clicked.connect(self.data_visualization)
        self.ui.report_start_date.textChanged.connect(self.report_start_date_value_change)
        self.ui.btn_refresh.clicked.connect(self.hot_reload)
        self.ui.btn_save.clicked.connect(self.save_report)
        #################################################################################################

        data = ['BSc. Physics','BSc. Statistics','BSc. Chemistry','BSc. Mathematics','Doctor of Optometry','BSc. Biochemistry','BSc. Computer Science',
        'BSc. Actuarial Science','BSc. Biological Science','BSc. Environmental Science','BSc. Food Science and Technology','BSc. Meterology and Climate Science']
        college = ['CoS']

        completer = QCompleter(data)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.search_box.setCompleter(completer)

        country_completer = QCompleter(self.country_names(r'backend\\json\\data_json.json'))
        country_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.reg_nationality.setCompleter(country_completer)
        
        self.ui.reg_college_2.addItem(college[0],data)
        self.ui.reg_college_2.currentIndexChanged.connect(self.update_program_combo)
        self.update_program_combo(self.ui.reg_college_2.currentIndex())
        self.ui.college_comboBox.addItem(college[0])
        self.ui.college_courses.addItems(data)
        self.ui.btn_remove_combox_item.clicked.connect(self.remove_item_from_comboBox)
        self.create_program_data_dir()
        self.ui.btn_scan_range.clicked.connect(self.get_active_cameras)
        ##################################################################################################

    def get_active_cameras(self):
        scan_range=self.ui.scan_range.text()
        if scan_range:
            for camera in range(int(scan_range)):
                capture = VideoCapture(camera)
                valid_cameras = []
                if capture.isOpened():
                    valid_cameras.append(camera)
                    data=[str(x) for x in valid_cameras]
                    self.ui.comboBox.addItems(data)
                    self.ui.reg_camera_combo.addItems(data)
                    self.open_exit_camera.set_combo_items(data)
                    self.open_surveillance_camera_one.set_combo_items(data)
                    self.surveillance_camera_three.set_combo_items(data)
                    self.surveillance_camera_two.set_combo_items(data)
                    self.surveillance_camera_four.set_combo_items(data)
                    self.ui.camera_three_comboBox.addItems(data)
                    self.ui.camera_two_comboBox.addItems(data)
                    self.ui.camera_one_comboBox.addItems(data)
                    self.ui.camera_four_comboBox.addItems(data)
                    self.ui.scan_range_label.setText("Active camera(s): "+str(len(data)))
        else:
            self.alert_builder("Oops! no scan range provided...")

    def country_names(self,path:str):
        with open(path,'r') as data:
            json_data = json.load(data)
        country_list = []
        for country_name in range(len(json_data)):
            country_list.append(json_data[country_name]['Name'])
        return country_list

    def alert(self, content:str):
        self.alert = AlertDialog()
        self.alert.content(content)
        self.alert.show()

    def helper(self,path_pdf,file_name:str):
        path = 'C:\\ProgramData\\iVision\\data'
        date=dt.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        new_name=r'backend\\report\\piechart\\'+file_name+date+'.pdf'
        os.rename(path_pdf,new_name)
        shutil.copy2(new_name,path)
        os.rename(new_name,path_pdf)

    def save_report(self):
        filename = self.ui.file_name.text()
        if self.ui.bar_chart.isChecked():
            path =r'backend\\report\\barchart\\barchart.pdf'   
            if self.ui.file_name.text():
                self.helper(path,filename)
                self.alert = AlertDialog()
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert = AlertDialog()
                self.alert.content("Oops! please provide file name")
                self.alert.show()         
        elif self.ui.line_graph.isChecked():
            path = r'backend\\report\\line_graph\\line_plot.pdf'
            if self.ui.file_name.text():
                self.helper(path,filename)
                self.alert = AlertDialog()
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert = AlertDialog()
                self.alert.content("Oops! please provide file name")
                self.alert.show() 
        elif self.ui.pie_chart.isChecked():
            path = r'backend\\report\\piechart\\piechart.pdf'
            if self.ui.file_name.text():
                self.helper(path,filename)
                self.alert = AlertDialog()
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert = AlertDialog()
                self.alert.content("Oops! please provide file name")
                self.alert.show() 
        

    def reconstruct_date(self,date:str):
        list_months = ['January', 'Febuary', 'March',
                'April', 'May', 'June', 'July',
                'August', 'September', 'October',
                'November', 'December']
        date_value=str(date).split('-')
        year = date_value[0]
        month = date_value[1]
        day = date_value[2]
        month=list_months[int(month)-1]
        return str(day+' '+month+' '+year)

    def create_program_data_dir(self):
        path = 'C:\\ProgramData\\iVision\\data'
        if not os.path.exists(path):
            os.makedirs(path)
            return path

    def get_pichart_data(self):
        query = self.query_database("SELECT DISTINCT program FROM tb_attendance")
        result_set= []
        for item in query: 
            result_set.append(item[0])
        total:list = []
        for item in result_set:
            program = "\'{}\'".format(item)
            sub_count = self.query_database("SELECT COUNT(*) FROM tb_attendance WHERE program="+program)
            total.append(sub_count[0][0])
        data = self.query_database("SELECT DISTINCT program FROM tb_attendance")
        result= []
        for item in data:
            item = str(item[0]).split(' ')
            result.append(item[1]) 
        return total, result
        

    def hot_reload(self):
        data = self.get_pichart_data()
        self.piechart.piechart(data,"Percentages of programs")
        self.ui.plot_area.setPixmap(QPixmap.fromImage(r'backend\\report\\piechart\\piechart.png'))
        self.ui.plot_area.setScaledContents(True)
        self.data_visualization()

    def report_start_date_value_change(self):
        date=self.ui.report_start_date.text()
        if self.ui.line_graph.isChecked():
            self.ui.date_range_comboBox.addItem(date) 

    def count_attendance_for_all_distinct_dates(self):
        program_="\'{}\'".format(self.ui.college_courses.currentText())
        results_list = []
        results=self.query_database("SELECT DISTINCT date_stamp FROM tb_attendance where program="+program_+" order by date_stamp asc")
        for date in results:
            results_list.append(date[0])    
        values =[]
        for date in results_list:
            date_values="\'{}\'".format(date)
            result_set=self.query_database("SELECT COUNT(*) FROM tb_attendance where date_stamp="+date_values + " and program="+program_)
            values.append(result_set[0][0])
            return values, results[0][0], results[-1][-1]

    def get_data_barchart(self):
        query_result = self.query_database("SELECT DISTINCT program FROM tb_attendance")
        result_list= []
        for item in query_result: 
            result_list.append(item[0])
        total:list = []
        for item in result_list:
            program = "\'{}\'".format(item)
            sub_count = self.query_database("SELECT COUNT(*) FROM tb_attendance WHERE program="+program)
            total.append(sub_count[0][0])
        data = self.query_database("SELECT DISTINCT program FROM tb_attendance")
        results= []
        for item in data:
            item = str(item[0]).split(' ')
            results.append(item[1][0:4].upper()) 
        return total,results

    def get_data_by_date(self):
        start = self.ui.report_start_date.text()
        start_date="\'{}\'".format(start)
        query_result = self.query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp= "+start_date)
        result_list= []
        for item in query_result: 
            result_list.append(item[0])
        total:list = []
        for item in result_list:
            program = "\'{}\'".format(item)
            sub_count = self.query_database("SELECT COUNT(*) FROM tb_attendance WHERE program="+program+" and date_stamp= "+start_date)
            total.append(sub_count[0][0])
        data = self.query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp= "+start_date)
        result= []
        for item in data:
            item = str(item[0]).split(' ')
            result.append(item[1][0:4].upper())   
        return total, result

    def get_data_by_date_range(self):
        start_date="\'{}\'".format(self.ui.report_start_date.text())
        end_date="\'{}\'".format(self.ui.report_end_date.text())
        query_result = self.query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp BETWEEN "+start_date+" AND "+end_date)
        result_list= []
        for item in query_result: 
            result_list.append(item[0])
        total:list = []
        for item in result_list:
            program = "\'{}\'".format(item)
            sub_count = self.query_database("SELECT COUNT(*) date_stamp FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" and "+end_date+" and program="+program)
            total.append(sub_count[0][0])
        data = self.query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp BETWEEN "+start_date+" AND "+end_date)
        result= []
        for item in data:
            item = str(item[0]).split(' ')
            result.append(item[1][0:4].upper())  
        return total, result

    def line_plot_values(self):
        results_list = []
        dates=self.get_date_for_line_plot()
        program=self.ui.college_courses.currentText()
        for date in range(len(dates)):
            date_values="\'{}\'".format(dates[date])
            program_="\'{}\'".format(program)
            results=self.query_database("SELECT COUNT(*) program FROM tb_attendance where date_stamp="+date_values+" AND program="+program_)
            results_list.append(results[0][0])
        return results_list

    def get_date_for_line_plot(self):
        setattr(self.ui.date_range_comboBox,'allItems',
        lambda:[self.ui.date_range_comboBox.itemText(i) for i in range(self.ui.date_range_comboBox.count())])
        return self.ui.date_range_comboBox.allItems()

    def remove_item_from_comboBox(self):
        self.ui.date_range_comboBox.removeItem(self.ui.date_range_comboBox.currentIndex())

    def data_visualization(self):
        colors = ['#2000DF', '#80c300', '#3DED97', 'yellow', 'orange', 'violet','#60009F','#005080'
        ,'#00A000','#4E0707','#B56727','#5DBB63']        
        width = 0.7
        program = self.ui.college_courses.currentText()
        if self.ui.bar_chart.isChecked():
            if not self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_data_barchart()
                self.barchart.bar_plot_single_view(data[0], data[1],width,"Statictics","Number of students","Programs",
                colors[:len(data[0])])
                self.ui.plot_area_2.setPixmap(QPixmap.fromImage(r'backend\\report\\barchart\\barchart.png'))
                self.ui.plot_area_2.setScaledContents(True)
            elif self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_data_by_date()
                self.barchart.bar_plot_single_view(data[0], data[1],width,"Statictics ","Number of students",
                self.get_report_start_date(),colors[:len(data[0])])
                self.ui.plot_area_2.setPixmap(QPixmap.fromImage(r'backend\\report\\barchart\\barchart.png'))
                self.ui.plot_area_2.setScaledContents(True)
            elif self.ui.report_end_date.text() and self.ui.report_end_date.text():
                data = self.get_data_by_date_range()      
                self.barchart.bar_plot_single_view(data[0], data[1],width,"Statictics","Number of students",
                self.get_report_start_date()+" <> "+self.get_report_end_date(),colors[:len(data[0])])
                self.ui.plot_area_2.setPixmap(QPixmap.fromImage(r'backend\\report\\barchart\\barchart.png'))
                self.ui.plot_area_2.setScaledContents(True)   
        elif self.ui.line_graph.isChecked():
            program=self.ui.college_courses.currentText()
            if self.ui.date_range_comboBox.currentText():
                y_values =self.line_plot_values()
                self.line_graph.plot_graph(y_values,title="Trend in attendance for "+program,label_="Trends",
                y_label="Number of students",x_label="Date")
                self.ui.plot_area_2.setPixmap(QPixmap.fromImage(r'backend\\report\\line_graph\\line_plot.png'))
                self.ui.plot_area_2.setScaledContents(True)
            elif not self.ui.date_range_comboBox.currentText():
                y_values=self.count_attendance_for_all_distinct_dates()
                self.line_graph.plot_graph(y_values[0],title="Trend in attendance for "+program,label_="Trends",
                y_label="Number of students",x_label=self.reconstruct_date(y_values[1])+'<>'+self.reconstruct_date(y_values[2]))
                self.ui.plot_area_2.setPixmap(QPixmap.fromImage(r'backend\\report\\line_graph\\line_plot.png'))
                self.ui.plot_area_2.setScaledContents(True)
        elif self.ui.pie_chart.isChecked():
            if self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_data_by_date()
                self.piechart.piechart(data,self.get_report_start_date())
                self.ui.plot_area.setPixmap(QPixmap.fromImage(r'backend\\report\\piechart\\piechart.png'))
                self.ui.plot_area.setScaledContents(True)
            elif self.ui.report_end_date.text() and self.ui.report_end_date.text():
                data = self.get_data_by_date_range()      
                self.piechart.piechart(data,self.get_report_start_date()+" <> "+self.get_report_end_date())
                self.ui.plot_area.setPixmap(QPixmap.fromImage(r'backend\\report\\piechart\\piechart.png'))
                self.ui.plot_area.setScaledContents(True)
            elif not self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_pichart_data()
                self.piechart.piechart(data,"Percentages of programs")
                self.ui.plot_area.setPixmap(QPixmap.fromImage(r'backend\\report\\piechart\\piechart.png'))
                self.ui.plot_area.setScaledContents(True)  


    def export_data_to_csv(self):
        table=self.ui.tableWidget.item(0,0)
        date=dt.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iVision\\data\\students_data'+date+'.csv'
        if table:
            details=self.query_database_for_data()
            data = pd.DataFrame(details)
            data.to_csv(path,sep=',',index=False,
            header=['Id','Program','Date_stamp','Time_in','Time_out','Duration','Reference'])
            self.alert = AlertDialog()
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! you have no data to export...")
            self.alert.show()

    def export_data_to_json(self):
        table=self.ui.tableWidget.item(0,0)
        date=dt.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iVision\\data\\students_data'+date+'.json'
        if table:
            details=self.query_database_for_data()
            data=pd.DataFrame(details,columns=['Id','Program','Date_stamp','Time_in','Time_out','Duration','Reference'])
            data.to_json(path,orient='records',indent=4)
            self.alert = AlertDialog()
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! you have no data to export...")
            self.alert.show()

    def update_program_combo(self,index):
        self.ui.reg_programs.clear()
        programs = self.ui.reg_college_2.itemData(index)
        if programs:
            self.ui.reg_programs.addItems(programs)
        
    def query_database(self, query: str):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        if cursor:
            for item in cursor:
                details.append(item)
            db.commit()
        return details
    
    def ui_table(self, details: list):
        self.ui.tableWidget.setAutoScroll(True)
        self.ui.tableWidget.setAutoScrollMargin(2)
        self.ui.tableWidget.setTabKeyNavigation(True)
        self.ui.tableWidget.setColumnWidth(1,230)
        self.ui.tableWidget.setRowCount(len(details))
        self.ui.tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget.setItem(row_count,1,QtWidgets.QTableWidgetItem(str(data[1])))
            self.ui.tableWidget.setItem(row_count,2,QtWidgets.QTableWidgetItem(str(data[2])))
            self.ui.tableWidget.setItem(row_count,3,QtWidgets.QTableWidgetItem(str(data[3])))
            self.ui.tableWidget.setItem(row_count,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget.setItem(row_count,5,QtWidgets.QTableWidgetItem(str(data[5])))
            self.ui.tableWidget.setItem(row_count,0,QtWidgets.QTableWidgetItem(str(data[6])))
            row_count = row_count+1

    def fetch_details_for_card_view(self):
        results=self.query_database("SELECT * FROM tb_attendance WHERE st_reference="+str(self.ui.search_box.text()))
        self.ui_table(results)
        if self.ui.search_box.text():
            db_data=self.fetch_data_from_db(self.ui.search_box.text())
            if len(db_data) > 0:
                list_months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',
                     'August', 'September', 'October', 'November', 'December']
                start_date = (str(db_data[8])).split('-')
                end_date=str(db_data[9]).split('-')
                student_year=(int(dt.now().date().strftime('%Y'))-int(start_date[0]))
                      
                if student_year <= 1:
                    level = "1st year"
                elif student_year > 1 and student_year <= 2:
                    level = "2nd year"
                elif student_year > 2 and student_year <= 3:
                    level = "3rd year"
                elif student_year > 3 and student_year <= 4:
                    level = "4th year"
                helper = str(db_data[3]).split(" ")
                self.ui.db_firstname.setText(helper[0])
                self.ui.db_middlename.setText(helper[1])
                self.ui.db_lastname.setText(db_data[4])
                self.ui.db_refrence.setText(str(db_data[1]))
                self.ui.db_index.setText(str(db_data[2]))
                self.ui.db_college.setText(db_data[5])
                self.ui.db_nationality.setText(db_data[7])
                self.ui.db_programe.setText(db_data[6])
                self.ui.db_year.setText(level)
                self.ui.db_validity.setText(list_months[int(start_date[1])-1]+","+start_date[0]+
                " - "+list_months[int(end_date[1])-1]+","+end_date[0])
                self.load_image_from_db(self.ui.search_box.text(),self.ui.db_image_data)
            else:
                self.alert_builder("Student details not found. Please enter\nyour details to register!")
        else:
            self.alert_builder("Oops! search field can't be empty.")

    def query_for_data_reference(self):
        start = self.ui.db_start_date.text()
        start_date="\'{}\'".format(start)
        end = self.ui.db_end_date.text()
        end_date="\'{}\'".format(end)
        results = self.query_database("SELECT * FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" AND "+end_date)
        self.ui_table(results)
        return results
    
    def fetch_data_by_program_and_date(self):
        start = self.ui.db_start_date.text()
        start_date="\'{}\'".format(start)
        prog = self.ui.search_box.text()
        program="\'{}\'".format(prog)
        print(program)
        results = self.query_database("SELECT * FROM tb_attendance WHERE program="+program+" and date_stamp="+start_date)
        self.ui_table(results)
        return results

    def query_database_for_data(self):      
        if self.ui.checkBox.isChecked():
            if self.ui.search_box.text() and self.ui.db_start_date.text():
                program = self.ui.search_box.text()
                program = "\'{}\'".format(program)
                details = self.query_database("SELECT * FROM tb_attendance WHERE program="+program)
                self.ui_table(details)
                return details
            elif self.ui.search_box.text() and self.ui.db_start_date.text():
                self.fetch_data_by_program_and_date()
            elif self.ui.search_box.text() and self.ui.db_start_date.text() and  self.ui.db_end_date.text():
                start = self.ui.db_start_date.text()
                start_date="\'{}\'".format(start)
                end = self.ui.db_end_date.text()
                end_date="\'{}\'".format(end)
                prog = self.ui.search_box.text()
                program="\'{}\'".format(prog)
                results = self.query_database("SELECT * FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" and "+end_date+" and program="+program)
                self.ui_table(results)
                return results
            else:
                program = self.ui.search_box.text()
                program = "\'{}\'".format(program)
                details = self.query_database("SELECT * FROM tb_attendance WHERE program="+program)
                self.ui_table(details)
                return details
        else:
            if self.ui.db_start_date.text() and  self.ui.db_end_date.text():
                self.query_for_data_reference()
            elif self.ui.db_start_date.text():
                current_date = self.ui.db_start_date.text()
                current_date = "\'{}\'".format(current_date)
                results = self.query_database("SELECT * FROM tb_attendance WHERE date_stamp ="+current_date)
                self.ui_table(results)
                return results
            elif self.ui.search_box.text():
                self.fetch_details_for_card_view()
            elif self.ui.search_box.text() and self.ui.db_start_date.text() and  self.ui.db_end_date.text():
                self.fetch_details_for_card_view()
                return self.query_for_data_reference() 
            else:
                details=self.query_database("SELECT * FROM tb_attendance")
                self.ui_table(details)
                return details 
                        

    def get_date_on_search_page(self):
        date = self.ui.calendarWidget.selectedDate()
        if self.ui.start_date.isChecked():
            self.ui.db_start_date.setText(str(date.toPython()))
        elif self.ui.end_date.isChecked():
            self.ui.db_end_date.setText(str(date.toPython()))

    def clear_fields_on_search_page(self):
        self.ui.db_firstname.setText("")
        self.ui.db_middlename.setText("")
        self.ui.db_lastname.setText("")
        self.ui.db_college.setText("")
        self.ui.db_refrence.setText("")
        self.ui.db_index.setText("")
        self.ui.db_nationality.setText("")
        self.ui.db_programe.setText("")
        self.ui.db_validity.setText("")
        self.ui.db_year.setText("")
        self.ui.db_image_data.setPixmap("")
        self.ui.db_start_date.setText("")
        self.ui.db_end_date.setText("")
        

    def get_report_start_date(self):
        date =self.ui.calendarWidget_report.selectedDate()
        self.ui.report_start_date.setText(str(date.toPython()))
        return str(date.toString())

    def get_report_end_date(self):
        date =self.ui.calendarWidget_report_2.selectedDate()
        self.ui.report_end_date.setText(str(date.toPython()))
        return str(date.toString())
  

    def get_registration_start_date(self):
        date = self.ui.calendarWidget_reg.selectedDate()
        self.ui.reg_start_date.setText(str(date.toPython()))

    def get_registration_end_date(self):
        date = self.ui.calendarWidget_reg_2.selectedDate()
        self.ui.reg_end_date.setText(str(date.toPython()))

    def register_student(self):
        check_state=self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        if self.ui.reg_student_ref.text() and self.ui.reg_firstname.text():
            student = Student(
                int(self.ui.reg_student_ref.text()),
                int(self.ui.reg_index.text()),
                self.ui.reg_firstname.text()+" "+self.ui.reg_middlename.text(),
                self.ui.reg_lastname.text(),
                self.ui.reg_college_2.currentText(),
                self.ui.reg_programs.currentText(),
                self.ui.reg_nationality.text(),
                self.ui.reg_start_date.text(),
                self.ui.reg_end_date.text(),
            )
            if check_state == True:
                if self.ui.image_file_reg.text() and self.ui.file_system.isChecked():
                    with open(self.ui.image_file_reg.text(), 'rb') as image:
                        data = image.read()
                        my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(?,?)",(student.reference,data))
                    my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (?,?,?,?,?,?,?,?,?)",
                    (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))   
                    db.commit() 
                    self.alert_builder("Student registered successfully")   
                elif self.ui.online_image.isChecked() and self.ui.image_file_reg.text():
                    path = r'backend\\images\\download\\image.jpeg'
                    if os.path.exists(path):
                        with open(path, 'rb') as image:
                            data = image.read()
                            my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(?,?)",(student.reference,data))
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (?,?,?,?,?,?,?,?,?)",
                        (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date)) 
                        db.commit()
                        self.alert_builder("Student registered successfully")
                        os.remove(path)          
                else:
                    self.alert_builder("Oops! something went wrong while\nprocessing your request") 
            else:
                if self.ui.image_file_reg.text() and self.ui.file_system.isChecked():
                    with open(self.ui.image_file_reg.text(), 'rb') as image:
                        data = image.read()
                        my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(%s,%s)",(student.reference,data))
                    my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))   
                    db.commit()
                    self.alert_builder("Student registered successfully")    
                elif self.ui.online_image.isChecked() and self.ui.image_file_reg.text():
                    path = r'backend\\images\\download\\image.jpeg'
                    if os.path.exists(path):
                        with open(path, 'rb') as image:
                            data = image.read()       
                            my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(%s,%s)",(student.reference,data))
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))
                        db.commit()
                        os.remove(path)
                        self.alert_builder("Student registered successfully")    
                else:
                    self.alert_builder("Oops! something went wrong while\nprocessing your request") 
        else:
            self.alert_builder("Oops! something went wrong while\nprocessing your request") 

    def alert_builder(self, message:str):
        self.alert = AlertDialog()
        self.alert.content(message)
        self.alert.show()
          
    def fetch_data_from_db(self,reference):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        detail =my_cursor.execute("SELECT * FROM tb_students WHERE reference="+reference)
        detail= my_cursor.fetchone()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
            db.commit()
        return db_data

    def load_image_from_db(self,reference,label):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        cursor=my_cursor.execute("SELECT st_reference,image from tb_images WHERE st_reference="+reference)
        cursor= my_cursor.fetchone()
        image_data = []
        if cursor:
            for data in cursor:
                image_data.append(data)
            db.commit()
            if len(image_data)>0:
                with open(r'backend\\images\\assets\\image.jpeg','wb') as image_file:
                        image_file.write(image_data[1])
            label.setPixmap(QPixmap.fromImage(r'backend\\images\\assets\\image.jpeg'))
            label.setScaledContents(True)
        else:
            label.setPixmap(QPixmap.fromImage(r'backend\\images\\assets\\img.png'))
            label.setScaledContents(True)

    def search_student(self):
            if self.ui.search_reg.text():
                db_data=self.fetch_data_from_db(self.ui.search_reg.text())
                if len(db_data) > 0:
                    helper = str(db_data[3]).split(" ")
                    self.ui.reg_firstname.setText(helper[0])
                    self.ui.reg_middlename.setText(helper[1])
                    self.ui.reg_lastname.setText(db_data[4])
                    self.ui.reg_student_ref.setText(str(db_data[1]))
                    self.ui.reg_index.setText(str(db_data[2]))
                    self.ui.reg_college.setText(db_data[5])
                    self.ui.reg_nationality.setText(db_data[7])
                    self.ui.reg_start_date.setText(db_data[8])
                    self.ui.reg_end_date.setText(db_data[9])
                    self.ui.reg_programs.setCurrentText(db_data[6])
                    self.ui.reg_college_2.setCurrentText(db_data[5])
                    self.load_image_from_db(self.ui.search_reg.text(),self.ui.reg_image)
                else:
                    self.alert_builder("Student not found. Please enter\nyour details to register!")
            else:
                self.alert_builder("Oops! search field can't be empty.")

    def update_student(self):
        check_state = self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        if self.ui.reg_student_ref.text() and self.ui.image_file_reg.text() and self.ui.file_system.isChecked():
            ref = self.ui.reg_student_ref.text()
            with open(self.ui.image_file_reg.text(), 'rb') as image:
                data = image.read()
                if check_state == True:
                    my_cursor.execute("UPDATE tb_images SET image =? WHERE st_reference=?",(data,ref))
                    db.commit()
                else:
                    my_cursor.execute("UPDATE tb_images SET image =%s WHERE st_reference=%s",(data,ref))
                    db.commit()
            self.alert_builder("Hey! Student image updated successfully.")
        elif self.ui.reg_student_ref.text() and self.ui.image_file_reg.text() and self.ui.online_image.isChecked():
            ref = self.ui.reg_student_ref.text()
            path = r'backend\\images\\download\\image.jpeg'
            if os.path.exists(path):
                with open(path, 'rb') as image:
                    data = image.read()
                    if check_state == True:
                        my_cursor.execute("UPDATE tb_images SET image =? WHERE st_reference=?",(data,ref))
                        db.commit()
                    else:
                        my_cursor.execute("UPDATE tb_images SET image =%s WHERE st_reference=%s",(data,ref))
                        db.commit()
                self.alert_builder("Hey! Student image updated successfully.")
                os.remove(path)
            else:
                self.alert_builder("Oops! the image does not exist.\nplease download it and try again.")
        else:
            self.alert_builder("Oops! Something went wrong.")
            
    def remove_student(self):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        try:
            my_cursor.execute("DELETE FROM tb_students where reference="+self.ui.reg_student_ref.text())
            db.commit()
            self.resets_fileds()
            self.alert_builder("Student data removed successfuly!")
        except:
            self.alert_builder("Oops! internal server erro!")

    def resets_fileds(self):
        self.ui.reg_firstname.setText("")
        self.ui.reg_middlename.setText("")
        self.ui.reg_lastname.setText("")
        self.ui.reg_student_ref.setText("")
        self.ui.reg_index.setText("")
        self.ui.reg_college.setText("")
        self.ui.reg_nationality.setText("")
        self.ui.reg_start_date.setText("")
        self.ui.reg_end_date.setText("")
        self.ui.reg_college.setText("")
        self.ui.reg_image.setPixmap("")

    def connected_to_internet(self,url='http://www.google.com/', timeout=5):
        try:
            _ = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError:  
            return False

    def browse_image_files(self):
        if self.ui.file_system.isChecked():    
            path= QFileDialog.getOpenFileName(self, "Select File","","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png)")
            if path:
                self.ui.image_file_reg.setText(path[0])
                self.ui.reg_image.setPixmap(QPixmap.fromImage(path[0]))
                self.ui.reg_image.setScaledContents(True)
        elif self.ui.online_image.isChecked():
            link = self.ui.image_file_reg.text()
            if self.connected_to_internet()==True:
                try:
                    wget.download(link,r"backend\\images\\download\\image.jpeg")
                    self.ui.reg_image.setPixmap(QPixmap.fromImage(r"backend\\images\\download\\image.jpeg"))
                    self.ui.reg_image.setScaledContents(True)
                except Exception as e:
                    self.alert_builder("Oops! check your image url!")
            elif self.connected_to_internet()==False:
                 self.alert_builder("Oops! check you internet connection!")         

    def loadUi_file(self):
        self.ui.firstname.setText("")
        self.ui.middlename.setText("")
        self.ui.lastname.setText("")
        self.ui.refrence.setText("")
        self.ui.index.setText("")
        self.ui.coledge.setText("")
        self.ui.nationality.setText("")
        self.ui.validity.setText("")
        self.ui.program.setText("")
        self.ui.year.setText("")
        self.ui.last_in.setText("")
        self.ui.last_out.setText("")
        self.ui.image.setPixmap("")
        self.ui.label_notification.setText("Notification")


    def last_seen(self,reference:str):  
        (db,my_cursor,connection_status) = self.database.my_cursor()
        cursor=my_cursor.execute("SELECT date_stamp,time_out,duration FROM tb_attendance WHERE st_reference = "+(reference)+" ORDER BY date_stamp DESC LIMIT 2")
        cursor= my_cursor.fetchall()
        last_seen_info = []
        if cursor:
            for data in cursor:
                last_seen_info.append(data)
            db.commit()
        if len(last_seen_info)>=2:
            details=self.reconstruct_date(last_seen_info[1][0])
            time = last_seen_info[0][1]
            duration = last_seen_info[0][2]
            self.ui.last_out.setText(details+' @ '+time)
            self.ui.last_in.setText(duration)           
        else:
            self.ui.last_out.setText("Oops! first timer")
            self.ui.last_in.setText("00:00:00") 

    def retreive_student_details(self,data):
        if isinstance(data, str):
                self.last_seen(data)
                db_data=self.fetch_data_from_db(data)
                if len(db_data) > 0:
                    list_months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',
                     'August', 'September', 'October', 'November', 'December']
                    start_date = (str(db_data[8])).split('-')
                    end_date=str(db_data[9]).split('-')
                    student_year=(int(dt.now().date().strftime('%Y'))-int(start_date[0]))
                      
                    if student_year <= 1:
                        level = "1st year"
                    elif student_year > 1 and student_year <= 2:
                        level = "2nd year"
                    elif student_year > 2 and student_year <= 3:
                        level = "3rd year"
                    elif student_year > 3 and student_year <= 4:
                        level = "4th year"

                    helper = str(db_data[3]).split(" ")
                    self.ui.firstname.setText(helper[0])
                    self.ui.middlename.setText(helper[1])
                    self.ui.lastname.setText(db_data[4])
                    self.ui.refrence.setText(str(db_data[1]))
                    self.ui.index.setText(str(db_data[2]))
                    self.ui.coledge.setText(db_data[5])
                    self.ui.nationality.setText(db_data[7])
                    self.ui.validity.setText(list_months[int(start_date[1])-1]+","+start_date[0]+
                    " - "+list_months[int(end_date[1])-1]+","+end_date[0])
                    self.ui.year.setText(level)
                    self.ui.program.setText(db_data[6])
                    self.load_image_from_db(data,self.ui.image)
                else:
                    self.loadUi_file()
                    self.show_info("Oops! student not found. Please register!")                

    def mark_attendance_db(self):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        attendance = Attendance(
            self.ui.refrence.text(),
            self.ui.program.text(),
            str(dt.now().date().strftime("%Y-%m-%d")),
            str(dt.now().time().strftime("%H:%M:%S")),
            str(dt.now().time().strftime("%H:%M:%S")),
            "00:00:00"
        )
        check_state = self.database.check_state()
        details = []
        date="\'{}\'".format(dt.now().date().strftime("%Y-%m-%d"))
        if self.ui.refrence.text() != "Reference" and self.ui.refrence.text() !="" :
            data=my_cursor.execute("SELECT st_reference,date_stamp FROM tb_attendance WHERE st_reference="+self.ui.refrence.text()+" and date_stamp="+date)
            data=my_cursor.fetchone()
            if data:
                for detail in data:
                    details.append(detail)
                db.commit()
             
            if not details:
                if check_state==True:
                    my_cursor.execute("INSERT INTO tb_attendance(st_reference,program,date_stamp,time_in,time_out,duration) VALUES(?,?,?,?,?,?)",
                    (attendance.st_reference,attendance.program,attendance.date,
                    attendance.time_in,attendance.time_out,attendance.duration))
                    db.commit()
                else: 
                    my_cursor.execute("INSERT INTO tb_attendance(st_reference,program,date_stamp,time_in,time_out,duration) VALUES(%s,%s,%s,%s,%s,%s)",
                    (attendance.st_reference,attendance.program,attendance.date,
                    attendance.time_in,attendance.time_out,attendance.duration))
                    db.commit() 
            elif details:
                winsound.Beep(1000,100)
                self.show_info("Attendance taken, you can proceed!\nNext person please...")
            else:
                 self.show_info("Oops! something went wrong...")


    def start_webcam_registration(self):
        ip_address = self.ui.reg_camera_ip.text()
        system_attached_camera = self.ui.reg_camera_combo.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:  
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_registration
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.show_alert = AlertDialog()
                self.show_alert.content("Hey! wait a second while system\ninitializes camera") 
                self.show_alert.show()
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:       
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_registration
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.show_alert = AlertDialog()
                self.show_alert.content("Hey! wait a second while system\ninitializes camera") 
                self.show_alert.show()
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_registration
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_registration)
        self.timer.start(3)

    def update_frame_registration(self):
        thickness = 2
        rect_thickness = 1
        color = (255,255,0)

        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)

        self.beta = int(self.ui.reg_bright_value.text())
        self.apha = int(self.ui.reg_contrast_value.text())*0.01
        self.kernel = (int(self.ui.reg_sharpness_value.text())*0.01, int(self.ui.sharp_value.text())*0.01)
       
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.ones(self.frame.shape, self.frame.dtype), 0, self.beta)

        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.now = dt.now()
        self.now = self.now.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.now,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(10,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        for qr_code in decode(self.result):
            qr_code_data  = qr_code.data.decode('utf-8')
            pts = np.array([qr_code.polygon], np.int)
            rect = np.array([qr_code.rect], np.int)
            pts = pts.reshape((-1, 1, 2)) 
            print(qr_code_data)  
            # cv2.polylines(frame, [pts], True,color,1)
            for x,y,w,h in rect:
                w , h =x+w, y+h
                cv2.rectangle(self.result, (x,y), (w,h), color, rect_thickness)
                cv2.line(self.result,(x,y),(x+15,y),color,thickness)
                cv2.line(self.result,(x,y),(x,y+15),color,thickness)
                cv2.line(self.result,(w,y),(w-15,y),color,thickness)
                cv2.line(self.result,(w,y),(w,y+15),color,thickness)
                cv2.line(self.result,(x,h),(x+15,h),color,thickness)
                cv2.line(self.result,(x,h),(x,h-15),color,thickness)
                cv2.line(self.result,(w,h),(w-15,h),color,thickness)
                cv2.line(self.result,(w,h),(w,h-15),color,thickness) 
            winsound.Beep(1000,100) 
        self.display_feed_registration(self.result,1)         
        
    def display_feed_registration(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui.reg_cap_frame.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui.reg_cap_frame.setScaledContents(True)
        
    def stop_webcam_registration(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.reg_cap_frame.setPixmap(QPixmap())
        self.ui.reg_cap_frame.setAlignment(Qt.AlignCenter)
        self.timer.stop()

    def update_reg_brigthness(self, value):
        self.ui.reg_bright_value.setText(str(value))
        return value 

    def update_reg_sharpness(self, value):
        self.ui.reg_sharpness_value.setText(str(value))
        return value

    def update_reg_contrast(self, value):
        self.ui.reg_contrast_value.setText(str(value))
        return value 


    def start_webcam(self):
        ip_address = self.ui.camera_ip.text()
        system_attached_camera = self.ui.comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:  
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.show_info("Hey! wait a second while system\ninitializes camera")
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:       
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.show_info("Hey! wait a second while system\ninitializes camera")
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(3)

    def update_frame(self):

        thickness = 2
        rect_thickness = 1
        color = (255,255,0)
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)

        self.beta = int(self.ui.brightness_value.text())
        self.apha = int(self.ui.contrast_value.text())*0.01
        self.kernel = (int(self.ui.sharp_value.text())*0.01, int(self.ui.sharp_value.text())*0.01)
       
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.ones(self.frame.shape, self.frame.dtype), 0, self.beta)

        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.now = dt.now()
        self.now = self.now.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.now,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(10,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        for qr_code in decode(self.result):
            qr_code_data  = qr_code.data.decode('utf-8')
            pts = np.array([qr_code.polygon], np.int)
            rect = np.array([qr_code.rect], np.int)
            pts = pts.reshape((-1, 1, 2))   
            # cv2.polylines(frame, [pts], True,color,1)
            for x,y,w,h in rect:
                w , h =x+w, y+h
                cv2.rectangle(self.result, (x,y), (w,h), color, rect_thickness)
                cv2.line(self.result,(x,y),(x+15,y),color,thickness)
                cv2.line(self.result,(x,y),(x,y+15),color,thickness)
                cv2.line(self.result,(w,y),(w-15,y),color,thickness)
                cv2.line(self.result,(w,y),(w,y+15),color,thickness)
                cv2.line(self.result,(x,h),(x+15,h),color,thickness)
                cv2.line(self.result,(x,h),(x,h-15),color,thickness)
                cv2.line(self.result,(w,h),(w-15,h),color,thickness)
                cv2.line(self.result,(w,h),(w,h-15),color,thickness)
            self.retreive_student_details(qr_code_data)
            self.mark_attendance_db()  
        self.display_feed(self.result,1)         
        
    def display_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_view.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui.camera_view.setScaledContents(True)
        
    def stop_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_view.setPixmap(QPixmap())
        self.ui.camera_view.setAlignment(Qt.AlignCenter)
        self.timer.stop()

    def show_info(self, content:str):
        self.ui.label_notification.setText(content)       

    def update_brigthness(self, value):
        self.ui.brightness_value.setText(str(value))
        return value 

    def update_sharpness(self, value):
        self.ui.sharp_value.setText(str(value))
        return value

    def update_contrast(self, value):
        self.ui.contrast_value.setText(str(value))
        return value     


    def start_webcam_cam_one(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_one_id_ip.text()
        system_attached_camera = self.ui.camera_one_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_one)
        self.timer.start(3)

    def update_frame_cam_one(self): 
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_one(self.frame,1)
        
    def display_feed_cam_one(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_1.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_1.setScaledContents(True)
    
    def stop_webcam_cam_one(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_1.setPixmap(QPixmap())
        self.ui.camera_1.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
   
    
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            #self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()    
 

    def start_webcam_cam_two(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_two_id_ip.text()
        system_attached_camera = self.ui.camera_two_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_two)
        self.timer.start(3)

    def update_frame_cam_two(self): 
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_two(self.frame,2)
        
    def display_feed_cam_two(self, image, window=2):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 2:
            self.ui.camera_2.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_2.setScaledContents(True)
    
    def stop_webcam_cam_two(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_2.setPixmap(QPixmap())
        self.ui.camera_2.setAlignment(Qt.AlignCenter)
        self.timer.stop() 


    def start_webcam_cam_three(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_three_id_ip.text()
        system_attached_camera = self.ui.camera_three_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_three)
        self.timer.start(3) 
    
    def update_frame_cam_three(self):  
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_three(self.frame,window=1)
        
    def display_feed_cam_three(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_3.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_3.setScaledContents(True)
    
    def stop_webcam_cam_three(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_3.setPixmap(QPixmap())
        self.ui.camera_3.setAlignment(Qt.AlignCenter)
        self.timer.stop() 


    def start_webcam_cam_four(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_four_id_ip.text()
        system_attached_camera = self.ui.camera_four_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_four)
        self.timer.start(3) 
    
    def update_frame_cam_four(self):  
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_four(self.frame,window=1)
        
    def display_feed_cam_four(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_4.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_4.setScaledContents(True)
    
    def stop_webcam_cam_four(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_4.setPixmap(QPixmap())
        self.ui.camera_4.setAlignment(Qt.AlignCenter)
        self.timer.stop()    

class Splash_screen(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_MainWindow()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.main.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()

    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter +=1

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Splash_screen()  
    sys.exit(application.exec_()) 