################################################################################
##
## BY: Asamaning REDOLF
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

from packages.root import *
from packages.date import *
from packages.misc import *
from packages.mail import *
from packages.pyqt import *
from packages.model import *
from packages.system import *
from packages.camera import *
from packages.hasher import *
from utils.structure import *
from packages.report import *
from packages.startup import *
from packages.globals import *
from packages.computing import *
from packages.processing import *
from packages.connection import *
from packages.authorities import *

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_dashboard()
        self.saveTimer = QTimer()
        self.timer = QTimer()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QPixmap.fromImage(self.resource_path('icon.ico')))
        self.ui.label.setScaledContents(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        #########################################################################################
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())    
        #########################################################################################

        #########################################################################################
        self.ui.btn_close.clicked.connect(self.application_exit)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        # self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        self.ui.btn_clear_label.clicked.connect(self.loadUi_file)
        #########################################################################################

        #########################################################################################################
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_admin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.admin))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.database))
        self.ui.btn_consolidation_report.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.merge_report))
        self.ui.btn_report.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report))
        self.ui.btn_sink_data.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_help_link.clicked.connect(self.help_url)

        ##########################################################################################################

        #########################################################################################################
        self.piechart = Piechart()
        self.barchart = Barchart()
        self.line_graph = Line_plot()
        ########################################################################################################
        self.set_sender_details()
        self.show_pages_based_role()
        #########################################################################################
        self.config = Configuration()
        self.application_icon(self.config,'Configuration')
        
        self.restapi = RESTAPI()
        self.application_icon(self.restapi,'API')
        self.ui.btn_open_database.clicked.connect(lambda: self.restapi.show())

        self.settings = Settings()
        self.application_icon(self.settings,'Settings')
        self.ui.btn_settings.clicked.connect(lambda: self.settings.show())

        self.merge = CentralDatabase()
        self.ui.btn_merge_connection.clicked.connect(lambda: self.merge.show())
        self.application_icon(self.merge,'Consolidation')

        self.mail = Mail()
        self.application_icon(self.mail,'Mail')
        self.ui.btn_mail_report_or_data.clicked.connect(lambda: self.mail.show())

        self.data_view = DataView()
        self.application_icon(self.data_view,'Values')
        self.ui.btn_generated_data.clicked.connect(lambda: self.data_view.show())
        self.ui.btn_generated_data_local.clicked.connect(lambda: self.data_view.show())

        self.http_response = HTTPResponse()
        self.application_icon(self.http_response,'Response')
        self.ui.btn_http_error_view.clicked.connect(lambda: self.http_response.show())
        
        self.user = User()
        self.application_icon(self.user,'Profile')
        self.ui.btn_login_user.clicked.connect(lambda: self.user.show())
        details=self.user_last_seen(login_reference)

        self.user.setProfile(
            account_firstname,
            account_lastname,
            account_contact,
            account_mail,
            account_status,
            account_role,
            self.visits_count(),
            details[0],
            details[1],
            login_reference)
        self.set_session()
        self.user.profileImage(f'C:\\ProgramData\\iAttend\\data\\cache\\images\\administrators\\{login_reference}.png',self.resource_path('image.jpg'))
        self.insert_thread()
        
        self.camera_4 = Camera_Four()
        self.application_icon(self.camera_4,'Camera 4')
        self.ui.btn_camera.clicked.connect(lambda: self.camera_4.show())

        self.camera_3 = Camera_Three()
        self.application_icon(self.camera_3,'Camera 3')
        self.ui.btn_camera.clicked.connect(lambda: self.camera_3.show())

        self.camera_2 = Camera_Two()
        self.application_icon(self.camera_2,'Camera 2')
        self.ui.btn_camera.clicked.connect(lambda: self.camera_2.show())

        self.camera_1 = Camera_One()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_1.show())
        self.ui.btn_camera.clicked.connect(self.camera_config)

        self.login = Authentication()
        self.application_icon(self.login,'Login')
        self.ui.btn_logout.clicked.connect(self.logout)
        ############################################################################################


        ############################################################################################
        self.ui.btn_connect_detect.clicked.connect(self.start_webcam)
        self.ui.btn_connect_detect.pressed.connect(self.connect_to_camera)
        self.ui.btn_disconnect.clicked.connect(self.stop_webcam)
        ############################################################################################

        #############################################################################################
        self.ui.btn_search_page.clicked.connect(self.query_database_for_data)
        self.ui.search_page_date.dateTimeChanged.connect(self.start_date_on_search_page)
        self.ui.search_page_date_2.dateTimeChanged.connect(self.end_date_on_search_page)
        self.ui.report_date.dateTimeChanged.connect(self.start_report_date)
        self.ui.report_date_2.dateTimeChanged.connect(self.stop_report_date)
        self.ui.btn_reload.clicked.connect(self.clear_fields_on_search_page)
        self.ui.btn_csv.clicked.connect(self.export_data_to_csv)
        self.ui.btn_json.clicked.connect(self.export_data_to_json)
        ##############################################################################################


        ###############################################################################################
        self.ui.brigthness.valueChanged.connect(self.update_brigthness)
        self.ui.sharpness.valueChanged.connect(self.update_sharpness)
        self.ui.contrast.valueChanged.connect(self.update_contrast)

        self.ui.brightness_value.setText(str(self.ui.brigthness.value()))
        self.ui.sharp_value.setText(str(self.ui.sharpness.value()))
        self.ui.contrast_value.setText(str(self.ui.contrast.value()))
        ##################################################################################################

        ##################################################################################################
        self.ui.btn_load.clicked.connect(self.data_visualization)
        self.ui.btn_load.pressed.connect(self.change_load_text)
        self.ui.report_start_date.textChanged.connect(self.report_start_date_value_change)
        self.ui.btn_refresh.clicked.connect(self.refresh_report_page)
        self.ui.btn_save.clicked.connect(self.save_report)
        #################################################################################################

        completer = QCompleter(self.read_text_file(self.resource_path('programs.txt')))
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.search_box.setCompleter(completer)

        self.ui.btn_remove_combox_item.clicked.connect(self.remove_item_from_comboBox)
        self.ui.btn_scan_range.clicked.connect(self.camera_thread)
        self.ui.btn_batch_browse.clicked.connect(self.browse_batch_data)
        self.ui.btn_send_mail.clicked.connect(self.send_mail)
        self.ui.btn_batch_mail.clicked.connect(self.send_code_thread)

        self.ui.btn_user_fetch.pressed.connect(self.set_load_user_text)
        self.ui.btn_user_fetch.clicked.connect(self.load_user_from_api)
        self.ui.btn_user_register.clicked.connect(self.register_user)
        self.ui.btn_user_status.clicked.connect(self.update_user_status)
        self.ui.btn_user_update.clicked.connect(self.update_user_details)
        self.ui.btn_user_clear.clicked.connect(self.clear_user_details)
        self.ui.btn_user_search.clicked.connect(self.search_user)
        self.ui.btn_export_data.clicked.connect(self.export_user_data)
        self.ui.user_start_date_widget.dateTimeChanged.connect(self.user_page_stard_date)
        self.ui.user_end_date_widget.dateTimeChanged.connect(self.user_page_end_date)
        self.ui.btn_mail_user_details.clicked.connect(self.send_account_detail)
        self.ui.btn_generate_code.clicked.connect(self.generate_code_print)
        self.ui.btn_find_filesearch.clicked.connect(self.search_for_code)
        self.ui.btn_print_code.clicked.connect(self.print_code)

        load_data(self.resource_path('structure.json'))
        load_colleges(self.resource_path('structure.json'))

        self.set_curent_dates()
        self.set_endpoints_colleges()
        self.get_central_database_properties()
        self.ui.db_consolidation_date.dateTimeChanged.connect(self.start_date_for_consolidation)
        self.ui.db_consolidation_date_2.dateTimeChanged.connect(self.end_date_for_consolidation)
        self.ui.btn_consolidation_load.clicked.connect(self.load_merge_data)
        self.ui.btn_consolidation_partition.clicked.connect(self.partition_strategy)
        self.ui.btn_consolidation_test.clicked.connect(self.database_test)
        self.ui.btn_consolidation_upload.clicked.connect(self.push_data)
        self.ui.btn_consolidation_update.clicked.connect(self.update_merge_connection_properties)

        self.ui.query_parameter.addItems(self.read_partitions(self.get_root_path('partition\\partition.txt')))
        self.ui.merge_query_parameter.addItems(self.read_partitions(self.get_root_path('partition\\partition.txt')))
        self.ui.merge_query_parameter.addItem('Facility')
        self.ui.report_colleges.addItems(load_colleges(self.resource_path('structure.json')))
        self.ui.report_colleges.activated.connect(self.load_college_faculties_report)
        self.ui.report_faculties.activated.connect(self.load_colleges_report)
        self.ui.btn_load_tables.clicked.connect(self.load_database_tables)
        self.load_college_faculties_report()
        self.load_colleges_report()
        
        self.ui.btn_merge_load.clicked.connect(self.merge_report_generate)
        self.ui.btn_merge_load.pressed.connect(self.change_merge_load_text)
        self.ui.btn_merge_save.clicked.connect(self.merge_report)

        self.ui.btn_search_student.clicked.connect(self.get_student_record_from_api)
        self.ui.btn_search_student.pressed.connect(self.search_student_text)
        self.ui.btn_insert_new_student_record.clicked.connect(self.insert_new_student_record)

        self.check_in_mode = True
        self.start_time = current.now()
        
        # ,QDateTime,QDate,QTime
        ##################################################################################################

    def application_icon(self,widget,title):
        self.icon =QIcon(self.resource_path('icon.ico'))
        widget.setWindowIcon(self.icon)
        widget.setWindowTitle(title)
         
    ############################## Central Reporting #############################
    def change_merge_load_text(self):
        table_name=self.merge.get_table_name()
        if table_name:
            self.ui.btn_merge_load.setText('Loading...')
            self.ui.btn_merge_load.setIcon(QIcon(u":/icons/asset/loader.svg"))    
        pass
    
    def merge_report_generate(self):
        if self.ui.merge_pie_chart.isChecked():
            self.merge_piechart_generate()
            self.ui.btn_merge_load.setText('Load')
            self.ui.btn_merge_load.setIcon(QIcon(u":/icons/asset/download.svg"))
        elif self.ui.merge_bar_chart.isChecked():
            self.merge_barchart_generate()
            self.ui.btn_merge_load.setText('Load')
            self.ui.btn_merge_load.setIcon(QIcon(u":/icons/asset/download.svg"))
        else:
            self.ui.btn_merge_load.setText('Load')
            self.ui.btn_merge_load.setIcon(QIcon(u":/icons/asset/download.svg"))

    def get_merge_plot_properties(self,hearder:str):
        title = f"{hearder} {self.ui.merge_query_parameter.currentText()}"
        chart_title=self.get_plot_parameter(value=self.ui.merge_chart_title.text(),default=title,type='text')
        figure_area=self.get_plot_parameter(value=self.ui.merge_figure_area.text(),default=10,type='number')
        bar_width=self.get_plot_parameter(value=self.ui.merge_bar_width.text(),default=8,type='number')
        bar_width= (bar_width/10)
        dpi=self.get_plot_parameter(value=self.ui.merge_dpi.text(),default=200,type='number')
        startangle=self.get_plot_parameter(value=self.ui.merge_start_angle.text(),default=0,type='number')
        pctdistance=self.get_plot_parameter(value=self.ui.merge_pctdist.text(),default=4,type='number')
        pctdistance = (pctdistance/10)
        labeldistance=self.get_plot_parameter(value=self.ui.merge_pie_ldist.text(),default=105,type='number')
        labeldistance = (labeldistance/100)
        return chart_title,figure_area,bar_width,dpi,startangle,pctdistance,labeldistance

    def merge_piechart_generate(self):
        colors=self.shuffle_list(self.get_read_colors_file(self.resource_path('colors.txt')))
        properties=self.get_merge_plot_properties('Grouped By')
        self.alert = AlertDialog()
        path = self.get_visualize_path()
        table_name=self.merge.get_table_name()
        if table_name:
            data = self.query_database_with_merge_parameter()
            if len(data[0])>=1:
                self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))
                self.piechart.piechart(data=data,title=properties[0],colors=colors[:len(data[0])],startangle=properties[4],
                area=properties[1],dpi=properties[3],pctdistance=properties[5],labeldistance=properties[6],
                xlabel=f"Total records: {self.calculate_records_total(data[1])}")
                self.ui.merge_plot_area.setPixmap(QPixmap.fromImage(path+'piechart.png'))
                self.ui.merge_plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        else:
            self.alert.content("Oops! test database connection\nto load tables...")
            self.alert.show()

    def merge_barchart_generate(self):
        colors=self.shuffle_list(self.get_read_colors_file(self.resource_path('colors.txt')))
        properties=self.get_merge_plot_properties('Grouped By')
        self.alert = AlertDialog()
        path = self.get_visualize_path()
        y_label= 'Number of students'
        table_name=self.merge.get_table_name()
        if table_name:
            data = self.query_database_with_merge_parameter()
            if len(data[0])>=1:
                self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))
                self.barchart.bar_plot_single_view(y_values=data[1],x_labels=data[0],
                bar_width=properties[2],y_label=y_label,x_label=f"Total records: {self.calculate_records_total(data[1])}",
                colors=colors[:len(data[0])],title=f"{properties[0]}",area=properties[1],dpi=properties[3])
                self.ui.merge_plot_area.setPixmap(QPixmap.fromImage(path+'barchart.png'))
                self.ui.merge_plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        else:
            self.alert.content("Oops! test database connection\nto load tables...")
            self.alert.show()
    
    def query_distinct_merge_parameter(self,database_column):
        table_name=self.merge.get_table_name()
        return f"SELECT DISTINCT {database_column} FROM {table_name}"

    def count_distinct_merge_parameter(self,database_column,parameter):
        table_name=self.merge.get_table_name()
        return f"SELECT COUNT({database_column}) FROM {table_name} WHERE {database_column}={parameter}"

    def get_database_merge_field(self):
        dictionary=self.map_query_parameter_to_db_field()
        return dictionary.get(self.ui.merge_query_parameter.currentText())

    def query_database_with_merge_parameter(self):
        if self.ui.merge_query_parameter.currentText()=="Facility":
            query_param = "facility_used"
        else:
            query_param=self.get_database_merge_field()
        query_result = self.merge_report_data(self.query_distinct_merge_parameter(query_param))
        result_list= []
        for item in query_result: 
            result_list.append(item[0])
        total:list = []
        for item in result_list:
            parameter = self.date_formater(item)
            sub_count = self.merge_report_data(self.count_distinct_merge_parameter(query_param,parameter))
            total.append(sub_count[0][0])
        department:list = []
        if query_param=='student_program':
            for item in query_result:
                item = str(item[0]).split(' ')
                department.append(item[2][0:4].upper()) 
                if 'OF' in department:
                    index = department.index('OF')
                    department[index] = 'OPT'
            return department,total
        else:
            return result_list,total

    def merge_report_data(self,query:str):
        db,db_cursor = self.merge.merge_cursor()
        details = []
        cursor = db_cursor.execute(query)
        cursor = db_cursor.fetchall()
        db.commit()
        db_cursor.close()
        if cursor:
            for item in cursor:
                details.append(item)
        return details

    def merge_report(self):
        filename = self.ui.merge_file_name.text()
        date=current.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        transformed_name=filename+date
        self.alert = AlertDialog()
        if self.ui.merge_bar_chart.isChecked():
            if filename:
                self.barchart.save_chart(transformed_name)
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert.content("Oops! please provide file name")
                self.alert.show()         
        elif self.ui.merge_pie_chart.isChecked():
            if filename:
                self.piechart.save_chart(transformed_name)
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert.content("Oops! please provide file name")
                self.alert.show() 

    ############################## Central Reporting END #############################


    ############################## Data consolidation #############################

    def load_colleges_report(self):
        report_departments = get_dept(self.resource_path('structure.json'),self.ui.report_colleges.currentText(),self.ui.report_faculties.currentText())
        self.ui.report_departments.clear()
        self.ui.report_departments.addItems(report_departments)
        self.ui.report_colleges.activated.connect(self.load_college_faculties_report)

    def load_college_faculties_report(self):
        faculties=load_faculties(self.resource_path('structure.json'),self.ui.report_colleges.currentText())
        self.ui.report_faculties.clear()
        self.ui.report_faculties.addItems(faculties)
        report_departments = get_dept(self.resource_path('structure.json'),self.ui.report_colleges.currentText(),self.ui.report_faculties.currentText())
        self.ui.report_departments.clear()
        self.ui.report_departments.addItems(report_departments)

    def shuffle_list(self,data: list):
        shuffled = np.random.permutation(data)
        return shuffled

    def get_read_colors_file(self,path):
        colors_list = []
        with open(path,'r') as data:
            colors=data.read().replace('\n','')
            colors = colors.split(',')
            for color in colors:
                color = '#'+color
                colors_list.append(color)
            return np.random.permutation(colors_list)

    def get_database_field(self):
        dictionary=self.map_query_parameter_to_db_field()
        return dictionary.get(self.ui.query_parameter.currentText())

    def map_query_parameter_to_db_field(self):
        query_parameter = self.read_partitions(self.get_root_path('partition\\partition.txt'))
        database_fields=self.read_partitions(self.get_root_path('partition\\database_fields.txt'))
        return dict(zip(query_parameter,database_fields))
        
    def get_root_path(self,relative_path):
        root_path = 'C:\\ProgramData\\iAttend\\data\\'
        return os.path.join(root_path,relative_path)

    def read_partitions(self,path):
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read().split(',')
            return details

    def date_formater(self,date):
        start_date="\'{}\'".format(date)
        return start_date

    def consolidation_mail_details(self):
        data=load_data('C:\\ProgramData\\iAttend\\data\\email_details\\consolidation.json')
        return data['sender'],data['subject'],data['mail'],data['password']

    def consolidation_mail_content(self,facility_name,total_records,date_fetched,current_account):
        date = current.now().strftime("%a %b %d, %Y,")
        time_ = time.strftime("%I:%M:%S %p")
        path = 'C:\\ProgramData\\iAttend\\data\\email_details\\consolidation_content.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read()
                details = str(details).replace('stamp',f"{date} {time_}").replace('facility',facility_name).replace('value',total_records).replace('date',date_fetched).replace('Username',current_account)
            return details

    def push_data(self):
        self.alert = AlertDialog()
        facility = self.ui.db_consolidation_facility.text()
        tablename = self.ui.database_tables.currentText()
        try: 
            properties = self.merge_database_properties()
            results=self.transform_data(self.load_merge_data(),facility)
            partition = self.validate_field("^[0-9]+$",self.ui.db_consolidation_partition.text())
            facility = self.ui.db_consolidation_facility.text()
            if results and partition and facility and tablename: 
                batch_size=self.compute_push_strategy(self.load_merge_data())
                db,test=self.database_connection_test(properties)
                cursor = db.cursor()
                cursor.execute(user_database(properties[4]))
                for record in range(0,len(results),batch_size):
                    self.ui.db_consolidation_notification.setText("Pushing records to server\nin progress....")
                    cursor.executemany(f"INSERT INTO {tablename}(student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability,facility_used) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                    results[record:record+batch_size])
                    db.commit()
                current_account = f"{account_firstname} {account_lastname}"
                receiver = self.ui.db_consolidation_mail.text() 
                records_date=self.load_merge_dates()
                content = self.consolidation_mail_content(facility,str(len(results)),records_date,current_account)
                if self.connected_to_internet()==True and receiver !="":
                    self.mail=UserMailThread(details=self.consolidation_mail_details(),mail_content=content,receiver=receiver)
                    self.mail.start()
                self.alert.content("Pushed "+str(len(results))+" records to server\nMail sent to administrator..")
                self.alert.show()
                self.application_logs(f'Push records to central database -> successfully')  
            else:
                self.alert.content("Oops! records or partition strategy\nfacility/table name not set!")
                self.alert.show()
        except Exception as e:
            self.alert.content(str(e))
            self.application_logs(f'Push records to central database -> {str(e)}')
            self.alert.show()
          
    def transform_data(self, records:list, facility: str):
        data_list = []        
        for record in range(len(records)):
            data_list.append(list(records[record])+[facility])
        return tuple(data_list)

    def get_central_database_properties(self):
        properties=load_data('C:\\ProgramData\\iAttend\\data\\properties\\central_database_connection_propeties.json')
        self.ui.db_consolidation_hostname.setText(properties['hostname'])
        self.ui.db_consolidation_port.setText(properties['port'])
        self.ui.db_consolidation_username.setText(properties['username'])
        self.ui.db_consolidation_password.setText(properties['password'])
        self.ui.db_consolidation_database.setText(properties['database'])

    def validate_merge_database_fields(self):
        properties_list =  self.merge_database_properties()
        data_list = []
        empty_list = []
        for field in properties_list:
            if field:
                data_list.append(field)
            else:
               empty_list.append(field)
        return data_list,empty_list

    def update_merge_connection_properties(self):
        self.alert = AlertDialog()
        path = 'C:\\ProgramData\\iAttend\\data\\properties\\central_database_connection_propeties.json'
        data_list,empty_list=self.validate_merge_database_fields()
        data_list = [data_list[2],data_list[3],data_list[0],data_list[1],data_list[4]]
        if len(empty_list) == 0:
            self.connection_properties(path,data_list)
            self.alert.content("Hey! database properties updated......")
            self.alert.show()
        else:
            self.alert.content("Oops! empty  values not allowed......")
            self.alert.show()

    def connection_properties(self,path,properties):
        with open(path,'r') as content:
            update = json.load(content) 
            update['username'] = properties[0]
            update['password'] = properties[1]
            update['hostname'] = properties[2]
            update['port'] = properties[3]
            update['database'] = properties[4]
            with open(path,'w') as content:
                json.dump(update, content, indent=4)
            content.close()

    def load_database_tables(self):
        self.alert = AlertDialog()
        try:
            properties = self.merge_database_properties()
            db,test=self.database_connection_test(properties)
            cursor=db.cursor()
            cursor.execute("SHOW TABLES")
            results = cursor.fetchall()
            tables = []
            for row in results:
                tables.append(row[0])
            self.ui.database_tables.clear()
            self.ui.database_tables.addItems(tables)
        except:
            self.alert.content(test)
            self.application_logs(f'Load tables central database connection <Push records> -> {test}')
            self.alert.show()
            
    def database_test(self):
        self.alert = AlertDialog()
        properties = self.merge_database_properties()
        valid,invalid = self.validate_merge_database_fields()
        if len(invalid)==0:
            db,test=self.database_connection_test(properties)
            self.application_logs(f'Central database connection test -> {test}')
            self.alert.content(test)
            self.alert.show()
        else:
            self.alert.content("Oops! set all database properties...")
            self.alert.show()
            
    def merge_database_properties(self):
        host = self.ui.db_consolidation_hostname.text()
        port = self.ui.db_consolidation_port.text()
        user = self.ui.db_consolidation_username.text()
        password = self.ui.db_consolidation_password.text()
        database = self.ui.db_consolidation_database.text()
        return host, port, user, password, database

    def database_connection_test(self,properties: list):
        try:
            connection_status:bool = ("Connected to database...")
            db=connector.connect(host=properties[0],port=properties[1],user=properties[2],password=properties[3],database=properties[4]) 
            return db,connection_status
        except Exception as e:
            return "Oops",str(e)
        
    def compute_push_strategy(self,results):
        return (len(results)//int(self.ui.db_consolidation_partition.text()))
    
    def partition_strategy(self):
        self.alert = AlertDialog()
        results=self.load_merge_data()
        number = self.ui.db_consolidation_partition.text()
        partition = self.validate_field("^[0-9]+$",number)
        if results and partition:
            data=self.compute_push_strategy(results)
            self.alert.content("Pushing "+str(data)+" records per batch\n Number of batches: "+str(number))
            self.alert.show()
        else:
            self.alert.content("Oops! provide data and range\nto perform this operation...")
            self.alert.show()
             
    def consolidation_table(self,details: list):
        self.ui.merge_table.setAutoScroll(True)
        self.ui.merge_table.setAutoScrollMargin(2)
        self.ui.merge_table.setTabKeyNavigation(True)
        self.ui.merge_table.setRowCount(len(details))
        self.ui.merge_table.verticalHeader().setVisible(True)
        self.ui.merge_table.setColumnWidth(2,350)
        self.ui.merge_table.setColumnWidth(0,100)
        self.ui.merge_table.setColumnWidth(1,100)
        self.ui.merge_table.setColumnWidth(1,140)
        self.ui.merge_table.setColumnWidth(4,250)
        self.ui.merge_table.setColumnWidth(5,100)
        self.ui.merge_table.setColumnWidth(6,100)
        row_count = 0
        for data in details:
            self.ui.merge_table.setItem(row_count,0,QTableWidgetItem(str(data[0])))
            self.ui.merge_table.setItem(row_count,1,QTableWidgetItem(str(data[1])))
            self.ui.merge_table.setItem(row_count,2,QTableWidgetItem(str(data[2])))
            self.ui.merge_table.setItem(row_count,3,QTableWidgetItem(str(data[3])))
            self.ui.merge_table.setItem(row_count,4,QTableWidgetItem(str(data[4])))
            self.ui.merge_table.setItem(row_count,5,QTableWidgetItem(str(data[5])))
            self.ui.merge_table.setItem(row_count,6,QTableWidgetItem(str(data[6])))
            row_count = row_count+1

    def load_merge_dates(self):
        start=self.date_formater(self.ui.db_consolidation_start.text())
        stop=self.date_formater(self.ui.db_consolidation_stop.text())
        if self.ui.db_fetch_all.isChecked(): 
            return 'All records fetched from database'
        elif start and not stop:
            return self.reconstruct_date(start)
        elif start and stop:
            return f'{self.reconstruct_date(start)}-{self.reconstruct_date(stop)}'

    def load_merge_data(self):
        self.alert = AlertDialog()
        start=self.date_formater(self.ui.db_consolidation_start.text())
        stop=self.date_formater(self.ui.db_consolidation_stop.text())
        if self.ui.db_fetch_all.isChecked():
            results=self.query_cache_data_list("SELECT student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability FROM tb_attendance")
            self.consolidation_table(results)
            self.ui.db_consolidation_notification.setText("Total records fetched: "+str(len(results)))
            return results
        elif self.ui.db_consolidation_start.text() and self.ui.db_consolidation_stop.text():
            print("in start and stop")
            if self.ui.db_consolidation_start.text() <= self.ui.db_consolidation_stop.text():
                results=self.query_cache_data_list(f"SELECT student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability FROM tb_attendance WHERE date_stamp BETWEEN {start} AND {stop}")
                self.consolidation_table(results)
                self.ui.db_consolidation_notification.setText("Total records fetched: "+str(len(results)))
                return results
            else:
                self.alert.content(f"Oops! invalid date range,\nstart date must be less than stop date")
                self.alert.show()
        elif self.ui.db_consolidation_start.text():
            print("in start")
            results=self.query_cache_data_list(f"SELECT student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability FROM tb_attendance WHERE date_stamp={start}")
            self.consolidation_table(results)
            self.ui.db_consolidation_notification.setText("Total records fetched: "+str(len(results)))
            return results
        
    def start_date_for_consolidation(self):
        date = self.ui.db_consolidation_date.date().toPython()
        self.ui.db_consolidation_start.setText(str(date))

    def end_date_for_consolidation(self):
        date = self.ui.db_consolidation_date_2.date().toPython()
        self.ui.db_consolidation_stop.setText(str(date))   

    ############################## Data consolidation END #############################

    def set_endpoints_colleges(self):
        results=load_colleges(self.resource_path('restapi_endpoints.json'))
        self.restapi.set_colleges(results)
        self.settings.set_colleges_settings(results)

    def load_properties_path(self):
        self.resource_path('database_properties.json')       

    def read_text_file(self,path):
        with open(path,'r') as file:
            data_list = []
            programs = file.readlines()
            for program in programs:
                data_list.append(program)
            file.close()
            return data_list
        
    ############################## Helper methods #############################
   
    def application_logs(self,message):
        time =current.now().time().strftime('%I:%M:%S %p')
        date=current.now().date().strftime('%a %b %d %Y')
        filename=current.now().date().strftime('%a_%b_%d_%Y')
        path =Path(f'C:\\ProgramData\\iAttend\\data\\application_logs\\{filename}.txt')
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n[{date}] [{time}]: {message}')
            file.close()

    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path
    
    def set_curent_dates(self):
        self.now = current.now().date()
        curent_date=QDate(self.now.year,self.now.month,self.now.day)
        self.ui.search_page_date.setDate(curent_date)
        self.ui.search_page_date_2.setDate(curent_date)
        self.ui.user_start_date_widget.setDate(curent_date)
        self.ui.user_end_date_widget.setDate(curent_date)
        self.ui.db_consolidation_date.setDate(curent_date)
        self.ui.db_consolidation_date_2.setDate(curent_date)
        self.ui.report_date.setDate(curent_date)
        self.ui.report_date_2.setDate(curent_date)
        self.ui.db_end_date.clear()
        self.ui.user_end_date_field.clear()
        self.ui.user_start_date_field.clear()
        self.ui.db_start_date.clear()
        self.ui.report_start_date.clear()
        self.ui.report_end_date.clear()
        self.ui.db_consolidation_date.clear()
        self.ui.db_consolidation_stop.clear()

    def value_formater(self,value):
        return "\'{}\'".format(value)

    def get_cache_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\cache\\database\\attendance_database_cache.db'

    def query_cache_database(self,query:str):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        cursor.execute(query)
        cursor = cursor.fetchone()
        db.commit()
        details = []
        if cursor:
            for item in cursor:
                details.append(item)
        return details

    def query_cache_data_list(self,query:str):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        cursor.execute(query)
        cursor = cursor.fetchall()
        db.commit()
        details = []
        if cursor:
            for item in cursor:
                details.append(item)
        return details 
        
    def camera_config(self):
        if account_role == admin:
            self.config.show()

    ############################## Helper methods END  #############################


    ############################## User Session methods  #############################

    def show_pages_based_role(self):
        if account_role == analyst:
            self.ui.stackedWidget.setCurrentWidget(self.ui.merge_report)
            self.ui.btn_camera.hide()
            self.ui.btn_admin.hide()
            self.ui.btn_home.hide()
            self.ui.btn_settings.hide()
            self.ui.btn_search.hide()
            self.ui.btn_database.hide()
            self.ui.btn_report.hide()
            self.ui.btn_sink_data.hide()
            self.ui.btn_consolidation_report.hide()
            self.ui.auto_check_in_check_out.hide()
            self.ui.spinBox.hide()
            self.ui.checkin.hide()
            self.ui.checkout.hide()
            self.ui.scan_status.hide()
        elif account_role == user:
            self.ui.frame.setMinimumHeight(580)
            self.ui.frame.setMaximumHeight(580)
            self.ui.btn_admin.hide()
            self.ui.btn_settings.hide()
            self.ui.btn_consolidation_report.hide()
        
    def application_exit(self):
        self.close()
        self.set_log_out_session()
        self.http_response.close()
        self.camera_1.close()
        self.camera_2.close()
        self.camera_3.close()
        self.camera_4.close()
        self.data_view.close()
        self.merge.close()
        self.mail.close()
        self.user.close()
        self.config.close()
        self.login.show()

    def logout(self):
        self.alert = AlertDialog()
        try:
            self.set_log_out_session()
            self.close()
            self.http_response.close()
            self.config.close()
            self.camera_1.close()
            self.camera_2.close()
            self.camera_3.close()
            self.camera_4.close()
            self.data_view.close()
            self.merge.close()
            self.mail.close()
            self.user.close()
            self.restapi.close()
            self.application_logs("Authentication page shown.....")
            self.login.show()
        except Exception as e:
            self.alert.content(str(e))
            self.alert.show()

    def compute_duration(self,time_in: str, time_out: str):
        from datetime import date,time
        time_in = time_in.split(':')
        seconds = str(time_in[2]).split(' ')[0]
        time_in = time(hour=int(time_in[0]),minute=int(time_in[1]),second=int(seconds))
        time_out =time_out.split(':')
        seconds = str(time_out[2]).split(' ')[0]
        time_out = time(int(time_out[0]),int(time_out[1]),int(seconds))
        date_ = date(1,1,1)
        duration=current.combine(date_,time_out)-current.combine(date_,time_in)
        return str(duration)

    def set_log_out_session(self):
        date="\'{}\'".format(current.now().date().strftime("%Y-%m-%d"))
        _date=current.now().date().strftime("%Y-%m-%d")
        duration="\'{}\'".format("00:00:00")
        reference = "\'{}\'".format(login_reference)
        self.alert = AlertDialog()
        try:
            db = sqlite3.connect(self.get_cache_path())
            my_cursor = db.cursor() 
            my_cursor.execute(f"SELECT user_login,user_duration FROM tb_user_session WHERE user_reference={reference} AND user_date={date} AND user_duration={duration}") 
            cursor=my_cursor.fetchall()
            db.commit()

            details=[]
            if cursor is not None:
                for data in cursor:
                    details.append(data)
            time_out =current.now().time().strftime('%H:%M:%S %p')
            new_time_out =current.now().time().strftime('%H:%M:%S %p')
            _time_out =current.now().time().strftime('%H:%M:%S %p')
            
            new_duration = self.compute_duration(time_in=str(details[0][0]),time_out=time_out)
            _duration = new_duration
            new_duration="\'{}\'".format(new_duration)
            new_time_out="\'{}\'".format(new_time_out)
            if str(details[0][1]) == "00:00:00":
                my_cursor.execute(f"UPDATE tb_user_session SET user_logout={new_time_out} , user_duration={new_duration} WHERE user_reference={reference} AND user_date={date} AND user_duration={duration}")
                db.commit()
                my_cursor.execute(f"DELETE FROM tb_user_session_last_seen WHERE user_reference={reference}")
                db.commit()
                my_cursor.execute("INSERT INTO tb_user_session_last_seen (user_reference,user_username,user_date,user_login,user_logout,user_duration) VALUES (?,?,?,?,?,?)",
                (login_reference,login_username,_date,str(details[0][0]),_time_out,_duration))
                db.commit()
                my_cursor.close()
                db.close()
            pass
        except Exception as e:
            self.alert.content(str(e))
            self.application_logs("Current login user logged out unsuccessfully")
            self.application_logs("Current login user logged with unupdated session details")
            self.application_logs(str(e))
            self.alert.show()

    def user_last_seen(self,reference:str):
        db = sqlite3.connect(self.get_cache_path())
        _cursor = db.cursor()
        cursor=_cursor.execute(f"SELECT user_date,user_logout,user_duration FROM tb_user_session_last_seen WHERE user_reference ={reference}")
        cursor= _cursor.fetchall()
        db.commit()
        last_seen_info = []
        if cursor:
            for data in cursor:
                last_seen_info.append(data)
        if len(last_seen_info)>=1:
            details=str(last_seen_info[0][0]).split('-')
            details = datetime.date(int(details[0]),int(details[1]),int(details[2])).strftime("%a %d %b, %Y")
            time = last_seen_info[0][1]
            duration = last_seen_info[0][2]
            return details+' @ '+time , duration          
        else:
            return "Oops! first timer", "00:00:00"
            
    def insert_thread(self):
        self.pool = QThreadPool()
        self.work = SendThread(self.insert_user_session)
        self.pool.start(self.work)

    def insert_user_session(self):   
        session=self.set_user_session()
        self.alert = AlertDialog()
        try:
            db = sqlite3.connect(self.get_cache_path())
            cursor = db.cursor()
            cursor.execute("INSERT INTO tb_user_session (user_reference,user_username,user_date,user_login,user_logout,user_duration) VALUES (?,?,?,?,?,?)",
            (session.reference,session.username,session.date,session.login,session.logout,session.duration))
            db.commit() 
        except Exception as e:
            self.alert.content(str(e))
            self.alert.show()

    def set_user_session(self):
        session = Session(
            login_reference,
            login_username,
            str(current.now().date().strftime("%Y-%m-%d")),
            str(current.now().time().strftime("%H:%M:%S %p")),
            str(current.now().time().strftime("%H:%M:%S %p")),
            "00:00:00")
        return session

    def visits_count(self):
        results=self.query_cache_data_list("select count(user_reference) from tb_user_session where user_reference="+login_reference+" and user_duration NOT LIKE '%00:00:00%'")
        return results[0][0]

    def set_session(self):
        self.ui.label_6.setText("session@"+login_username+" "+current.now().time().strftime("%I:%M:%S %p"))
    
    ############################## User Session methods  #############################
    
    
    ############################## User Account #############################

    def export_user_data(self):
        self.alert = AlertDialog()
        table=self.ui.admin_table.item(0,0)
        date=current.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iAttend\\data\\exports\\csv\\login_user'+date+'.csv'
        if table:
            details=self.search_user()
            data = pd.DataFrame(details)
            data.to_csv(path,sep=',',index=False,
            header=['Id', 'User_reference', 'User_username', 'User_date','User_login', 'User_logout', 'User_duration'])
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert.content("Oops! you have no data to export...")
            self.alert.show()

    def user_page_stard_date(self):
        date_ = self.ui.user_start_date_widget.date().toPython()
        self.ui.user_start_date_field.setText(str(date_))

    def user_page_end_date(self):
        date_ = self.ui.user_end_date_widget.date().toPython()
        self.ui.user_end_date_field.setText(str(date_))

    def set_load_user_text(self):
        if self.ui.user_search.text():
            self.ui.btn_user_fetch.setText("Loading...")
            self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/loader.svg"))
        else:
            self.ui.btn_user_fetch.setText("Load User")
            self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/download.svg"))

    def render_user_interface(self, details:json):
        self.ui.user_firstname.setText(details['firstname'])
        self.ui.user_middlename.setText(details['othername'])
        self.ui.user_lastname.setText(details['lastname'])
        self.ui.user_reference.setText(details['reference'])
        
    def load_user_from_api(self):
        self.loadUi_file()
        self.alert = AlertDialog()
        reference=self.ui.user_search.text()
        url= self.restapi.get_field_text()
        url = str(url).replace('reference',reference)
        if reference and self.validate_field('^[0-9]+$',reference):
            try:
                request_body = requests.get(url)
                student_data=request_body.json()
                if request_body.status_code == 302:
                    self.render_user_interface(student_data)
                    self.ui.btn_user_fetch.setText("Load User")
                    self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/download.svg"))
                    self.save_student_image(reference,request_body,'administrators')
                    self.load_image_from_storage(reference,self.ui.user_image,'administrators')
                else:
                    self.ui.btn_user_fetch.setText("Load User")
                    self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/download.svg"))
                    self.alert.content(str(student_data))
                    self.alert.show()
            except Exception as e:
                self.ui.btn_user_fetch.setText("Load User")
                self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/download.svg"))
                self.alert.content(str(e))
                self.alert.show()
        else:
            self.alert.content("Oops! invalid reference number...")
            self.alert.show()
       
    ################ Some refactyoring to be done #################################   
    def search_user(self):
        self.alert = AlertDialog()
        reference = self.ui.user_search.text()
        if reference:
            if self.validate_field('^[0-9]+$',reference):
                details = self.query_cache_data_list(f"SELECT * FROM tb_user_session WHERE user_reference={reference}")
                user = self.query_cache_data_list(f"SELECT * FROM tb_user_details WHERE user_reference={reference}")
                status = self.query_cache_data_list(f"SELECT user_status, user_role FROM tb_user_credentials WHERE user_reference={reference}")
                if len(details) > 0:
                    self.render_user_data(details)
                else:  
                    self.alert.content(f"Oops! user with {reference} has no sessions.")
                    self.alert.show()
                if len(user) > 0: 
                    self.render_user_details(user,status[0][0],status[0][1])
                    self.load_image_from_storage(reference,self.ui.user_image,'administrators')
                return details
            else:
                self.alert.content("Oops! no details found for\nthe reference provided.")
                self.alert.show()
        elif self.ui.user_start_date_field.text() and self.ui.user_end_date_field.text():
            start_date = self.ui.user_start_date_field.text()
            start_date="\'{}\'".format(start_date)
            stop_date = self.ui.user_end_date_field.text()
            stop_date="\'{}\'".format(stop_date)
            if start_date <= stop_date:
                details = self.query_cache_data_list(f"SELECT * FROM tb_user_session WHERE user_date BETWEEN {start_date} AND {stop_date}")
                self.render_user_data(details)
                return details
            else:
                self.alert.content(f"Oops! invalid date range,\nstart date must be less than stop date")
                self.alert.show()  
        elif self.ui.user_start_date_field.text() and not reference:
            date=self.ui.user_start_date_field.text()
            date_stamp="\'{}\'".format(date)
            details = self.query_cache_data_list(f"SELECT * FROM tb_user_session WHERE user_date={date_stamp}")
            self.render_user_data(details) 
            return details   
        else:
            details = self.query_cache_data_list("SELECT * FROM tb_user_session")
            self.render_user_data(details)
            return details
            
    def render_user_details(self,details:list,status:str,role:str):
        if len(details) > 0:
            name = str(details[0][2]).split(' ')
            self.ui.user_firstname.setText(name[0])
            self.ui.user_middlename.setText(name[1])
            self.ui.user_lastname.setText(details[0][3])
            self.ui.user_reference.setText(details[0][1])
            self.ui.user_contact.setText(details[0][4])
            self.ui.user_email.setText(details[0][5])
            self.ui.user_role.setCurrentText(role)
            self.ui.user_status.setCurrentText(str(status))
        else:
            pass
 
    def load_image_from_storage(self,reference,label,folder):
        directory = f'C:\\ProgramData\\iAttend\\data\\cache\\images\\{folder}'
        filename = f'{reference}.png'
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file == filename:
                    image_path=os.path.join(root, filename)
                    label.setPixmap(QPixmap.fromImage(image_path))
                    label.setScaledContents(True)
                    break
                else:
                    label.setPixmap(QPixmap.fromImage(self.resource_path('image')))
                    label.setScaledContents(True)
            else:
                continue
            break

    def render_user_data(self,details:list):
        self.ui.admin_table.setAutoScroll(True)
        self.ui.admin_table.setAutoScrollMargin(2)
        self.ui.admin_table.setTabKeyNavigation(True)
        self.ui.admin_table.setRowCount(len(details))
        self.ui.admin_table.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            date=str(data[3]).split('-')
            date = datetime.date(int(date[0]),int(date[1]),int(date[2])).strftime("%a %d %b, %Y")
            self.ui.admin_table.setItem(row_count,0,QTableWidgetItem(str(data[2])))
            self.ui.admin_table.setItem(row_count,1,QTableWidgetItem(str(date)))
            self.ui.admin_table.setItem(row_count,2,QTableWidgetItem(str(data[4])))
            self.ui.admin_table.setItem(row_count,3,QTableWidgetItem(str(data[5])))
            self.ui.admin_table.setItem(row_count,4,QTableWidgetItem(str(data[6])))
            row_count = row_count+1
    
    def clear_user_details(self):
        self.ui.user_firstname.setText("")
        self.ui.user_middlename.setText("")
        self.ui.user_lastname.setText("")
        self.ui.user_reference.setText("")
        self.ui.user_contact.setText("")
        self.ui.user_email.setText("")
        self.ui.user_image.setPixmap(u":/icons/asset/image.svg")
        self.ui.user_image.setScaledContents(False)


    def update_user_status(self):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        self.alert = AlertDialog()
        try:
            if self.ui.user_reference.text():
                cursor.execute("UPDATE tb_user_credentials SET user_status=? WHERE user_reference=?",
                (self.ui.user_status.currentText(),self.ui.user_reference.text()))
                db.commit()
                cursor.close()
                self.alert.content(f"User with {self.ui.user_reference.text()} status updated\nto {self.ui.user_status.currentText()}")
                self.alert.show()
            else:
                self.alert.content(f"Oops! no reference number\nprovided...")
                self.alert.show()            
        except Exception as e:
            self.alert.content(str(e))
            self.alert.show()

    def update_user_details(self):
        user = self.set_user_details()
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        self.alert = AlertDialog()
        try:
            if self.ui.user_reference.text() and self.ui.user_contact.text() and self.ui.user_email.text():
                cursor.execute("UPDATE tb_user_details SET user_contact =?, user_role =?, user_mail =? WHERE user_reference=?",
                (user.contact,user.role,user.mail,user.reference))
                db.commit()
                cursor.close()
                self.alert.content(f"User with {self.ui.user_reference.text()} this details\nupdated")
                self.alert.show()
            else:
                self.alert.content(f"Oops! provide all details in other\nto perform the update...")
                self.alert.show()
        except Exception as e:
            self.alert.content(str(e))
            self.alert.show() 

    def get_mail_content_new_account(self,lastname,username,reference,password):
        path = 'C:\\ProgramData\\iAttend\\data\\email_details\\new_account_mail.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read()
                details = str(details).replace('Name',lastname).replace('account_username',username).replace('account_reference',reference).replace('account_password',password).replace('College_name','CoS Team')
            return details

    def get_registration_details(self):
        data=load_data('C:\\ProgramData\\iAttend\\data\\email_details\\details.json')
        data['subject'] = "Account Details"
        return data['sender'],data['subject'],data['mail'],data['password']

    def send_account_detail(self):
        self.alert = AlertDialog()
        credentials=self.set_user_credentials()
        user = self.set_user_details()
        content = self.get_mail_content_new_account(str(user.lastname),str(credentials.username),str(credentials.reference),str(user.mail))
        if self.ui.user_reference.text() and self.ui.user_firstname.text() and self.ui.user_contact.text() and self.ui.user_email.text():
            receiver = self.ui.user_email.text() 
            if self.connected_to_internet()==True:
                self.mail=UserMailThread(details=self.get_registration_details(),mail_content=content,receiver=receiver)
                self.mail.start()
                self.alert.content(f"Registered account details sent to\n{self.ui.user_email.text()}")
                self.alert.show()
            else:
                self.alert.content("Oops! mail not sent check\ninternet connection")
                self.alert.show()
        else:
            self.alert.content("Oops! can't mail empty user details.")
            self.alert.show()
        
    def register_user(self):
        self.alert = AlertDialog()
        user = self.set_user_details()
        credentials = self.set_user_credentials()
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        if self.ui.user_reference.text() and self.ui.user_contact.text() and self.ui.user_firstname.text():
            details=self.query_cache_database("SELECT * FROM tb_user_details WHERE user_reference="+"\'{}\'".format(user.reference)+" AND user_contact="+"\'{}\'".format(user.contact))
            if not details:
                try: 
                    cursor.execute("INSERT INTO tb_user_details (user_reference,user_firstname,user_lastname,user_contact,user_mail) VALUES (?,?,?,?,?)",
                    (user.reference,user.firstname,user.lastname,user.contact,user.mail))   
                    cursor.execute("INSERT INTO tb_user_credentials (user_reference,user_username,user_role,user_status,user_password) VALUES (?,?,?,?,?)",
                    (credentials.reference,credentials.username,credentials.role,credentials.status,credentials.password))
                    db.commit()
                    cursor.close()
                    self.alert.content(f"User with {user.reference} registered successfully.")
                    self.alert.show()
                except Exception as e:
                    self.alert.content(str(e))
                    self.alert.show()
            else:
                self.alert.content(f"User with {user.reference} already exist.")
                self.alert.show() 
        else:
            self.alert.content(f"Oops! something wrong.")
            self.alert.show()

    def set_user_details(self):
        user = UserDetails(
            self.ui.user_firstname.text()+" "+self.ui.user_middlename.text(),
            self.ui.user_lastname.text(),
            self.ui.user_reference.text(),
            self.ui.user_contact.text(),
            self.ui.user_email.text(),
        )
        return user

    def set_user_credentials(self):
        user = self.set_user_details()
        password_hash = hash_password(user.mail)
        credentials = LoginUser(
            user.reference,
            user.lastname+str(math.floor(np.random.random(1)*1000)),
            self.ui.user_role.currentText(),
            self.ui.user_status.currentText(),
            password_hash
        )
        return credentials
    
    ############################## User Account Registration END #############################


    ############################## Batch Insert Data #############################
    
    def send_code_thread(self):
        student_data_path = self.ui.batch_browse.text()
        self.alert = AlertDialog()
        if student_data_path:
            if self.connected_to_internet()==True:
                self.pool = QThreadPool()
                self.work = SendThread(self.generate_code_and_send)
                self.pool.start(self.work)
            else:
                self.alert.content("Oops! check internet connectivity...")
                self.alert.show()
        else:
            self.alert.content("Oops! invalid file path or check\ninternet connectivity...")
            self.alert.show()
              
    def generate_code_and_send(self):
        student_data_path = self.ui.batch_browse.text() 
        self.threadPool = QThreadPool()
        content = self.get_mail_content()
        details = self.get_email_details()
        with open(student_data_path,'r') as data:
            student_data = csv.reader(data)
            student_list = []
            next(data)
            for row in student_data:
                student_list.append(row)
                student = Code(
                    reference=row[4]
                    )
                student_string ={
                    "reference":student.reference,
                    }
                if self.connected_to_internet()==True:
                    student_json=self.convert_to_json(student_string)
                    image = qrcode.make(student_json)
                    image_path='C:\\ProgramData\\iAttend\\data\\qr_code\\'+student.reference+".png"
                    image.save(image_path)
                    content = self.get_mail_content()
                    content=content.replace('name',row[0])
                    self.worker = BatchQRCodeMailThread(details,content,image_path,row[10])
                    self.threadPool.start(self.worker)
                    self.ui.batch_notification.setText("Sending mails in progress...")      
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! please check your internet\nconnection...")
                    self.alert.show()
            self.ui.batch_notification.setText("Mail for valid addresses sent...")
                   
    def convert_to_json(self, student:Student):
        to_json = json.dumps(student)
        return to_json  

    def validate_field(self,pattern,value):
        return bool(re.match(pattern,value))

    def load_batch_data(self):
        results_list = []
        path = batch_file_path
        if path:
            with open(path,'r') as filename:
                data=csv.reader(filename)
                if self.ui.header_check.isChecked():
                    next(data)
                pass
                for student in data:
                    results_list.append(student)
                return results_list

    def batch_table(self, details:list):
        self.ui.tableWidget_batch.setAutoScroll(True)
        self.ui.tableWidget_batch.setAutoScrollMargin(2)
        self.ui.tableWidget_batch.setTabKeyNavigation(True)
        self.ui.tableWidget_batch.setRowCount(len(details))
        self.ui.tableWidget_batch.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget_batch.setItem(row_count,0,QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_batch.setItem(row_count,1,QTableWidgetItem(str(data[1])))
            row_count = row_count+1
        
    def browse_batch_data(self):
        file_type = "CSV Files(*.csv);;Text Files(*.txt)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Documents",file_type)
        global batch_file_path
        if path:
            batch_file_path= path[0]
            self.ui.batch_browse.setText(os.path.basename(path[0]))
            try:
                self.batch_table(self.load_batch_data())
                self.alert = AlertDialog()
                if self.ui.header_check.isChecked():
                    self.alert.content(f"Please the header was skipped...\nTotal count: {len(self.load_batch_data())}")
                else:
                    self.alert.content(f"Total count: {len(self.load_batch_data())}")
                self.alert.show()
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"+str(e)))
                self.alert.show()

    ############################## Batch Insert Data END #############################

    def clear_camera_comboBoxes(self):
        self.ui.comboBox.clear()
        
    def get_active_cameras(self,camera:list):
        self.ui.comboBox.addItems(camera)
        count = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]
        self.ui.scan_range_label.setText("Active camera(s): "+str(len(count)))
        self.ui.label_notification.setText("Done scanning for available cameras...")           

    def camera_thread(self):
        scan_range = self.ui.scan_range.text()
        if self.validate_field('^[1-9]+$',scan_range):
            self.clear_camera_comboBoxes()
            self.ui.scan_range_label.setText('')
            self.active = ActiveCameras(scan_range)
            self.active.start()
            self.active.cameras.connect(self.get_active_cameras)
            self.ui.label_notification.setText("Scanning for available cameras...")
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! no scan range provided\nor invalid input...")
            self.alert.show()
    
    def server_logs(self,source,save_logs):
        date=current.now().date().strftime('%a %b %d %Y')
        path =Path('C:\\ProgramData\\iAttend\\data\\cache\\logs\\'+date+'_history.txt')
        path.touch(exist_ok=True)
        file = open(path)
        time =current.now().time().strftime('%I:%M:%S %p')
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n{source} {time} {save_logs}')
            file.close()     

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

    ############################## Reporting Page Local #######################

    def get_combo_items(self):
        combo_items = []
        for index in range(self.ui.report_faculties.count()):
            combo_items.append(self.ui.report_faculties.itemText(index))
        return combo_items

    def refresh_report_page(self):
        self.ui.chart_title.clear()
        self.ui.report_start_date.clear()
        self.ui.report_end_date.clear()
        self.ui.dpi.clear()
        self.ui.figure_area.clear()
        self.ui.bar_width.clear()
        self.ui.start_angle.clear()
        self.ui.pie_ldist.clear()
        self.ui.pctdist.clear()
        self.ui.file_name.clear()
        self.ui. plot_area.setText('Graph')
                  
    def save_report(self):
        filename = self.ui.file_name.text()
        date=current.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        transformed_name=filename+date
        self.alert = AlertDialog()
        if self.ui.bar_chart.isChecked():
            if self.ui.file_name.text():
                self.barchart.save_chart(transformed_name)
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert.content("Oops! please provide file name")
                self.alert.show()         
        elif self.ui.line_graph.isChecked():
            if self.ui.file_name.text():
                self.line_graph.save_chart(transformed_name)
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert.content("Oops! please provide file name")
                self.alert.show() 
        elif self.ui.pie_chart.isChecked():
            if self.ui.file_name.text():
                self.piechart.save_chart(transformed_name)
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert.content("Oops! please provide file name")
                self.alert.show()  
     
    def reconstruct_date(self,date:str):
        date_value=str(date).split('-')
        date_transformed = datetime.date(int(date_value[0]),int(date_value[1]),int(date_value[2])).strftime("%a %d %b, %Y")
        return date_transformed   
        
    def report_start_date_value_change(self):
        date=self.ui.report_start_date.text()
        if self.ui.line_graph.isChecked():
            self.ui.date_range_comboBox.addItem(date) 

    def report_date(self):
        report_start_date= self.ui.report_start_date.text()
        report_end_date= self.ui.report_end_date.text()
        return report_start_date, report_end_date

    def query_distinct_parameter(self,database_column,first_date_param,second_date_param,query_type):
        first_date_param = self.date_formater(first_date_param)
        second_date_param = self.date_formater(second_date_param)
        if query_type=="date":
            return f"SELECT DISTINCT {database_column} FROM tb_attendance WHERE date_stamp={first_date_param}"
        elif query_type=="range":
            return f"SELECT DISTINCT {database_column} FROM tb_attendance WHERE date_stamp BETWEEN {first_date_param} AND {second_date_param}"
        else:
            return f"SELECT DISTINCT {database_column} FROM tb_attendance"

    def count_distinct_parameter(self,database_column,first_date_param,second_date_param,query_type,parameter):
        first_date_param = self.date_formater(first_date_param)
        second_date_param = self.date_formater(second_date_param)
        if query_type=="date":
            return f"SELECT COUNT({database_column}) FROM tb_attendance WHERE {database_column}={parameter} AND date_stamp={first_date_param}"
        elif query_type=="range":
            return f"SELECT COUNT({database_column}) FROM tb_attendance WHERE {database_column}={parameter} AND date_stamp BETWEEN {first_date_param} AND {second_date_param}"
        else:
            return f"SELECT COUNT({database_column}) FROM tb_attendance WHERE {database_column}={parameter}"
    
    def query_database_with_parameter(self,date,range,type):
        query_param=self.get_database_field()
        if self.ui.query_parameter.currentText() == "Faculty":
            query_result = [(item,) for item in self.get_combo_items()]
        else:
            query_result = self.query_cache_data_list(self.query_distinct_parameter(query_param,date,range,type))
        result_list= []
        for item in query_result: 
            result_list.append(item[0])
        total:list = []
        for item in result_list:
            parameter = self.date_formater(item)
            sub_count = self.query_cache_data_list(self.count_distinct_parameter(query_param,date,range,type,parameter))
            total.append(sub_count[0][0])
        department:list = []
        if query_param =='student_program':
            for item in query_result:
                item = str(item[0]).split(' ')
                department.append(item[2][0:4].upper()) 
                if 'OF' in department:
                    index = department.index('OF')
                    department[index] = 'OPT'
            return department,total
        else:
            return result_list,total

    def line_plot_values(self,database_column,query_param,partition):
        results_list = []
        dates = sorted(self.get_dates_for_line_plot())
        for date in range(len(dates)):
            date_value=self.date_formater(dates[date])
            if partition=='Faculty' or partition=='Department' or partition=='College':
                results=self.query_cache_data_list(f"SELECT COUNT({database_column}) FROM tb_attendance where date_stamp={date_value} AND {database_column}={query_param}")
                results_list.append(results)
            else:
                results=self.query_cache_data_list(f"SELECT COUNT({database_column}) FROM tb_attendance where date_stamp={date_value}")
                results_list.append(results)
        return results_list

    def get_actual_plot_values(self,data: list):
        values: list = []
        for item in data:
            values.append(item[0][0])
        return values

    def get_dates_for_line_plot(self):
        setattr(self.ui.date_range_comboBox,'allItems',
        lambda:[self.ui.date_range_comboBox.itemText(i) for i in range(self.ui.date_range_comboBox.count())])
        return self.ui.date_range_comboBox.allItems()

    def remove_item_from_comboBox(self):
        self.ui.date_range_comboBox.removeItem(self.ui.date_range_comboBox.currentIndex())

    def get_plot_parameter(self,value,default,type):
        if type=='number':
            if self.validate_field('^[0-9]+$',value):
                return int(value)
            else:
                return default
        elif type=='text':
            if value:
                return value
            else:
                return default

    def get_plot_properties(self,hearder:str):
        title = f"{hearder} {self.ui.query_parameter.currentText()}"
        chart_title=self.get_plot_parameter(value=self.ui.chart_title.text(),default=title,type='text')
        figure_area=self.get_plot_parameter(value=self.ui.figure_area.text(),default=10,type='number')
        bar_width=self.get_plot_parameter(value=self.ui.bar_width.text(),default=8,type='number')
        bar_width= (bar_width/10)
        dpi=self.get_plot_parameter(value=self.ui.dpi.text(),default=200,type='number')
        startangle=self.get_plot_parameter(value=self.ui.start_angle.text(),default=0,type='number')
        pctdistance=self.get_plot_parameter(value=self.ui.pctdist.text(),default=4,type='number')
        pctdistance = (pctdistance/10)
        labeldistance=self.get_plot_parameter(value=self.ui.pie_ldist.text(),default=105,type='number')
        labeldistance = (labeldistance/100)
        return chart_title,figure_area,bar_width,dpi,startangle,pctdistance,labeldistance

    def reconstruct_date_report(self,date:str):
        date_value=str(date).split('-')
        date_transformed = datetime.date(int(date_value[0]),int(date_value[1]),int(date_value[2])).strftime("%b %d, %Y")
        return date_transformed 

    def get_visualize_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\reports\\visualize\\'

    def barchart_plots(self):
        colors=self.shuffle_list(self.get_read_colors_file(self.resource_path('colors.txt')))
        properties=self.get_plot_properties('Grouped By')
        self.alert = AlertDialog()
        report_date = self.report_date()
        path = self.get_visualize_path()
        y_label= 'Number of students'
        if not self.ui.report_start_date.text() and not self.ui.report_end_date.text():
            data = self.query_database_with_parameter('','','')
            if len(data[0])>=1:
                self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))
                self.barchart.bar_plot_single_view(y_values=data[1],x_labels=data[0],
                bar_width=properties[2],y_label=y_label,x_label=f"Total records: {self.calculate_records_total(data[1])}",
                colors=colors[:len(data[0])],title=f"{properties[0]}",area=properties[1],dpi=properties[3])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'barchart.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        elif self.ui.report_start_date.text() and self.ui.report_end_date.text():
            if self.ui.report_start_date.text() <= self.ui.report_end_date.text():
                data = self.query_database_with_parameter(date=report_date[0],range=report_date[1],type='range')
                if len(data[0])>=1: 
                    self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))     
                    self.barchart.bar_plot_single_view(y_values=data[1],x_labels=data[0],
                    bar_width=properties[2],y_label=y_label,x_label=f"values",colors=colors[:len(data[0])],
                    title=f"{properties[0]} [{self.reconstruct_date_report(report_date[0])} - {self.reconstruct_date_report(report_date[1])}]",
                    area=properties[1],dpi=properties[3])
                    self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'barchart.png'))
                    self.ui.plot_area.setScaledContents(True)
                else:
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()
            else:
                self.alert.content(f"Oops! invalid date range,\nstart date must be less than stop date")
                self.alert.show()
        elif self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.query_database_with_parameter(date=report_date[0],range='',type='date')
                if len(data[0])>=1:
                    self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))
                    self.barchart.bar_plot_single_view(y_values=data[1],x_labels=data[0],
                    bar_width=properties[2],y_label=y_label,x_label=f"values",
                    colors=colors[:len(data[0])],title=f"{properties[0]} [{self.reconstruct_date_report(report_date[0])}]",
                    area=properties[1],dpi=properties[3])
                    self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'barchart.png'))
                    self.ui.plot_area.setScaledContents(True)
                else:
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()

    def report_piechart(self):
        colors=self.shuffle_list(self.get_read_colors_file(self.resource_path('colors.txt')))
        properties=self.get_plot_properties('Grouped By')
        self.alert = AlertDialog()
        report_date = self.report_date()
        path = self.get_visualize_path()
        if not self.ui.report_start_date.text() and not self.ui.report_end_date.text():
            data = self.query_database_with_parameter('','','')
            if len(data[0])>=1:
                self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))
                self.piechart.piechart(data=data,title=properties[0],colors=colors[:len(data[0])],startangle=properties[4],
                area=properties[1],dpi=properties[3],pctdistance=properties[5],labeldistance=properties[6],
                xlabel=f"Total records: {self.calculate_records_total(data[1])}")
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'piechart.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        elif self.ui.report_start_date.text() and self.ui.report_end_date.text():
            if self.ui.report_start_date.text() <= self.ui.report_end_date.text():
                data = self.query_database_with_parameter(date=report_date[0],range=report_date[1],type='range')
                if len(data[0])>=1:
                    self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))      
                    self.piechart.piechart(data=data,title=f"{properties[0]} [{self.reconstruct_date_report(report_date[0])} - {self.reconstruct_date_report(report_date[1])}]",
                    colors=colors[:len(data[0])],startangle=properties[4],area=properties[1],dpi=properties[3],
                    pctdistance=properties[5],labeldistance=properties[6])
                    self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'piechart.png'))
                    self.ui.plot_area.setScaledContents(True)
                else:
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()
            else:
                self.alert.content(f"Oops! invalid date range,\nstart date must be less than stop date")
                self.alert.show() 
        elif  self.ui.report_start_date.text() and not self.ui.report_end_date.text():
            data = self.query_database_with_parameter(date=report_date[0],range='',type='date')
            if len(data[0])>=1:
                self.data_view.set_data(json.dumps(dict(zip(data[0],data[1])),indent=4))
                self.piechart.piechart(data=data,title=f"{properties[0]} [{self.reconstruct_date_report(report_date[0])}]",
                colors=colors[:len(data[0])],startangle=properties[4],area=properties[1],dpi=properties[3],
                pctdistance=properties[5],labeldistance=properties[6],xlabel=f"Total records: {self.calculate_records_total(data[1])}")
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'piechart.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
    
    def line_plot(self):
        colors=self.shuffle_list(self.get_read_colors_file(self.resource_path('colors.txt')))
        colors=colors[:1]
        marker=self.shuffle_list(self.read_partitions(self.resource_path('markers.txt')))
        marker=marker[:1]
        properties=self.get_plot_properties('Plotted By')
        self.alert = AlertDialog()
        path = self.get_visualize_path()
        y_label= 'Number of students'
        query_param=self.get_database_field() 
        report_faculties=self.date_formater(self.ui.report_faculties.currentText())
        report_departments=self.date_formater(self.ui.report_departments.currentText())
        report_college=self.date_formater(self.ui.report_colleges.currentText())
        query_value = self.ui.query_parameter.currentText()
        dates = sorted(self.get_dates_for_line_plot())
        if query_value == "Faculty":
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_faculties,'Faculty'))
            if len(data)>=1:
                self.data_view.set_data(json.dumps(dict(zip(dates,data)),indent=4))
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"Total records: {self.calculate_records_total(data)}",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        elif query_value == "Department":
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_departments,'Department'))
            if len(data)>=1:
                self.data_view.set_data(json.dumps(dict(zip(dates,data)),indent=4))
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"Total records: {self.calculate_records_total(data)}",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        elif query_value == "College":
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_college,'College'))
            if len(data)>=1:
                self.data_view.set_data(json.dumps(dict(zip(dates,data)),indent=4))
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"Total records: {self.calculate_records_total(data)}",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        else:
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_departments,''))
            if len(data)>=1:
                self.data_view.set_data(json.dumps(dict(zip(dates,data)),indent=4))
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"Total records: {self.calculate_records_total(data)}",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()

    def calculate_records_total(self,records):
       return reduce(lambda x, y: x + y, records)

    def change_load_text(self):
        self.ui.btn_load.setText('Loading...')
        self.ui.btn_load.setIcon(QIcon(u":/icons/asset/loader.svg"))

    def data_visualization(self):
        if self.ui.pie_chart.isChecked():
            self.report_piechart()
            self.ui.btn_load.setText('Load')
            self.ui.btn_load.setIcon(QIcon(u":/icons/asset/download.svg"))
        elif self.ui.bar_chart.isChecked():
            self.barchart_plots()
            self.ui.btn_load.setText('Load')
            self.ui.btn_load.setIcon(QIcon(u":/icons/asset/download.svg"))
        elif self.ui.line_graph.isChecked():
            self.line_plot()
            self.ui.btn_load.setText('Load')
            self.ui.btn_load.setIcon(QIcon(u":/icons/asset/download.svg"))
        else:
            self.ui.btn_load.setText('Load')
            self.ui.btn_load.setIcon(QIcon(u":/icons/asset/download.svg"))

    ############################## Reporting Page Local END #######################

    ################## Search Page ####################################################

    def export_data_to_csv(self):
        self.alert = AlertDialog()
        table=self.ui.tableWidget.item(0,0)
        filename= self.ui.search_page_filename.text()
        date=current.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iAttend\\data\\exports\\csv\\'+filename+date+'.csv'
        if table and filename:
            details=self.query_database_for_data()
            data = pd.DataFrame(details)
            data.to_csv(path,sep=',',index=False,
            header=['Generated_Id','Reference','College','Faculty',
            'Department','Category','Nationality','Gender','Disabled','Date',
            'Login','Logout','Duration'])
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert.content("Oops! you have no data or filename\nprovided...")
            self.alert.show()

    def export_data_to_json(self):
        self.alert = AlertDialog()
        table=self.ui.tableWidget.item(0,0)
        filename= self.ui.search_page_filename.text()
        date=current.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iAttend\\data\\exports\\json\\'+filename+date+'.json'
        if table and filename:
            details=self.query_database_for_data()
            data=pd.DataFrame(details,columns=['Generated_Id','Reference','College','Faculty',
            'Department','Category','Nationality','Gender','Disabled','Date','Login','Logout','Duration'])
            data.to_json(path,orient='records',indent=4)
            self.alert.content("Hey! data to exported successfully...")
            self.alert.show()
        else:
            self.alert.content("Oops! you have no data or filename\nprovided...")
            self.alert.show()
        
    def ui_table(self, details: list):
        self.ui.tableWidget.setAutoScroll(True)
        self.ui.tableWidget.setAutoScrollMargin(2)
        self.ui.tableWidget.setTabKeyNavigation(True)
        self.ui.tableWidget.setColumnWidth(0,150)
        self.ui.tableWidget.setColumnWidth(1,80)
        self.ui.tableWidget.setColumnWidth(2,80)
        self.ui.tableWidget.setColumnWidth(3,300)
        self.ui.tableWidget.setColumnWidth(6,80)
        self.ui.tableWidget.setColumnWidth(7,90)
        self.ui.tableWidget.setColumnWidth(9,100)
        self.ui.tableWidget.setColumnWidth(10,100)
        self.ui.tableWidget.setColumnWidth(11,100)
        self.ui.tableWidget.setRowCount(len(details))
        self.ui.tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            date=str(data[9]).split('-')
            program=str(data[4])
            date = datetime.date(int(date[0]),int(date[1]),int(date[2])).strftime("%a %d %b, %Y")
            self.ui.tableWidget.setItem(row_count,0,QTableWidgetItem(str(data[1])))
            self.ui.tableWidget.setItem(row_count,1,QTableWidgetItem(str(data[2])))
            self.ui.tableWidget.setItem(row_count,2,QTableWidgetItem(str(data[3])))
            self.ui.tableWidget.setItem(row_count,3,QTableWidgetItem(program[9:]))
            self.ui.tableWidget.setItem(row_count,4,QTableWidgetItem(str(data[5])))
            self.ui.tableWidget.setItem(row_count,5,QTableWidgetItem(str(data[6])))
            self.ui.tableWidget.setItem(row_count,6,QTableWidgetItem(str(data[7])))
            self.ui.tableWidget.setItem(row_count,7,QTableWidgetItem(str(data[8])))
            self.ui.tableWidget.setItem(row_count,8,QTableWidgetItem(str(date)))
            self.ui.tableWidget.setItem(row_count,9,QTableWidgetItem(str(data[10])))
            self.ui.tableWidget.setItem(row_count,10,QTableWidgetItem(str(data[11])))
            self.ui.tableWidget.setItem(row_count,11,QTableWidgetItem(str(data[12])))
            row_count = row_count+1

    def fetch_details_for_card_view(self):
        self.alert = AlertDialog()
        student_reference=self.value_formater(self.ui.search_box.text())
        results=self.query_cache_data_list(f"SELECT * FROM tb_attendance WHERE student_reference={student_reference}")
        self.ui_table(results)
        if self.ui.search_box.text():
            db_data=self.query_cache_database(f"SELECT * FROM tb_students INNER JOIN tb_student_study_details ON tb_students.student_reference=tb_student_study_details.student_reference WHERE tb_students.student_reference={student_reference}") 
            if len(db_data) > 0:
                start_date = (str(db_data[8])).split(' ')
                student_year=(int(current.now().date().strftime('%Y'))-int(start_date[1]))    
                if student_year <= 1:
                    level = "1st year"
                elif student_year > 1 and student_year <= 2:
                    level = "2nd year"
                elif student_year > 2 and student_year <= 3:
                    level = "3rd year"
                elif student_year > 3 and student_year <= 4:
                    level = "4th year"
                elif student_year > 4 and student_year <= 5:
                    level = "5th year"
                elif student_year > 5 and student_year <= 6:
                    level = "6th year"
                helper = str(db_data[3]).split(" ")
                self.ui.db_firstname.setText(helper[0])
                self.ui.db_middlename.setText(helper[1])
                self.ui.db_lastname.setText(db_data[4])
                self.ui.db_refrence.setText(str(db_data[1]))
                self.ui.db_index.setText(str(db_data[2]))
                self.ui.db_nationality.setText(db_data[5])
                self.ui.dbgender.setText(db_data[6])
                self.ui.db_year.setText(level)
                self.ui.db_validity.setText(db_data[8]+" - "+db_data[9])
                self.ui.db_college.setText(db_data[12])
                self.ui.db_faculty.setText(db_data[13])
                self.ui.db_programe.setText(db_data[14])
                self.ui.db_type.setText(db_data[15])
                self.load_image_from_storage(self.ui.search_box.text(),self.ui.db_image_data,'students')
                return results
            else:
                self.alert.content("Student details not found. Please enter\nyour details to register!")
                self.alert.show()
        else:
            self.alert.content("Oops! search field can't be empty.")
            self.alert.show()

    def query_for_data_by_date_range(self):
        start = self.ui.db_start_date.text()
        start_date="\'{}\'".format(start)
        end = self.ui.db_end_date.text()
        end_date="\'{}\'".format(end)
        results = self.query_cache_data_list("SELECT * FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" AND "+end_date)
        self.ui_table(results)
        return results
    
    def fetch_data_by_program_and_date(self):
        start = self.ui.db_start_date.text()
        start_date="\'{}\'".format(start)
        prog = self.ui.search_box.text()
        program="\'{}\'".format(prog)
        results = self.query_cache_data_list("SELECT * FROM tb_attendance WHERE student_program="+program+" and date_stamp="+start_date)
        self.ui_table(results)
        return results
    
    #search page creterias ###################################################
    def query_database_for_data(self):
        self.alert = AlertDialog()
        if self.ui.db_current_session.isChecked():
            details=self.query_cache_data_list("SELECT * FROM tb_attendance_temp")
            self.ui_table(details)
            return details 
        else:
            if self.ui.checkBox.isChecked():
                if self.ui.search_box.text() and self.ui.db_start_date.text() and  self.ui.db_end_date.text():
                    start = self.ui.db_start_date.text()
                    start_date= self.date_formater(start)
                    end = self.ui.db_end_date.text()
                    end_date=self.date_formater(end)
                    prog = self.ui.search_box.text()
                    program=self.date_formater(prog)
                    if self.ui.db_start_date.text() <= self.ui.db_end_date.text():
                        results_ = self.query_cache_data_list(f"SELECT * FROM tb_attendance WHERE date_stamp BETWEEN {start_date} AND {end_date} AND program={program}")
                        self.ui_table(results_)
                        return results_
                    else:
                        self.alert.content(f"Oops! invalid date range,\nstart date must be less than stop date")
                        self.alert.show()      
                elif self.ui.search_box.text() and self.ui.db_start_date.text():
                    return self.fetch_data_by_program_and_date()
                else:
                    program = self.ui.search_box.text()
                    program = "Dept. of "+program
                    program = "\'{}\'".format(program)
                    program=program.replace('\n','')
                    details = self.query_cache_data_list(f"SELECT * FROM tb_attendance WHERE student_program={program}")
                    self.ui_table(details)
                    return details
            else:
                if self.ui.db_start_date.text() and  self.ui.db_end_date.text():
                    if self.ui.db_start_date.text() <= self.ui.db_end_date.text():
                        return self.query_for_data_by_date_range()
                    else:
                        self.alert.content(f"Oops! invalid date range,\nstart date must be less than stop date")
                        self.alert.show()
                elif self.ui.db_start_date.text():
                    current_date = self.ui.db_start_date.text()
                    current_date = self.date_formater(current_date)
                    results = self.query_cache_data_list(f"SELECT * FROM tb_attendance WHERE date_stamp ={current_date}")
                    self.ui_table(results)
                    return results
                elif self.ui.search_box.text():
                    return self.fetch_details_for_card_view()
                elif self.ui.search_box.text() and self.ui.db_start_date.text() and  self.ui.db_end_date.text():
                    if self.ui.db_start_date.text() <= self.ui.db_end_date.text():
                        self.fetch_details_for_card_view()
                        return self.query_for_data_by_date_range()
                    else:
                        self.alert.content(f"Oops! invalid date range,\nstart date must be less than stop date")
                        self.alert.show() 
                else:
                    details=self.query_cache_data_list("SELECT * FROM tb_attendance")
                    self.ui_table(details)
                    return details 
                        
    def start_date_on_search_page(self):
        date = self.ui.search_page_date.date().toPython()
        self.ui.db_start_date.setText(str(date))

    def end_date_on_search_page(self):
        date = self.ui.search_page_date_2.date().toPython()
        self.ui.db_end_date.setText(str(date))
         
    def clear_fields_on_search_page(self):
        self.ui.db_firstname.setText("Firstname")
        self.ui.db_middlename.setText("Middlename")
        self.ui.db_lastname.setText("Lastname")
        self.ui.db_college.setText("College")
        self.ui.db_refrence.setText("Reference")
        self.ui.db_index.setText("Index")
        self.ui.db_nationality.setText("Nationality")
        self.ui.db_programe.setText("Program")
        self.ui.db_validity.setText("Validity")
        self.ui.db_year.setText("Year")
        self.ui.db_image_data.setPixmap(u":/icons/asset/image.svg")
        self.ui.db_image_data.setScaledContents(False)
        self.ui.db_start_date.setText("")
        self.ui.db_end_date.setText("")

    ##########################################################################################

    def start_report_date(self):
        date_ = self.ui.report_date.date().toPython()
        self.ui.report_start_date.setText(str(date_))

    def stop_report_date(self):
        date_ = self.ui.report_date_2.date().toPython()
        self.ui.report_end_date.setText(str(date_))


    #############################################Registration################################

    def get_email_details(self):
        from_ = self.ui.email_from.text()
        from_email = self.ui.email_sender.text()
        subject = self.ui.email_subject.text()
        password = self.ui.sender_password.text()
        to_address = self.ui.reg_email.text()
        return to_address, subject, from_email, from_, password

    def set_sender_details(self):
        details=self.get_details()
        self.ui.email_from.setText(details[0])
        self.ui.email_sender.setText(details[2])
        self.ui.email_subject.setText(details[1])
        self.ui.sender_password.setText(details[3])
    
    def get_details(self):
        data=load_data('C:\\ProgramData\\iAttend\\data\\email_details\\details.json')
        return data['sender'],data['subject'],data['mail'],data['password']
    
    def get_mail_content(self):
        path = 'C:\\ProgramData\\iAttend\\data\\email_details\\content.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read()
            return details.replace('name',' ')

    def convert_to_json(self, code:Code):
        to_json = json.dumps(code)
        return to_json

    def generate_code_print(self):
        self.alert = AlertDialog()
        reference = self.ui.find_file.text()
        if reference !='':
            code ={"reference":reference}
            code_json=self.convert_to_json(code)
            image = qrcode.make(code_json)
            path = 'C:\\ProgramData\\iAttend\\data\\qr_code\\'+self.ui.find_file.text()+".png"
            image.save(path)
            self.ui.generate_code_label.setPixmap(QPixmap.fromImage(path))
            self.ui.generate_code_label.setScaledContents(True)
            self.ui.find_filename.setText(os.path.basename(path))
            self.ui.find_filepath.setText(path)
        else:
            self.alert.content("Oops! can't generate code with\nempty field...")
            self.alert.show()

    def search_for_code(self):
        self.alert = AlertDialog()
        directory = 'C:\\ProgramData\\iAttend\\data\\qr_code\\'
        filename = self.ui.find_file.text()
        filename = filename+'.png'
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file == filename:
                    image_path=os.path.join(root, filename)
                    self.ui.generate_code_label.setPixmap(QPixmap.fromImage(image_path))
                    self.ui.generate_code_label.setScaledContents(True)
                    self.ui.find_filename.setText(os.path.basename(image_path))
                    self.ui.find_filepath.setText(image_path)
                    image = QImage(image_path)
                    image=image.size()
                    self.ui.image_size.setText(f"{image.width()} x {image.height()}")
                    break
            else:
                continue
            break
        else:
            self.alert.content("Oops! no file with such name found...")
            self.alert.show()

    def print_code(self):
        self.alert = AlertDialog()
        self.printer = QPrinter(QPrinter.HighResolution)
        path = self.ui.find_filepath.text()
        image = QImage(path)
        if path:
            dialog = QPrintDialog(self.printer, self)
            if dialog.exec_() != QPrintDialog.Accepted:
                return
            page_layout = QPageLayout(QPageSize(image.size()), QPageLayout.Portrait, QMarginsF())
            self.printer.setPageLayout(page_layout)
            painter = QPainter()
            painter.begin(self.printer)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            image_size = image.size()
            page_rect = painter.viewport()
            image_rect = QRectF(0, 0, image_size.width()+1000, image_size.height()+1000)
            image_rect.moveTop(page_rect.top())
            painter.drawImage(image_rect, image)
            painter.end()
        else:
            self.alert.content("Oops! select image file for\nprinting...")
            self.alert.show()
            
    def prepare_email(self):
        details = self.get_email_details()
        path = self.ui.find_filepath.text()
        content = self.get_mail_content()
        self.mail = QRCodeMailThread(details,content,path)
        self.mail.start()

    def prepare_email_to_send(self):
        self.alert = AlertDialog()
        if self.connected_to_internet()==True and self.ui.find_filepath.text():
            try:
                self.prepare_email()
                self.alert.content("Hey! mail sent successfully...")
                self.alert.show()
            except Exception as e:
                self.alert.content(str(e))
                self.alert.show()
        else:
            self.alert.content("Oops! something went wrong mail\nnot sent, check internet connection or\ninvalid file path")
            self.alert.show()

    def send_mail(self):
        self.prepare_email_to_send()
 
    def connected_to_internet(self,url='http://www.google.com/', timeout=5):
        try:
            _ = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError:  
            return False
 
    ############################################# Registration End ################################
        

    ############################## Home page ######################################### 

    ############################## Logout session start #########################################

    def compute_logout_duration(self,time_in: str, time_out: str):
        from datetime import date,time
        time_in = time_in.split(':')
        seconds = str(time_in[2]).split(' ')[0]
        time_in = time(hour=int(time_in[0]),minute=int(time_in[1]),second=int(seconds))
        time_out =time_out.split(':')
        seconds = str(time_out[2]).split(' ')[0]
        time_out = time(int(time_out[0]),int(time_out[1]),int(seconds))
        date_ = date(1,1,1)
        duration=current.combine(date_,time_out)-current.combine(date_,time_in)
        return str(duration)

    def query_cache_database_logout(self,qr_code_data):
        data_json = json.loads(qr_code_data)
        student_reference=self.value_formater(data_json['reference'])
        db = sqlite3.connect(self.get_cache_path())
        my_cursor = db.cursor()
        my_cursor.execute(f"SELECT generated_id,student_reference FROM tb_attendance_temp WHERE student_reference={student_reference}")
        cursor= my_cursor.fetchone()
        db.commit()
        results = []
        date="\'{}\'".format(current.now().date().strftime("%Y-%m-%d"))
        if cursor is not None:
            for data in cursor:
                results.append(data)
            cursor=my_cursor.execute(f"SELECT time_in,duration FROM tb_attendance_temp WHERE student_reference={self.value_formater(results[1])} AND date_stamp={date}")
            cursor=my_cursor.fetchall()
            db.commit()
            details = []
            if cursor is not None:
                for data in cursor:
                    details.append(data)
                db.commit()
                if len(details)>0:
                    time_out =current.now().time().strftime('%H:%M:%S %p')
                    date_stamp=current.now().date().strftime('%Y-%m-%d')
                    new_duration = self.compute_logout_duration(time_in=str(details[0][0]),time_out=time_out)
                    self.load_image_from_storage(data_json['reference'],self.ui.image,'students')
                    if str(details[0][1]) == "00:00:00":
                        my_cursor.execute("UPDATE tb_attendance_temp SET time_out= ?, duration= ?  WHERE student_reference=? and date_stamp= ? ",(time_out,new_duration,student_reference,date_stamp))
                        db.commit()
                        winsound.Beep(1000,100)
                        details = my_cursor.execute("SELECT * FROM tb_attendance_temp where student_reference="+student_reference)
                        details=my_cursor.fetchone()
                        my_cursor.execute("INSERT INTO tb_attendance (student_reference,student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability,date_stamp,time_in,time_out,duration) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (details[1],details[2],details[3],details[4],details[5],details[6],details[7],details[8],details[9],details[10],time_out,new_duration))
                        db.commit()
                        my_cursor.execute("DELETE FROM tb_attendance_temp where student_reference="+student_reference)
                        my_cursor.execute("DELETE FROM tb_attendance_last_seen WHERE student_reference="+student_reference)
                        db.commit()
                        winsound.Beep(1000,100)
                        my_cursor.execute("INSERT INTO tb_attendance_last_seen (student_reference,date_stamp,time_in,time_out,duration) VALUES (?,?,?,?,?)",
                        (details[1],details[9],details[10],time_out,new_duration))
                        db.commit()
                        winsound.Beep(1000,100)
                        self.show_info("Hey! your have successfully logged out...")
                    else:
                        winsound.Beep(1000,100)
                        self.show_info("Hey! your have successfully logged out...")
                else:
                    self.show_info(f"Oops! you are already logged out!\nStudent Id: {data_json['reference']}")
        else:
            self.show_info("Oops! attendance details for student\nnot found...")
       
    def log_student_out(self,qr_code_data:str):
        self.query_cache_database_logout(qr_code_data)

    ############################## Logout session end #########################################

    def loadUi_file(self):
        self.ui.firstname.setText("Firstname")
        self.ui.othername.setText("Othername")
        self.ui.lastname.setText("Lastname")
        self.ui.reference.setText("Reference")
        self.ui.index.setText("Index")
        self.ui.college.setText("College")
        self.ui.nationality.setText("Nationality")
        self.ui.validity.setText("Validity")
        self.ui.program.setText("Department")
        self.ui.year.setText("Year")
        self.ui.gender.setText("Gender")
        self.ui.type.setText("Type")
        self.ui.last_in.setText("Duration")
        self.ui.last_out.setText("Last seen")
        self.ui.faculty.setText("Faculty")
        self.ui.image.setPixmap(u":/icons/asset/image.svg")
        self.ui.image.setScaledContents(False)
        self.ui.label_notification.setText("Notification")

    def get_student_details_from_UI(self):
        firstname = self.ui.firstname.text()
        othername =  self.ui.othername.text()
        lastname =  self.ui.lastname.text()
        reference = self.ui.reference.text()
        index = self.ui.index.text()
        nationality = self.ui.nationality.text()
        college = self.ui.college.text()
        type =  self.ui.type.text()
        gender = self.ui.gender.text()
        disabled = student_disability
        department = self.ui.program.text()
        faculty = self.ui.faculty.text()
        validity = self.ui.validity.text()
        return (firstname, othername, lastname, reference, 
        index, nationality,college, type, gender,disabled
        ,department,faculty,validity)
        
    def last_seen(self,reference:str):  
        student_reference=self.value_formater(reference)
        db = sqlite3.connect(self.get_cache_path())
        _cursor = db.cursor()
        cursor=_cursor.execute(f"SELECT date_stamp,time_out,duration FROM tb_attendance_last_seen WHERE student_reference ={student_reference}")
        cursor= _cursor.fetchall()
        db.commit()
        last_seen_info = []
        if cursor:
            for data in cursor:
                last_seen_info.append(data)
        if len(last_seen_info)>=1:
            details=str(last_seen_info[0][0]).split('-')
            details = datetime.date(int(details[0]),int(details[1]),int(details[2])).strftime("%a %d %b, %Y")
            time = last_seen_info[0][1]
            duration = last_seen_info[0][2]
            self.ui.last_out.setText(details+' @ '+time)
            self.ui.last_in.setText(duration)           
        else:
            self.ui.last_out.setText("Oops! first timer")
            self.ui.last_in.setText("00:00:00") 

    def insert_into_cache_db(self,data):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        student_reference=self.value_formater(data[3])
        db_cache=self.query_cache_database("SELECT student_reference FROM tb_students WHERE student_reference="+student_reference)
        if len(db_cache)<=0:
            validity = str(data[12]).split('-')
            cursor.execute("INSERT INTO tb_students(student_reference,student_index,student_firstname,student_lastname,student_nationality,student_gender,student_disability,card_issued_date,card_expiry_date) VALUES (?,?,?,?,?,?,?,?,?)",
            (data[3],data[4],str(data[0]+' '+data[1]),data[2],data[5],data[8],data[9],validity[0],validity[1]))   
            db.commit()
            cursor.execute("INSERT INTO tb_student_study_details(student_reference,student_college,student_faculty,student_program,student_category) VALUES (?,?,?,?,?)",
            (data[3],data[6],data[11],data[10],data[7]))   
            db.commit() 
            return "Added student record to database"     
        else:
             return "Oops! student record to already exist."
                   
    def fetch_data_from_db(self,reference):
        data_json = json.loads(reference)
        student_reference=self.value_formater(data_json['reference'])
        db_cache=self.query_cache_database("SELECT * FROM tb_students INNER JOIN tb_student_study_details ON tb_students.student_reference=tb_student_study_details.student_reference WHERE tb_students.student_reference="+student_reference)
        if len(db_cache) > 0:
            self.server_logs('[CACHED]',db_cache[:2])
            self.update_interface_cache(db_cache)
            self.last_seen(data_json['reference'])
            self.load_image_from_storage(data_json['reference'],self.ui.image,'students')
        else:
            pass

    def search_student_text(self):
        if self.ui.student_reference_field.text():
            self.ui.btn_search_student.setText("Loading...")
            self.ui.btn_search_student.setIcon(QIcon(u":/icons/asset/loader.svg"))
        else:
            self.ui.btn_search_student.setText("Search")
            self.ui.btn_search_student.setIcon(QIcon(u":/icons/asset/search.svg"))      

    def save_student_image(self, reference, response: json, folder: str):
        with open(f"C:\\ProgramData\\iAttend\\data\\cache\\images\\{folder}\\{reference}.png", 'wb') as file:
            file.write(bytes(response.json()["image"]["data"]["data"]))
        file.close()

    def get_student_record_from_api(self):
        self.loadUi_file()
        reference_ = self.ui.student_reference_field.text()
        self.alert = AlertDialog()
        student_reference=self.value_formater(reference_)
        db_cache=self.query_cache_database("SELECT * FROM tb_students INNER JOIN tb_student_study_details ON tb_students.student_reference=tb_student_study_details.student_reference WHERE tb_students.student_reference="+student_reference)
        if len(db_cache) > 0:
            self.server_logs('[CACHED]',db_cache[:2])
            self.update_interface_cache(db_cache)
            self.last_seen(reference_)
            self.load_image_from_storage(reference_,self.ui.image,'students')
            self.ui.btn_search_student.setText("Search")
            self.ui.btn_search_student.setIcon(QIcon(u":/icons/asset/search.svg"))
        else:
            details_url= self.restapi.get_field_text()
            url = str(details_url).replace('reference',reference_)
            if reference_:
                try:
                    request_body = requests.get(url)
                    student_data=request_body.json()
                    if request_body.status_code == 302:
                        self.update_interface(student_data)
                        self.save_student_image(reference_,request_body,'students')
                        self.ui.btn_search_student.setText("Search")
                        self.ui.btn_search_student.setIcon(QIcon(u":/icons/asset/search.svg"))
                        self.load_image_from_storage(reference_,self.ui.image,'students')
                        self.httpError(f"Status code {request_body.status_code}\n{request_body.headers}")
                    else:
                        self.ui.btn_search_student.setText("Search")
                        self.ui.btn_search_student.setIcon(QIcon(u":/icons/asset/search.svg"))
                        self.alert.content(str(student_data['message']))
                        self.alert.show()
                except Exception as e:
                    self.ui.btn_search_student.setText("Search")
                    self.ui.btn_search_student.setIcon(QIcon(u":/icons/asset/search.svg"))
                    self.httpError(str(e))
            else:
                self.alert.content("Oops! invalid reference number...")
                self.alert.show()
   
    def insert_new_student_record(self):
        self.alert = AlertDialog()
        if self.ui.reference.text() != 'Reference' and self.ui.firstname.text() != 'Firstname':
            record = self.get_student_details_from_UI()
            response=self.insert_into_cache_db(data=record)
            self.alert.content(response)
            self.alert.show()
        else:
            self.alert.content(response)
            self.alert.show()
        
    def update_interface_cache(self, db_data):
        if db_data:
            start_date = (str(db_data[8])).split(' ')
            student_year=(int(current.now().date().strftime('%Y'))-int(start_date[1]))
            validity = str(db_data[8])+' - '+str(db_data[9])  
            if student_year <= 1:
                level = "1st year"
            elif student_year > 1 and student_year <= 2:
                level = "2nd year"
            elif student_year > 2 and student_year <= 3:
                level = "3rd year"
            elif student_year > 3 and student_year <= 4:
                level = "4th year"
            elif student_year > 4 and student_year <= 5:
                level = "5th year"
            elif student_year > 5 and student_year <= 6:
                level = "6th year"
            global student_disability
            student_disability=str(db_data[7])
            firstname_othername = str(db_data[3]).split(" ")
            self.ui.firstname.setText(firstname_othername[0])
            self.ui.othername.setText(firstname_othername[1])
            self.ui.lastname.setText(db_data[4])
            self.ui.reference.setText(str(db_data[1]))
            self.ui.index.setText(str(db_data[2]))
            self.ui.nationality.setText(db_data[5])
            self.ui.gender.setText(str(db_data[6]))
            self.ui.validity.setText(validity)
            self.ui.year.setText(level)
            self.ui.college.setText(str(db_data[12]))
            self.ui.faculty.setText(str(db_data[13]))
            self.ui.program.setText(str(db_data[14]))
            self.ui.type.setText(str(db_data[15]))
        else:
            self.loadUi_file()
            self.show_info("Oops! student not found. Please register!") 
                    
    def update_interface(self, request_body_json: json):
        if request_body_json:
            start_date = (str(request_body_json['validity'])).split('-')[0]
            start_date = start_date.split(' ')[1]
            student_year=(int(current.now().date().strftime('%Y'))-int(start_date))
            if student_year <= 1:
                level = "1st year"
            elif student_year > 1 and student_year <= 2:
                level = "2nd year"
            elif student_year > 2 and student_year <= 3:
                level = "3rd year"
            elif student_year > 3 and student_year <= 4:
                level = "4th year"
            elif student_year > 4 and student_year <= 5:
                level = "5th year"
            elif student_year > 5 and student_year <= 6:
                level = "6th year"
            self.ui.firstname.setText(request_body_json['firstname'])
            self.ui.othername.setText(request_body_json['othername'])
            self.ui.lastname.setText(request_body_json['lastname'])
            self.ui.reference.setText(request_body_json['reference'])
            self.ui.index.setText(request_body_json['index'])
            self.ui.nationality.setText(request_body_json['nationality'])
            self.ui.gender.setText(request_body_json['gender'])
            self.ui.validity.setText(request_body_json['validity'])
            self.ui.year.setText(level)
            self.ui.college.setText(request_body_json['college'])
            self.ui.faculty.setText(request_body_json['faculty'])
            self.ui.program.setText(str(request_body_json['department']))
            self.ui.type.setText(request_body_json['category'])
        else:
            self.loadUi_file()
            self.show_info("Oops! student not found. Please register!") 

    def httpError(self,response):
        self.http_response.set_response(response)
        
    def attendance_data(self):
        attendance = Attendance(
            self.ui.reference.text(),
            self.ui.college.text(),
            self.ui.faculty.text(),
            self.ui.program.text(),
            self.ui.type.text(),
            self.ui.nationality.text(),
            self.ui.gender.text(),
            student_disability,
            str(current.now().date().strftime("%Y-%m-%d")),
            str(current.now().time().strftime("%H:%M:%S %p")),
            str(current.now().time().strftime("%H:%M:%S %p")),
            "00:00:00" )
        return attendance

    def mark_attendance_db(self):
        cache_db = sqlite3.connect(self.get_cache_path())
        cursor = cache_db.cursor()
        attendance=self.attendance_data()
        details = []
        date="\'{}\'".format(current.now().date().strftime("%Y-%m-%d"))
        student_reference=self.value_formater(self.ui.reference.text())
        if self.ui.reference.text() != "Reference" and self.ui.reference.text() !="" :
            data=cursor.execute(f"SELECT student_reference,date_stamp FROM tb_attendance_temp WHERE student_reference={student_reference} AND date_stamp={date}")
            data=cursor.fetchone()
            if data:
                for item in data:
                    details.append(item)
                cache_db.commit()
            if not details:
                cursor.execute("INSERT INTO tb_attendance_temp(student_reference,student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability,date_stamp,time_in,time_out,duration) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (attendance.student_reference,attendance.student_college,attendance.student_faculty,attendance.student_program,attendance.student_category,attendance.student_nationality,attendance.student_gender,attendance.student_disability,attendance.date_stamp,attendance.time_in,attendance.time_out,attendance.duration))
                cache_db.commit()
            elif details:
                winsound.Beep(self.ui.frequency.value(),self.ui.duration.value())
                self.show_info("Attendance taken, you can proceed!\nNext person please...")
            else:
                 self.show_info("Oops! something went wrong...")

    def connect_to_camera(self):
        if self.ui.comboBox.currentText():
            self.show_info("Connecting to selected device this may\ntake some few seconds...")
        pass

    def start_webcam(self):
        self.show_alert = AlertDialog()
        if self.ui.comboBox.currentText():
            system_attached_camera = self.ui.comboBox.currentText()
            camera_id = int(system_attached_camera)
            self.system_capture = VideoCapture(camera_id)       
            if self.system_capture:    
                self.capture = VideoCapture(camera_id)                  
                self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
                self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
                self.timer.timeout.connect(self.update_frame)
                self.show_info("Connected to selected device\nsuccessfully...") 
                self.timer.start(3)
            else:
                self.stop_webcam
                self.show_alert.content("Oops! check the camera for\nconnetion or is already in use.")  
                self.show_alert.show()
            
        else:
            self.show_alert.content("Oops! your have no active cameras available")  
            self.show_alert.show()
            
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

        ps.putBText(self.result,self.ui.scan_status.text(),text_offset_x=10,text_offset_y=457,vspace=5,hspace=5, font_scale=0.5,
        background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX) 
    
        self.elapsed_time = current.now() - self.start_time
        if self.ui.auto_check_in_check_out.isChecked():
            if self.elapsed_time >= timedelta(seconds=self.ui.spinBox.value()):
                self.check_in_mode = not self.check_in_mode
                if self.check_in_mode:
                    winsound.Beep(500,900)
                    self.ui.scan_status.setText("Check-in activated")
                else:
                    winsound.Beep(500,900)
                    self.ui.scan_status.setText("Check-out activated") 
                self.start_time = current.now()       
        else:
            if self.ui.checkin.isChecked():
                self.ui.scan_status.setText("Check-in activated")
            elif self.ui.checkout.isChecked():
                self.ui.scan_status.setText("Check-out activated") 
            else:
                self.ui.scan_status.setText("No tracking")

        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)

        ps.putBText(self.result,f'FPS: {self.capture.get(cv2.CAP_PROP_FPS)}',text_offset_x=self.result.shape[1]-90,text_offset_y=457,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)

        
        if self.ui.auto_check_in_check_out.isChecked():
            self.text = "Automation Mode"
            ps.putBText(self.result,self.text,text_offset_x=270,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
                background_RGB=(0,255,0),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        else:
            self.text = "Manual Mode"
            ps.putBText(self.result,self.text,text_offset_x=280,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
                background_RGB=(0,255,0),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)

        self.now = current.now()
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
                if self.ui.auto_check_in_check_out.isChecked():
                    if self.check_in_mode:
                        self.ui.scan_status.setText("Check-in activated")
                        self.fetch_data_from_db(qr_code_data)
                        self.mark_attendance_db()
                    else:
                        self.ui.scan_status.setText("Check-out activated")
                        self.fetch_data_from_db(qr_code_data)
                        self.log_student_out(qr_code_data)
                else:
                    if self.ui.checkin.isChecked():
                        self.ui.scan_status.setText("Check-in activated")
                        self.fetch_data_from_db(qr_code_data)
                        self.mark_attendance_db()
                    elif self.ui.checkout.isChecked():
                        self.ui.scan_status.setText("Check-out activated")
                        self.fetch_data_from_db(qr_code_data)
                        self.log_student_out(qr_code_data)
                    else:
                        self.ui.scan_status.setText("No tracking")
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
        if self.timer.isActive():
            self.show_info("Disconnecting from selected device\nthis may take some few seconds...")
            self.show_alert.content("Hey! wait a second while system\nrelease camera") 
            self.show_alert.show()
            self.ui.camera_view.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui.camera_view.setScaledContents(False)
            self.timer.stop()
            self.show_info("Disconnected from device\nsuccessfully...") 
        else:
            self.show_alert.content("Oops! you have no active camera\nto disconnect from.") 
            self.show_alert.show()  

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
    
    def help_url(self):
        try:
            url = "https://github.com/redolf250/releases"
            webbrowser.open(url)
        except Exception as e:
            print(str(e))

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

class Authentication(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)
        self.show_alert = AlertDialog()
        self.restapi = RESTAPI()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_login.btn_close.clicked.connect(self.close)
        self.ui_login.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_login.btn_close.clicked.connect(self.close)
        self.ui_login.avater.setDisabled(True)
        self.ui_login.btn_login.clicked.connect(self.login)
        self.retrieve = ForgotPassword()
        self.icon =QIcon(window.resource_path('icon.ico'))
        self.retrieve.setWindowIcon(icon)
        self.retrieve.setWindowTitle('Reset')
        self.ui_login.btn_forgot_pass.clicked.connect(lambda: self.retrieve.show())
        self.ui_login.btn_login.pressed.connect(self.change_text)
        self.user()                 

    def application_logs(self,message):
        time =current.now().time().strftime('%I:%M:%S %p')
        date=current.now().date().strftime('%a %b %d %Y')
        filename=current.now().date().strftime('%a_%b_%d_%Y')
        path =Path(f'C:\\ProgramData\\iAttend\\data\\application_logs\\{filename}.txt')
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n[{date}] [{time}]: {message}')
            file.close()

    def change_text(self):
        self.ui_login.btn_login.setText('Loading...')
        self.ui_login.btn_login.setIcon(QIcon(u":/icons/asset/loader.svg"))

    def user(self):
        if self.restapi.check_state():
            self.ui_login.username.setText("root@developer")
            self.ui_login.student_id.setText("123456")
            self.ui_login.password.setText("root@developer")
        else:
            self.ui_login.username.setText("redolf250")
            self.ui_login.student_id.setText("20661163")
            self.ui_login.password.setText("redolfkendrick@gmail.com")

    def login(self):
        username = self.ui_login.username.text()
        reference = self.ui_login.student_id.text()
        password = self.ui_login.password.text()

        global login_username
        global login_reference
        global account_firstname
        global account_lastname
        global account_contact
        global account_mail
        global account_role 
        global account_status

        if username and reference and password:
            details = self.query_database_login("SELECT * FROM tb_user_details where user_reference="+str(reference))
            credentials = self.query_database_login("SELECT * FROM tb_user_credentials where user_reference="+str(reference))
            password = bytes(password,encoding='utf-8')
            if len(credentials) > 0:
                confirm = bcrypt.checkpw(password,credentials[0][5])
                if reference==str(credentials[0][1]) and username==str(credentials[0][2]) and confirm:
                    if str(credentials[0][4])=="ACTIVATED":
                        login_username = str(credentials[0][2])
                        login_reference = str(credentials[0][1])
                        account_status = str(credentials[0][4])
                        account_firstname = str(details[0][2])
                        account_lastname = str(details[0][3])
                        account_contact = str(details[0][4])
                        account_role = str(credentials[0][3]) 
                        account_mail = str(details[0][5])
                        self.main = MainWindow()
                        self.icon =QIcon(self.resource_path('icon.ico'))
                        self.main.setWindowIcon(self.icon)
                        self.main.setWindowTitle('iAttend')
                        self.close()
                        self.main.show()
                        self.application_logs("Authenticated user with credentials successfully")   
                    else:
                        self.application_logs("Authenticating user failed with credentials -> DEATIVATED")
                        self.ui_login.btn_login.setIcon(QIcon(u":/icons/asset/download.svg"))
                        self.ui_login.btn_login.setText('Login')
                        self.show_alert.content(f"Oops! user account DEACTIVATED\ncontact administrator.") 
                        self.show_alert.show() 
                else:
                    self.application_logs("Authenticating user failed with bad credentials")
                    self.ui_login.btn_login.setText('Login')
                    self.ui_login.btn_login.setIcon(QIcon(u":/icons/asset/download.svg"))
                    self.show_alert.content("Oops! Bad user credentials.") 
                    self.show_alert.show()
            else:
                self.ui_login.btn_login.setText('Login')
                self.ui_login.btn_login.setIcon(QIcon(u":/icons/asset/download.svg"))
                self.application_logs("Authenticating user failed with credentials -> no details found")
                self.show_alert.content("Oops! no details found.") 
                self.show_alert.show()
        else:
            self.ui_login.btn_login.setText('Login')
            self.ui_login.btn_login.setIcon(QIcon(u":/icons/asset/download.svg"))
            self.show_alert.content("Oops! invalid login details.") 
            self.show_alert.show()

    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path

    def get_cache_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\cache\\database\\attendance_database_cache.db'

    def query_database_login(self, query: str):
        try:
            db = sqlite3.connect(self.get_cache_path())
            cursor = db.cursor()
            details = []
            cursor = cursor.execute(query)
            cursor = cursor.fetchall()
            db.commit()
            db.close()
            if cursor:
                for item in cursor:
                    details.append(item)
            return details
        except Exception as e:
            self.show_alert.content(str(e)) 
            self.show_alert.show()  

class Splash_screen(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_MainWindow()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.main.setGraphicsEffect(self.shadow)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.create_program_directory()
        self.populate_root_user_data()
        self.create_cache_database()
        self.show()       
        
    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.application_logs("Application bootstrapping process completed")
            self.main = Authentication()
            self.icon =QIcon(self.resource_path('icon.ico'))
            self.main.setWindowIcon(self.icon)
            self.main.setWindowTitle('Login')
            self.application_logs("Application boostrapped to authentication page")
            self.main.show()
            self.close()
        counter +=1

    def application_logs(self,message):
        time =current.now().time().strftime('%I:%M:%S %p')
        date=current.now().date().strftime('%a %b %d %Y')
        filename=current.now().date().strftime('%a_%b_%d_%Y')
        path =Path(f'C:\\ProgramData\\iAttend\\data\\application_logs\\{filename}.txt')
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n[{date}] [{time}]: {message}')
            file.close()

    def create_sub_folders(self,directory: str,folder: tuple):   
        for item in folder:
            path = os.path.join(directory,item)
            if not os.path.exists(path):
                os.mkdir(path)

    def create_program_directory(self):
        root_dir = 'C:\\ProgramData\\iAttend\\data'
        list =('batch_logs','properties','qr_code',
        'email_details','reports','exports','cache',
        'partition','application_logs','httpErrors')

        pictures = 'C:\\Pictures\\iAttend\\'
        if not os.path.exists(pictures):
            os.makedirs(pictures)

        if not os.path.exists(root_dir):
            os.makedirs(root_dir)
        for item in list:
            path = os.path.join(root_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)
        self.create_files()

        cache_dir = 'C:\\ProgramData\\iAttend\\data\\cache'
        cache_sub_dirs = ('database','logs','images')    
        self.create_sub_folders(cache_dir,cache_sub_dirs)

        report_dir = 'C:\\ProgramData\\iAttend\\data\\reports'
        report_sub_dirs = ('piechart','barchart','linegraph','visualize') 
        self.create_sub_folders(report_dir,cache_sub_dirs)
   

        cache_images_dir = 'C:\\ProgramData\\iAttend\\data\\cache\\images'
        images_sub_dirs = ('students','administrators')    
        self.create_sub_folders(cache_images_dir,images_sub_dirs)
        
        export_dir = 'C:\\ProgramData\\iAttend\\data\\exports'
        export_sub_dir = ('csv','json')
        self.create_sub_folders(export_dir,export_sub_dir)

    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path

    def write_to_file(self,path: str,data: str,type: str):
        path =Path(path)
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                if type == 'json':
                    if os.path.getsize(path)==0:
                        json.dump(data,file,indent=2)
                else:
                    if os.path.getsize(path)==0:
                        file.write(data)
            file.close()

    def create_files(self):
        root = 'C:\\ProgramData\\iAttend\\data\\'
        mail_properties = {
                "sender": "Sender",
                "subject": "Subject",
                "mail": "example@example.com",
                "password": "Password"
                }
        
        path =os.path.join(root,'properties\\central_database_connection_propeties.json')
        json_data = {
            "username":"username@CoS",
            "password":"passsword@CoS",
            "hostname":"hostname@CoS",
            "port":"port@CoS",
            "database":"database@CoS"
        }
        self.write_to_file(path,json_data,'json')
        
        path =os.path.join(root,'properties\\central_database_connection_propeties.json')
        json_data = {
            "username":"username@connection",
            "password":"passsword@connection",
            "hostname":"hostname@connection",
            "port":"port@connection",
            "database":"database@connection",
            "servername":"servername@connection"
        }
        self.write_to_file(path,json_data,'json')
        
        path =os.path.join(root,'properties\\students_restapi_endpoints.json')
        json_data = {
            "details":"http://localhost/api/v1/students/details/reference",
            "endpoint":"RESTAPI"
        }
        self.write_to_file(path,json_data,'json')
       
        with open(self.resource_path('database_properties.json'),'r') as data:
            json_data = json.load(data)
        path =os.path.join(root,'properties\\database_properties.json')
        self.write_to_file(path,data,'json')
        
        with open(self.resource_path('restapi_endpoints.json'),'r') as data:
            json_data = json.load(data)
        path =os.path.join(root,'properties\\restapi_endpoints.json')
        self.write_to_file(path,json_data,'json')

        with open(self.resource_path('database_properties.json'),'r') as data:
            json_data = json.load(data)
        path =os.path.join(root,'properties\\database_properties.json')
        self.write_to_file(path,json_data,'json')
        
        path =os.path.join(root,'email_details\\details.json')
        self.write_to_file(path,mail_properties,'json')

        path =os.path.join(root,'email_details\\consolidation.json')
        self.write_to_file(path,mail_properties,'json')
        
        path =os.path.join(root,'partition\\partition.txt')
        partition = 'Faculty,Gender,College,Category,Disability,Nationality,Department'
        self.write_to_file(path,partition,'text/plain') 

        path =os.path.join(root,'partition\\database_fields.txt')
        partition = 'student_faculty,student_gender,student_college,student_category,student_disability,student_nationality,student_program'
        self.write_to_file(path,partition,'text/plain')
        
        path =os.path.join(root,'email_details\\content.txt')
        content = """
        Hello name,
                Please attached to this message is your
            attendance code. Please keep it safe as you 
            will need this everytime you would want to 
            access the facility. 
                Attend Today, Acheive Tomorrow!
                                            Thank you! """
        self.write_to_file(path,content,'text/plain')
        
        path =os.path.join(root,'email_details\\content_report.txt')
        report_content = """
        Hello name,
    	        Please attached to this message is the
            report or data you requested for. Feel free 
            to contact us for our services at anytime.
                                        Thank you! """
        self.write_to_file(path,report_content,'text/plain')
        
        path =os.path.join(root,'email_details\\credential_mail.txt')
        credentials_content = """
            Dear Name,
            
    	        The password for this account_name was reset on date_stamp
                at exactly time_stamp. 

    	        If you did not request a password reset or believe that this 
                request was made in error, please contact us immediately by 
                replying to this email.

                If you have any questions or concerns, please do not hesitate
                to contact our administrative team.

            Best regards,

            College_name,
            """
        self.write_to_file(path,credentials_content,'text/plain')
        
        path =os.path.join(root,'email_details\\new_account_mail.txt')
        new_account_content = """
        Dear Name,

            We are excited to welcome you to library team. Your 
            account has been successfully created, and we are
            thrilled to have you as part of our community.

            To access your account, login with your credentials.

            Your credentials to give you access are as below:
            username: account_username, password: account_password
            and reference: account_reference. You can always update
            your credentials.

            If you have any questions or concerns, please do not 
            hesitate to contact our customer support team. 
            We are available 24/7 to assist you with any issues 
            you may encounter.

        Best regards,

        College_name,
        """
        self.write_to_file(path,new_account_content,'text/plain')
        
        path =os.path.join(root,'email_details\\consolidation_content.txt')
        merge_content = """
        Dear Administrator,

            I hope this message finds you well. I wanted 
            to inform you that as of stamp, the data you 
            requested has been successfully pushed to the
            server.

            Facility name: facility
            Total records: value
            Date: date

            Our team has taken great care to ensure that the
            data is accurate and up-to-date, and we have also
            implemented appropriate security measures to protect
            the data.

            Please let us know if you need any further assistance
            or if you have any questions or concerns. We are always
            happy to help in any way we can.

            Thank you for your attention to this matter.

        Best regards,
        Username
        """
        self.write_to_file(path,merge_content,'text/plain')

    def create_cache_database(self):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        cursor.execute(create_tb_students_sqlite())
        cursor.execute(create_tb_attendance_sqlite())
        cursor.execute(create_tb_cameras_sqlite())
        cursor.execute(create_tb_user_sessions_sqlite())
        cursor.execute(create_tb_attendance_temp_sqlite())
        cursor.execute(create_tb_attendance_last_seen_sqlite())
        cursor.execute(create_tb_student_study_details_sqlite())
        cursor.execute(create_tb_user_details_cache())
        cursor.execute(create_tb_user_credentials_cache())
        db.commit()

    def get_cache_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\cache\\database\\attendance_database_cache.db'

    def populate_root_user_data(self):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        details=self.query_user_data("SELECT * FROM tb_user_details WHERE user_reference="+root_reference)
        self.query_user_data("SELECT * FROM tb_user_credentials WHERE user_reference="+root_reference)
        if not details:
            password_hash = hash_password(root_password)
            cursor.execute("INSERT INTO tb_user_details (user_reference,user_firstname,user_lastname,user_contact,user_mail) VALUES (?,?,?,?,?)",
            (root_reference,root_firstname,root_lastname,root_contact,root_mail)) 
            cursor.execute("INSERT INTO tb_user_credentials (user_reference,user_username,user_role,user_status,user_password) VALUES (?,?,?,?,?)",
            (root_reference,root_username,root_role,root_status,password_hash))    
            db.commit()
        pass 
     
    def query_user_data(self,query):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        details=cursor.execute(query)
        details= cursor.fetchone()
        db.commit()
        cursor.close()
        db_data = []
        if details:
            for data in details:
                db_data.append(data)
        return db_data

    def application_logs(self,message):
        time =current.now().time().strftime('%I:%M:%S %p')
        date=current.now().date().strftime('%a %b %d %Y')
        filename=current.now().date().strftime('%a_%b_%d_%Y')
        path =Path(f'C:\\ProgramData\\iAttend\\data\\application_logs\\{filename}.txt')
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n[{date}] [{time}]: {message}')
            file.close()

if __name__ == '__main__':
    try:
        application = QApplication(sys.argv)
        window = Splash_screen()
        icon =QIcon(window.resource_path('icon.ico'))
        window.setWindowIcon(icon)
        window.setWindowTitle('Preloader')
        window.application_logs("Application bootstrapping process in progress")  
        sys.exit(application.exec_())
    except Exception as e:
        window.application_logs(str(e))