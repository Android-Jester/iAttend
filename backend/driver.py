################################################################################
##
## BY: Asamani Redolf
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
        self.ui.btn_batch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.batch))
        self.ui.btn_sink_data.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_help_link.clicked.connect(self.help_url)

        self.ui.btn_database.hide()
        self.ui.btn_batch.hide()
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

        self.open_exit_camera = ExitCameraFeed()
        self.ui.btn_open_exit_camera_ui.clicked.connect(lambda: self.open_exit_camera.show())
    
        self.database = Database()
        self.ui.btn_open_database.clicked.connect(lambda: self.database.show())

        self.restapi = RESTAPI()
        self.ui.btn_open_database.clicked.connect(lambda: self.restapi.show())

        self.settings = Settings()
        self.ui.btn_settings.clicked.connect(lambda: self.settings.show())

        self.merge = CentralDatabase()
        self.ui.btn_merge_connection.clicked.connect(lambda: self.merge.show())

        self.mail = Mail()
        self.ui.btn_mail_report_or_data.clicked.connect(lambda: self.mail.show())

        self.directory = Images()
        self.ui.btn_batch_folder.clicked.connect(lambda: self.directory.show())

        self.data_view = DataView()
        self.ui.btn_generated_data.clicked.connect(lambda: self.data_view.show())
        
        self.user = User()
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
        self.load_user_profile(login_reference)
        self.set_session()
        self.user.profileImage('C:\\ProgramData\\iAttend\\data\\images\\user_image.jpg')
        self.insert_thread()
        
        self.camera_4 = Camera_Four()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_4.show())
        self.camera_3 = Camera_Three()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_3.show())
        self.camera_2 = Camera_Two()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_2.show())
        self.camera_1 = Camera_One()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_1.show())
        self.ui.btn_camera.clicked.connect(self.camera_config)

        self.login = Authentication()
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
        self.ui.report_date.dateTimeChanged.connect(self.get_report_date)
        self.ui.btn_reload.clicked.connect(self.clear_fields_on_search_page)
        self.ui.btn_csv.clicked.connect(self.export_data_to_csv)
        self.ui.btn_json.clicked.connect(self.export_data_to_json)
        ##############################################################################################

        ##############################################################################################
        self.ui.btn_search_reg.clicked.connect(self.search_student)
        self.ui.calendarWidget_reg.selectionChanged.connect(self.get_registration_start_date)
        self.ui.btn_register.clicked.connect(self.register_student)
        self.ui.btn_clear.clicked.connect(self.resets_fileds)
        self.ui.btn_update.clicked.connect(self.update_student)
        self.ui.btn_remove.clicked.connect(self.remove_student)
        self.ui.btn_browse_reg.clicked.connect(self.browse_image_files)
        self.ui.btn_send_mail.clicked.connect(self.send_mail)
        self.ui.reg_type.addItems(self.read_category(self.resource_path('categories.txt')))
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
        country_completer = QCompleter(self.country_names(self.resource_path('data_json.json')))
        country_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.reg_nationality.setCompleter(country_completer)
        
        self.ui.reg_college.addItems(load_colleges(self.resource_path('structure.json')))
       
        self.ui.btn_remove_combox_item.clicked.connect(self.remove_item_from_comboBox)
        self.ui.btn_scan_range.clicked.connect(self.camera_thread)
        self.ui.btn_batch_browse.clicked.connect(self.browse_batch_data)
        self.ui.btn_start_job.clicked.connect(self.insert_records_thread)
        self.ui.btn_batch_images.clicked.connect(self.insert_images_thread)
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
        self.ui.btn_add_category.clicked.connect(self.add_category)
        self.ui.btn_refresh_category.clicked.connect(self.refresh_category)

        load_data(self.resource_path('structure.json'))
        load_colleges(self.resource_path('structure.json'))
        self.ui.reg_college.activated.connect(self.load_college_faculties)
        self.ui.reg_faculty.activated.connect(self.load_colleges)
        self.load_college_faculties()
        self.load_colleges()
        self.set_curent_dates()
        self.set_database_colleges()
        self.set_endpoints_colleges()
        self.get_central_database_properties()
        self.ui.db_consolidation_date.dateTimeChanged.connect(self.set_date_for_consolidation)
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
        
        # ,QDateTime,QDate,QTime
        ##################################################################################################

    def show_pages_based_role(self):
        if account_role == analyst:
            self.ui.stackedWidget.setCurrentWidget(self.ui.merge_report)
            self.ui.btn_camera.hide()
            self.ui.btn_admin.hide()
            self.ui.btn_home.hide()
            self.ui.btn_search.hide()
            self.ui.btn_database.hide()
            self.ui.btn_report.hide()
            self.ui.btn_batch.hide()
            self.ui.btn_sink_data.hide()
            self.ui.btn_consolidation_report.hide()
        elif account_role == user:
            self.ui.frame.setMinimumHeight(580)
            self.ui.frame.setMaximumHeight(580)
            self.ui.btn_admin.hide()
            self.ui.btn_consolidation_report.hide()
        
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

    def change_merge_load_text(self):
        table_name=self.merge.get_table_name()
        if table_name:
            self.ui.btn_merge_load.setText('Loading...')
        pass
    
    def merge_report_generate(self):
        if self.ui.merge_pie_chart.isChecked():
            self.merge_piechart_generate()
            self.ui.btn_merge_load.setText('Load')
        elif self.ui.merge_bar_chart.isChecked():
            self.merge_barchart_generate()
            self.ui.btn_merge_load.setText('Load')
        elif self.ui.merge_line_graph.isChecked():
            print("Line graph generation......")
            self.ui.btn_merge_load.setText('Load')

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
    

    def merge_linegraph_generate(self):
        pass
    
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
        elif self.ui.merge_line_graph.isChecked():
            if filename:
                self.line_graph.save_chart(transformed_name)
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
                    cursor.executemany(f"INSERT INTO {tablename}(student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability,facility_used) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                    results[record:record+batch_size])
                    db.commit()
                current_account = f"{account_firstname} {account_lastname}"
                receiver = self.ui.db_consolidation_mail.text() 
                records_date=self.load_merge_dates()
                content = self.consolidation_mail_content(facility,str(len(results)),records_date,current_account)
                if self.connected_to_internet()==True and receiver:
                    self.mail=UserMailThread(details=self.consolidation_mail_details(),mail_content=content,receiver=receiver)
                    self.mail.start()
                self.application_logs(f'Push records to central database -> successfully')
                self.alert.content("Pushed "+str(len(results))+" records to server\nMail sent to administrator..")
                self.alert.show()
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
        state = self.ui.db_consolidation_range.isChecked()
        stop=self.date_formater(self.ui.db_consolidation_stop.text())
        if self.ui.db_fetch_all.isChecked(): 
            return 'All records fetched from database'
        elif start and not state:
            return self.reconstruct_date(start)
        elif start and stop and state:
            return f'{self.reconstruct_date(start)}-{self.reconstruct_date(stop)}'

    def load_merge_data(self):
        self.alert = AlertDialog()
        start=self.date_formater(self.ui.db_consolidation_start.text())
        state = self.ui.db_consolidation_range.isChecked()
        stop=self.date_formater(self.ui.db_consolidation_stop.text())
        if self.ui.db_fetch_all.isChecked():
            results=self.query_cache_data_list("SELECT student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability FROM tb_attendance")
            self.consolidation_table(results)
            self.ui.db_consolidation_notification.setText("Total records fetched: "+str(len(results)))
            return results
        elif start and not state:
            results=self.query_cache_data_list("SELECT student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability FROM tb_attendance WHERE date_stamp="+start)
            self.consolidation_table(results)
            self.ui.db_consolidation_notification.setText("Total records fetched: "+str(len(results)))
            return results
        elif start and stop and state:
            results=self.query_cache_data_list("SELECT student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability FROM tb_attendance WHERE date_stamp BETWEEN "+start+" AND "+stop)
            self.consolidation_table(results)
            self.ui.db_consolidation_notification.setText("Total records fetched: "+str(len(results)))
            return results
        
    def set_date_for_consolidation(self):
        date = self.ui.db_consolidation_date.date().toPython()
        if self.ui.db_consolidation_range.isChecked():
            self.ui.db_consolidation_stop.setText(str(date))
        else:
            self.ui.db_consolidation_start.setText(str(date))
    

    def set_database_colleges(self):
        results=load_colleges(self.resource_path('database_properties.json'))
        self.database.set_colleges(results)

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

    def read_category(self,path):
        with open(path,'r') as file:
            category_list = []
            category = file.readlines()
            for item in category:
                item=item.replace('\n','')
                category_list.append(item)
            file.close()
            return category_list
        
    def set_curent_dates(self):
        self.now = current.now().date()
        curent_date=QDate(self.now.year,self.now.month,self.now.day)
        self.ui.search_page_date.setDate(curent_date)
        self.ui.search_page_date_2.setDate(curent_date)
        self.ui.user_start_date_widget.setDate(curent_date)
        self.ui.user_end_date_widget.setDate(curent_date)
        self.ui.db_consolidation_date.setDate(curent_date)
        self.ui.report_date.setDate(curent_date)
        self.ui.db_end_date.clear()
        self.ui.user_end_date_field.clear()
        self.ui.user_start_date_field.clear()
        self.ui.db_start_date.clear()
        self.ui.report_start_date.clear()
        self.ui.db_consolidation_date.clear()

    def value_formater(self,value):
        return "\'{}\'".format(value)

    def load_colleges(self):
        program = get_dept(self.resource_path('structure.json'),self.ui.reg_college.currentText(),self.ui.reg_faculty.currentText())
        self.ui.reg_programs.clear()
        self.ui.reg_programs.addItems(program)
        self.ui.reg_college.activated.connect(self.load_college_faculties)

    def load_college_faculties(self):
        faculties=load_faculties(self.resource_path('structure.json'),self.ui.reg_college.currentText())
        self.ui.reg_faculty.clear()
        self.ui.reg_faculty.addItems(faculties)
        program = get_dept(self.resource_path('structure.json'),self.ui.reg_college.currentText(),self.ui.reg_faculty.currentText())
        self.ui.reg_programs.clear()
        self.ui.reg_programs.addItems(program)
        
    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path
    
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

    def application_exit(self):
        self.close()
        self.set_log_out_session()
        update_information_file()
        self.database.close()
        self.camera_1.close()
        self.camera_2.close()
        self.camera_3.close()
        self.camera_4.close()
        self.directory.close()
        self.data_view.close()
        self.merge.close()
        self.mail.close()
        self.user.close()
        self.config.close()
        self.open_exit_camera.close()
        self.login.show()
        
    def camera_config(self):
        if account_role == admin:
            self.config.show()
     
    def user_last_seen(self,reference:str):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        check_state=self.database.check_state()
        if check_state == True:
            cursor=my_cursor.execute("SELECT user_date,user_logout,user_duration FROM tb_user_session_last_seen WHERE user_reference = "+(reference))
            cursor= my_cursor.fetchall()
            db.commit()       
        else:
            db = sqlite3.connect(self.get_cache_path())
            _cursor = db.cursor()
            cursor=_cursor.execute("SELECT user_date,user_logout,user_duration FROM tb_user_session_last_seen WHERE user_reference = "+(reference))
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
        (db,my_cursor,connection_status) = self.database.my_cursor()
        check_state=self.database.check_state()
        session=self.set_user_session()
        self.alert = AlertDialog()
        try:
            if check_state == True:
                my_cursor.execute("INSERT INTO tb_user_session (user_reference,user_username,user_date,user_login,user_logout,user_duration) VALUES (?,?,?,?,?,?)",
                (session.reference,session.username,session.date,session.login,session.logout,session.duration))
                db.commit()         
            else:
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
 
    def load_user_profile(self,reference):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        cursor=my_cursor.execute("SELECT user_reference,user_image from tb_user_profile WHERE user_reference="+reference)
        cursor= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        image_data = []
        path = 'C:\\ProgramData\\iAttend\\data\\images\\user_image.jpg'
        if cursor:
            for data in cursor:
                image_data.append(data)
            if len(image_data)>0:
                with open(path,'wb') as image_file:
                    image_file.write(image_data[1])
            pass
        pass

    def visits_count(self):
        results=self.query_cache_data_list("select count(user_reference) from tb_user_session where user_reference="+login_reference+" and user_duration NOT LIKE '%00:00:00%'")
        return results[0][0]

    def set_session(self):
        self.ui.label_6.setText("session@"+login_username+" "+current.now().time().strftime("%I:%M:%S %p"))

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

    def read_user_endpoints(self):
        with open('C:\\ProgramData\\iAttend\\data\\user\\api_routes.json','r') as content:
            data = content.read()
            try:
                return json.loads(data)
            except Exception as e:
                pass
    
    def set_load_user_text(self):
        self.ui.btn_user_fetch.setText("Loading...")
        self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/loader.svg"))

    def render_user_interface(self, details:json):
        self.ui.user_firstname.setText(details['firstname'])
        self.ui.user_middlename.setText(details['othername'])
        self.ui.user_lastname.setText(details['lastname'])
        self.ui.user_reference.setText(details['reference'])
        
    def load_user_from_api(self):
        self.alert = AlertDialog()
        user=self.read_user_endpoints()
        reference=self.ui.user_search.text()
        url = str(user['details']).replace('reference',reference)
        if self.validate_field('^[0-9]+$',reference):
            try:
                request_body = requests.get(url)
                student_data=request_body.json()
                if request_body.status_code == 200:
                    self.render_user_interface(student_data)
                    self.ui.btn_user_fetch.setText("Load")
                    self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/download.svg"))
                else:
                    self.ui.btn_user_fetch.setText("Load")
                    self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/download.svg"))
                    self.alert.content(str(student_data))
                    self.alert.show()
            except Exception as e:
                self.ui.btn_user_fetch.setText("Load")
                self.ui.btn_user_fetch.setIcon(QIcon(u":/icons/asset/download.svg"))
                self.alert.content(str(e))
                self.alert.show()
        else:
            self.alert.content("Oops! invalid reference number...")
            self.alert.show()
       
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
                    self.load_user_image(reference,self.ui.user_image)
                return details
            else:
                self.alert.content("Oops! invalid reference provided.")
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
 
    def load_user_image(self,reference,label):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        cursor=my_cursor.execute("SELECT user_reference,user_image from tb_user_profile WHERE user_reference="+reference)
        cursor= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        image_data = []
        path = 'C:\\ProgramData\\iAttend\\data\\images\\user_image.jpg'
        if cursor:
            for data in cursor:
                image_data.append(data)
            if len(image_data)>0:
                with open(path,'wb') as image_file:
                        image_file.write(image_data[1])
            label.setPixmap(QPixmap.fromImage(path))
            label.setScaledContents(True)

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

    def query_user_data(self,query):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        detail =my_cursor.execute(query)
        detail= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
        return db_data

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
    
    
    def logout(self):
        self.alert = AlertDialog()
        try:
            self.set_log_out_session()
            self.close()
            update_information_file()
            self.config.close()
            self.database.close()
            self.camera_1.close()
            self.camera_2.close()
            self.camera_3.close()
            self.camera_4.close()
            self.directory.close()
            self.data_view.close()
            self.merge.close()
            self.mail.close()
            self.user.close()
            self.open_exit_camera.close()
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
            check_state = self.database.check_state()
            (db,my_cursor,connection_status) = self.database.my_cursor()
            if check_state == True:
                my_cursor.execute("SELECT user_login,user_duration FROM tb_user_session WHERE user_reference="+reference+" AND user_date="+date+" AND user_duration="+duration)
                cursor=my_cursor.fetchall()
                db.commit()
            else:
                db = sqlite3.connect(self.get_cache_path())
                my_cursor = db.cursor() 
                my_cursor.execute("SELECT user_login,user_duration FROM tb_user_session WHERE user_reference="+reference+" AND user_date="+date+" AND user_duration="+duration) 
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
                my_cursor.execute("UPDATE tb_user_session SET user_logout="+new_time_out+", user_duration="+new_duration+" WHERE user_reference="+reference+" AND user_date="+date+" AND user_duration="+duration)
                db.commit()
                my_cursor.execute("DELETE FROM tb_user_session_last_seen WHERE user_reference="+reference)
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
                    index=row[3],
                    reference=row[4],
                    email_address=[10]
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

    def insert_images_thread(self):
        self.alert = AlertDialog()
        check_state = self.database.check_state()
        path = self.directory.directory_path()
        if path:
            if not check_state:
                self.pool = QThreadPool()
                self.work = ImageThread(self.insert_images)
                self.pool.start(self.work)
            else:
                self.alert.content("Oops! no database configured...")
                self.alert.show()
        else:
            self.alert.content("Oops! invalid file path...")
            self.alert.show()

    def validate_field(self,pattern,value):
        return bool(re.match(pattern,value))

    def insert_images(self):
        date=current.now().strftime('%d_%B_%Y_%I_%M_%S_%p')
        name = str('images_logs_unprocessed')
        log_path = str('C:\\ProgramData\\iAttend\\data\\batch_logs\\'+name+'_'+date+'.txt')
        path = self.directory.directory_path()
        images_extension = ['jpg', 'jpeg', 'png'] 
        self.ui.batch_notification.setText("Saving images in progress...") 
        for item in os.listdir(path):
            image = os.path.join(path,item)
            image = os.path.abspath(image)
            image_name = os.path.basename(image)
            extension = image_name.split('.')[1]
            student_reference = image_name.split('.')[0]
            validate=self.validate_field('^[0-9]+$',student_reference)
            if not validate:
                with open(log_path,'a+') as file:
                    file.writelines('\n'+str(student_reference))
                    file.close
            if extension in images_extension and validate:
                db = sqlite3.connect(self.get_cache_path())
                my_cursor = db.cursor()
                with open(image,'rb') as image_data:
                    data = image_data.read()
                    my_cursor.execute("INSERT INTO tb_student_images(student_reference,student_image) VALUES(?,?)",(student_reference,data))
                    db.commit()
                    my_cursor.close()
        self.ui.batch_notification.setText("Valid images saved successfully\nanalyse logs for details...") 
              
    def insert_records_thread(self): 
        path = self.ui.batch_browse.text()
        self.alert = AlertDialog()
        check_state = self.database.check_state()
        partition = self.validate_field("^[0-9]+$",self.ui.batch_partition.text())
        if path:
            if not check_state:
                self.pool = QThreadPool()
                self.work = ImageThread(self.batch_insert_student_data)
                self.pool.start(self.work)
            else:
                self.alert.content("Oops! no database configured...")
                self.alert.show()
        else:
            self.alert.content("Oops! invalid file path or\n Split not set...")
            self.alert.show()

    def batch_insert_student_data(self):
        self.alert = AlertDialog()
        check_state=self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        student_list = self.load_batch_data()
        file_path = self.ui.batch_browse.text()
        date=current.now().strftime('%d_%B_%Y_%I_%M_%S_%p')
        name = str('batch_logs_unprocessed')
        path = str('C:\\ProgramData\\iAttend\\data\\batch_logs\\'+name+'_'+date+'.txt')
        table=self.ui.tableWidget_batch.item(0,0)
        if file_path and table:
            self.ui.batch_notification.setText("Saving records in progress...")  
            if check_state == True:
                pass
            else:
                start = time.time()
                partition = self.validate_field("^[0-9]+$",self.ui.batch_partition.text())
                batch_size= len(student_list)//partition
                for student in student_list:
                    name_ = str(student[0]).split(' ')
                    firstname  = name_[0]+' '+name_[1]
                    lastname = str(name_[2]).strip()
                    date = str(student[6]).split('-')
                    details=self.fetch_data_from_db(str(student[1])) 
                    if not details:
                        my_cursor.execute("INSERT INTO tb_students(student_reference,student_index,student_firstname,student_lastname,student_nationality,student_gender,student_disability,card_issued_date,card_expiry_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (student[1],student[2],firstname,lastname,student[3],student[4],student[5],str(date[0]).strip(),str(date[1]).strip())) 
                        db.commit()
                        my_cursor.execute("INSERT INTO tb_student_study_details(student_reference,student_college,student_faculty,student_program,student_category) VALUES (%s,%s,%s,%s,%s)",
                        (student[1],student[7],student[8],student[9],student[10]))   
                        db.commit()
                        print(f"Student record @{student[1]} pushed to server")
                    else:
                        with open(path,'a+') as file:
                            file.writelines('\n'+str(student))
                        file.close
                end = time.time()
                self.ui.batch_notification.setText("Valid records saved successfully...")
                print(f"Execution time {end-start} seconds")
        else:   
            self.alert.content("Oops! invalid file path or content is empty...")
            self.alert.show()
       
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
                    name_transformed = student[0]+' '+student[1]+' '+student[2]
                    student.pop(2)
                    student[0] = name_transformed
                    issued_date = str(student[7]).split('/')
                    expiry_date = str(student[8]).split('/')
                    issued_date_transformed = datetime.date(int(issued_date[2]),int(issued_date[0]),int(issued_date[1])).strftime("%b %Y")
                    expiry_date_transformed = datetime.date(int(expiry_date[2]),int(expiry_date[0]),int(expiry_date[1])).strftime("%b %Y")
                    student[8] = issued_date_transformed+' - '+expiry_date_transformed
                    student.pop(1)
                    student.pop(6)
                    results_list.append(student)
                return results_list

    def batch_table(self, details:list):
        self.ui.tableWidget_batch.setAutoScroll(True)
        self.ui.tableWidget_batch.setAutoScrollMargin(2)
        self.ui.tableWidget_batch.setTabKeyNavigation(True)
        self.ui.tableWidget_batch.setColumnWidth(0,250)
        self.ui.tableWidget_batch.setColumnWidth(1,140)
        self.ui.tableWidget_batch.setColumnWidth(2,140)
        self.ui.tableWidget_batch.setColumnWidth(3,220)
        self.ui.tableWidget_batch.setColumnWidth(4,100)
        self.ui.tableWidget_batch.setColumnWidth(5,110)
        self.ui.tableWidget_batch.setColumnWidth(6,190)
        self.ui.tableWidget_batch.setColumnWidth(7,100)
        self.ui.tableWidget_batch.setColumnWidth(8,100)
        self.ui.tableWidget_batch.setColumnWidth(9,300)
        self.ui.tableWidget_batch.setColumnWidth(10,140)
        self.ui.tableWidget_batch.setColumnWidth(11,250)
        self.ui.tableWidget_batch.setRowCount(len(details))
        self.ui.tableWidget_batch.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget_batch.setItem(row_count,0,QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_batch.setItem(row_count,1,QTableWidgetItem(str(data[1])))
            self.ui.tableWidget_batch.setItem(row_count,2,QTableWidgetItem(str(data[2])))
            self.ui.tableWidget_batch.setItem(row_count,3,QTableWidgetItem(str(data[3])))
            self.ui.tableWidget_batch.setItem(row_count,4,QTableWidgetItem(str(data[4])))
            self.ui.tableWidget_batch.setItem(row_count,5,QTableWidgetItem(str(data[5])))
            self.ui.tableWidget_batch.setItem(row_count,6,QTableWidgetItem(str(data[6])))
            self.ui.tableWidget_batch.setItem(row_count,7,QTableWidgetItem(str(data[7])))
            self.ui.tableWidget_batch.setItem(row_count,8,QTableWidgetItem(str(data[8])))
            self.ui.tableWidget_batch.setItem(row_count,9,QTableWidgetItem(str(data[9])))
            self.ui.tableWidget_batch.setItem(row_count,10,QTableWidgetItem(str(data[10])))
            self.ui.tableWidget_batch.setItem(row_count,11,QTableWidgetItem(str(data[11])))
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


    def clear_camera_comboBoxes(self):
        self.ui.comboBox.clear()
        self.open_exit_camera.set_combo_items('')
        
    def get_active_cameras(self,camera:list):
        self.ui.comboBox.addItems(camera)
        self.open_exit_camera.set_combo_items(camera)
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
            self.alert_builder("Oops! no scan range provided\nor invalid input...")
    

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
        if not self.database.check_state():
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
        else:
            self.alert.content("Oops! no database configured...")
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
        elif self.ui.report_start_date.text() and self.ui.report_end_date.text():
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
        if query_value == "Faculty":
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_faculties,'Faculty'))
            if len(data)>=1:
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"Total records: {self.calculate_records_total(data[1])}",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        elif query_value == "Department":
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_departments,'Department'))
            if len(data)>=1:
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"values",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        elif query_value == "College":
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_college,'College'))
            if len(data)>=1:
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"values",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()
        else:
            data=self.get_actual_plot_values(self.line_plot_values(query_param,report_departments,''))
            if len(data)>=1:
                self.line_graph.plot_graph(data,title=f"{properties[0]}",label_="Trends",y_label=y_label,
                x_label=f"values",area=properties[1],dpi=properties[3],color=colors[0],marker=marker[0])
                self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                self.ui.plot_area.setScaledContents(True)
            else:
                self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                self.alert.show()

    def calculate_records_total(self,records):
       return reduce(lambda x, y: x + y, records)

    def change_load_text(self):
        self.ui.btn_load.setText('Loading...')

    def data_visualization(self):
        if self.ui.pie_chart.isChecked():
            self.report_piechart()
            self.ui.btn_load.setText('Load')
        elif self.ui.bar_chart.isChecked():
            self.barchart_plots()
            self.ui.btn_load.setText('Load')
        elif self.ui.line_graph.isChecked():
            self.line_plot()
            self.ui.btn_load.setText('Load')

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
        
    def query_database(self, query: str):
        db,my_cursor,connection_status = self.database.my_cursor()
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        db.commit()
        my_cursor.close()
        if cursor:
            for item in cursor:
                details.append(item)
        return details
    
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
        try:
            student_reference=self.value_formater(self.ui.search_box.text())
            results=self.query_cache_data_list("SELECT * FROM tb_attendance WHERE student_reference="+student_reference)
            self.ui_table(results)
            if self.ui.search_box.text():
                db_data=self.fetch_data_from_db(self.ui.search_box.text())
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
                    self.load_image_from_db("SELECT student_reference,student_image from tb_student_images WHERE student_reference="+student_reference,self.ui.db_image_data)
                else:
                    self.alert_builder("Student details not found. Please enter\nyour details to register!")
            else:
                self.alert_builder("Oops! search field can't be empty.")
        except:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid search parameter...")
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
                    self.fetch_data_by_program_and_date()
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
                        self.query_for_data_by_date_range()
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
                    self.fetch_details_for_card_view()
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
        
    def get_report_date(self):
        date_ = self.ui.report_date.date().toPython()
        if self.ui.report_date_range.isChecked():
             self.ui.report_end_date.setText(str(date_))
        else:
            self.ui.report_start_date.setText(str(date_))
  
    def get_registration_start_date(self):
        date = self.ui.calendarWidget_reg.selectedDate()
        if self.ui.change_date_box.isChecked():
            expiry_date=str(date.toPython())
            end_date= expiry_date.split('-') 
            expiry_date_transformed = datetime.date(int(end_date[0]),int(end_date[1]),int(end_date[2])).strftime("%b %Y")  
            self.ui.reg_end_date.setText(expiry_date_transformed)
        else:
            start_date=str(date.toPython())
            start_date = start_date.split('-')
            issued_date_transformed = datetime.date(int(start_date[0]),int(start_date[1]),int(start_date[2])).strftime("%b %Y")
            self.ui.reg_start_date.setText(issued_date_transformed)
    

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
            return details.replace('name',self.ui.reg_firstname.text())

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

    def generate_code(self):
        code = Code(
            index=self.ui.reg_index.text(),
            reference=self.ui.reg_student_ref.text(),
            email_address=self.ui.reg_email.text()
        )
        if code.reference !='':
            code ={"reference":code.reference}
            code_json=self.convert_to_json(code)
            image = qrcode.make(code_json)
            path = 'C:\\ProgramData\\iAttend\\data\\qr_code\\'+self.ui.reg_student_ref.text()+".png"
            image.save(path)
            return path
            
    def prepare_email(self):
        details = self.get_email_details()
        path = self.generate_code()
        content = self.get_mail_content()
        self.mail = QRCodeMailThread(details,content,path)
        self.mail.start()

    def prepare_email_to_send(self):
        self.alert = AlertDialog()
        if self.connected_to_internet()==True and self.ui.reg_email.text():
            try:
                self.prepare_email()
                self.alert.content("Hey! mail sent successfully...")
                self.alert.show()
            except Exception as e:
                self.alert.content(str(e))
                self.alert.show()
        else:
            self.alert.content("Oops! something went wrong mail\nnot sent...")
            self.alert.show()

    def send_mail(self):
        self.alert = AlertDialog()
        if self.database.check_state():
            self.alert.content("Oops! no database is configured...")
            self.alert.show()
        else:
            self.prepare_email_to_send()

    def get_student_data(self):
        if  self.ui.reg_disability.isChecked():
            self.disability = "Yes"
        else:
            self.disability = "No"
       
        student = Student(
            self.ui.reg_student_ref.text(),
            self.ui.reg_index.text(),
            self.ui.reg_firstname.text()+" "+self.ui.reg_middlename.text(),
            self.ui.reg_lastname.text(),
            self.ui.reg_nationality.text(),
            self.ui.reg_gender.currentText(),
            self.disability,
            self.ui.reg_start_date.text(),
            self.ui.reg_end_date.text()) 
        college = College(
            self.ui.reg_college.currentText(),
            self.ui.reg_faculty.currentText(),
            self.ui.reg_programs.currentText(),
            self.ui.reg_type.currentText()
        )
        return student,college

    def validate_student_fields(self):
        student,college=self.get_student_data()
        student_list = [student.student_firstname,student.student_lastname,
                        student.student_reference,student.student_index,
                        student.student_nationality,student.card_issued_date,
                        student.card_expiry_date,college.student_college,
                        college.student_faculty,college.student_program]
        data_list = []
        empty_list = []
        for field in student_list:
            if field:
                data_list.append(field)
            else:
               empty_list.append(field)
        return data_list,empty_list

    def register_student(self):
        _,empty_list=self.validate_student_fields()
        student,college=self.get_student_data()
        check_state=self.database.check_state()
        try:
            (db,my_cursor,connection_status) = self.database.my_cursor()
            if len(empty_list)==0 :
                details=self.fetch_data_from_server("SELECT * FROM tb_students WHERE student_reference="+self.value_formater(student.student_reference))
                root_path = 'C:\\ProgramData\\iAttend\\data\\images\\'
                if not details:
                    if check_state == True:
                        self.alert_builder("Oops! no database configured...")
                    else:
                        if self.ui.image_file_reg.text() and self.ui.file_system.isChecked():
                            my_cursor.execute("INSERT INTO tb_students(student_reference,student_index,student_firstname,student_lastname,student_nationality,student_gender,student_disability,card_issued_date,card_expiry_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (student.student_reference,student.student_index,student.student_firstname,student.student_lastname,student.student_nationality,student.student_gender,student.student_disability,student.card_issued_date,student.card_expiry_date))   
                            db.commit()
                            my_cursor.execute("INSERT INTO tb_student_study_details(student_reference,student_college,student_faculty,student_program,student_category) VALUES (%s,%s,%s,%s,%s)",
                            (student.student_reference,college.student_college,college.student_faculty,college.student_program,college.student_category))   
                            db.commit()
                            with open(self.ui.image_file_reg.text(),'rb') as image:
                                data = image.read()
                                my_cursor.execute("INSERT INTO tb_student_images(student_reference,student_image) VALUES(%s,%s)",(student.student_reference,data))
                            db.commit()
                            my_cursor.close() 
                            self.alert_builder("Student registered successfully")    
                        elif self.ui.image_less.isChecked():
                            path = self.resource_path('image.jpg')
                            my_cursor.execute("INSERT INTO tb_students(student_reference,student_index,student_firstname,student_lastname,student_nationality,student_gender,student_disability,card_issued_date,card_expiry_date) VALUES (?,?,?,?,?,?,?,?,?)",
                            (student.student_reference,student.student_index,student.student_firstname,student.student_lastname,student.student_nationality,student.student_gender,student.student_disability,student.card_issued_date,student.card_expiry_date))   
                            db.commit()
                            my_cursor.execute("INSERT INTO tb_student_study_details(student_reference,student_college,student_faculty,student_program,student_category) VALUES (?,?,?,?,?)",
                            (student.student_reference,college.student_college,college.student_faculty,college.student_program,college.student_category))   
                            db.commit()
                            with open(path,'rb') as image:
                                data = image.read()
                                my_cursor.execute("INSERT INTO tb_student_images(student_reference,student_image) VALUES(?,?)",(student.student_reference,data))
                            db.commit()
                            my_cursor.close() 
                            self.alert_builder("Student registered successfully")    
                else:
                    self.alert_builder("Oops! student with this reference\nalready exists")
            else:
                self.alert_builder("Oops! some information is not\ncaptured...")
        except Exception as e:
            self.alert_builder(str(e))

    def alert_builder(self, message:str):
        self.alert = AlertDialog()
        self.alert.content(message)
        self.alert.show()
          
    def search_thread(self):
        reference = self.ui.search_reg.text()
        if reference:
            student_reference=self.value_formater(reference)
            db_data=self.fetch_data_from_server("SELECT * FROM tb_students INNER JOIN tb_student_study_details ON tb_students.student_reference=tb_student_study_details.student_reference WHERE tb_students.student_reference="+student_reference)
            if db_data:
                helper = str(db_data[3]).split(" ")
                self.ui.reg_firstname.setText(helper[0])
                self.ui.reg_middlename.setText(helper[1])
                self.ui.reg_lastname.setText(db_data[4])
                self.ui.reg_student_ref.setText(str(db_data[1]))
                self.ui.reg_index.setText(str(db_data[2]))
                self.ui.reg_nationality.setText(db_data[5])
                self.ui.reg_gender.setCurrentText(str(db_data[6]))
                self.ui.reg_start_date.setText(db_data[8])
                self.ui.reg_end_date.setText(db_data[9])
                self.ui.reg_college.setCurrentText(str(db_data[12]))
                faculty=load_faculties(self.resource_path('structure.json'),str(db_data[12]))
                self.ui.reg_faculty.clear()
                self.ui.reg_faculty.addItems(faculty)
                self.ui.reg_faculty.setCurrentText(str(db_data[13]))
                program = get_dept(self.resource_path('structure.json'),str(db_data[12]),str(db_data[13]))
                self.ui.reg_programs.clear()
                self.ui.reg_programs.addItems(program)
                self.ui.reg_programs.setCurrentText(str(db_data[14]))
                self.ui.reg_type.setCurrentText(str(db_data[15]))
                if str(db_data[7])=='YES':
                    self.ui.reg_disability.setChecked(True)
                self.load_image_from_db("SELECT student_reference,student_image from tb_student_images WHERE student_reference="+student_reference,self.ui.reg_image)
            else:
                self.alert_builder("Student not found. Please enter\nyour details to register!")
        else:
            self.alert_builder("Oops! search field can't be empty.")
        
    def search_student(self):
        self.search_thread()
        
    def update_student(self):
        check_state = self.database.check_state()
        self.alert = AlertDialog()
        try:
            db = sqlite3.connect(self.get_cache_path())
            my_cursor = db.cursor()
            if self.ui.reg_student_ref.text() and self.ui.image_file_reg.text() and self.ui.file_system.isChecked():
                ref = self.ui.reg_student_ref.text()
                with open(self.ui.image_file_reg.text(), 'rb') as image:
                    data = image.read()
                    if check_state == True:
                        self.alert_builder("Oops! no database configured...")  
                    else:
                        my_cursor.execute("UPDATE tb_student_images SET student_image=? WHERE student_reference=?",(data,ref))
                    db.commit()
                    my_cursor.close()
                self.alert_builder("Hey! Student image updated successfully.")
           
        except Exception as e:
            self.alert.content("Document saved successfully")
            self.alert.show()

    def remove_student(self):
        check_state = self.database.check_state()
        try:
            (db,my_cursor,connection_status) = self.database.my_cursor()
            if check_state == True:
                self.alert_builder("Oops! no database configured...")
            else: 
                if self.ui.reg_student_ref.text():
                    student_reference=self.value_formater(self.ui.reg_student_ref.text()) 
                    my_cursor.execute("DELETE FROM tb_students where student_reference="+student_reference)
                    db.commit()
                    my_cursor.close()
                    db_cache = sqlite3.connect(self.get_cache_path())
                    cache_cursor = db_cache.cursor()
                    cache_cursor.execute("DELETE FROM tb_students where student_reference="+student_reference)
                    cache_cursor.execute("DELETE FROM tb_student_images where student_reference="+student_reference)
                    db_cache.commit()
                    cache_cursor.close()
                    self.resets_fileds()
                    self.alert_builder("Student data removed successfuly!")
                else:
                    self.alert_builder("Oops! student reference not\nprovided...")

        except:
            self.alert_builder("Oops! internal server error!")

    def add_category(self):
        self.alert = AlertDialog()
        category = self.ui.category_field.text()
        path = self.resource_path("categories.txt")
        if category:
            if os.path.exists(path):
                with open(path,'r+') as file:
                    data=file.readlines()
                    categorylist = []
                    for line in data:
                        categorylist.append(line)
                    if category not in categorylist:
                        file.writelines(f'\n{category}')
                        self.alert.content("Category added successfully...")
                        self.alert.show()
                    else:
                        self.alert.content("Oops! category already exist...")
                        self.alert.show()
                file.close()
        else:
            self.alert.content("Oops! invalid category provided...")
            self.alert.show()
    
    def refresh_category(self):
        self.ui.reg_type.clear()
        self.ui.reg_type.addItems(self.read_category(self.resource_path('categories.txt')))

    def resets_fileds(self):
        self.ui.reg_firstname.setText("")
        self.ui.reg_middlename.setText("")
        self.ui.reg_lastname.setText("")
        self.ui.reg_student_ref.setText("")
        self.ui.reg_index.setText("")
        self.ui.reg_nationality.setText("")
        self.ui.reg_start_date.setText("")
        self.ui.reg_end_date.setText("")
        self.ui.reg_college.setCurrentText("CoS")
        self.ui.reg_faculty.clear()
        self.ui.reg_faculty.addItems(load_faculties(self.resource_path('structure.json'),"CoS"))
        self.ui.reg_type.setCurrentText("Undergraduate")
        self.ui.reg_gender.setCurrentText("Male")
        program = get_dept(self.resource_path('structure.json'),self.ui.reg_college.currentText(),self.ui.reg_faculty.currentText())
        self.ui.reg_programs.clear()
        self.ui.reg_programs.addItems(program)
        self.ui.reg_image.setPixmap(u":/icons/asset/image.svg")
        self.ui.reg_image.setScaledContents(False)

    def connected_to_internet(self,url='http://www.google.com/', timeout=5):
        try:
            _ = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError:  
            return False

    def browse_image_files(self):
        if self.ui.file_system.isChecked():    
            path= QFileDialog.getOpenFileName(self, "Select File","C:\\Pictures","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png)")
            if path:
                self.ui.image_file_reg.setText(path[0])
                self.ui.reg_image.setPixmap(QPixmap.fromImage(path[0]))
                self.ui.reg_image.setScaledContents(True)
        elif self.ui.online_image.isChecked():
            self.alert = AlertDialog()
            if self.connected_to_internet()==True and self.ui.image_file_reg.text():
                self.pool = QThreadPool()
                self.work = SendThread(self.download_image)
                self.pool.start(self.work)
                self.alert.content("Image downloaded successfully!")
                self.alert.show()
            elif self.connected_to_internet()==False:
                 self.alert_builder("Oops! check you internet connection!") 

    def download_image(self):
        try:
            link = requests.get(self.ui.image_file_reg.text())
            image_path = 'C:\\Pictures\\iAttend\\downloaded_image.jpg'
            path ='C:\\Pictures\\iAttend\\'
            wget.download(link.url,image_path)
            self.ui.reg_image.setPixmap(QPixmap.fromImage(image_path))
            self.ui.reg_image.setScaledContents(True)
            self.alert_builder(f"Image downloaded successfully..\nlocation {path}") 
        except Exception as e:
            self.alert_builder("Oops! check your image url!")       

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

    def last_seen(self,reference:str):  
        (db,my_cursor,connection_status) = self.database.my_cursor()
        check_state=self.database.check_state()
        student_reference=self.value_formater(reference)
        if check_state == True:
            cursor=my_cursor.execute("SELECT user_date,user_logout,user_duration FROM tb_user_session WHERE user_reference = "+student_reference)
            cursor= my_cursor.fetchall()
            db.commit()       
        else:
            db = sqlite3.connect(self.get_cache_path())
            _cursor = db.cursor()
            cursor=_cursor.execute("SELECT date_stamp,time_out,duration FROM tb_attendance_last_seen WHERE student_reference = "+student_reference)
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

    def insert_into_cache_db(self,data: list):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        student_reference=self.value_formater(data[1])
        db_cache=self.query_cache_database("SELECT * FROM tb_students WHERE student_reference="+student_reference)
        if not db_cache:
            cursor.execute("INSERT INTO tb_students(student_reference,student_index,student_firstname,student_lastname,student_nationality,student_gender,student_disability,card_issued_date,card_expiry_date) VALUES (?,?,?,?,?,?,?,?,?)",
            (data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))   
            db.commit()
            cursor.execute("INSERT INTO tb_student_study_details(student_reference,student_college,student_faculty,student_program,student_category) VALUES (?,?,?,?,?)",
            (data[11],data[12],data[13],data[14],data[15]))   
            db.commit()       

    def fetch_data_from_server(self,query):
        try:
            (db,my_cursor,connection_status) = self.database.my_cursor()
            detail =my_cursor.execute(query)
            detail= my_cursor.fetchone()
            db.commit()
            my_cursor.close()
            db_data = []
            if detail:
                for data in detail:
                    db_data.append(data)
                return db_data
        except Exception as e:
            self.alert_builder(str(e)) 
        
    def load_image_from_db(self,query,label):
        db = sqlite3.connect(self.get_cache_path())
        my_cursor = db.cursor()
        cursor=my_cursor.execute(query)
        cursor= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        image_data = []
        root_path = 'C:\\ProgramData\\iAttend\\data\\images\\database_image.jpg'
        if cursor:
            for data in cursor:
                image_data.append(data)
            if len(image_data)>0:
                with open(root_path,'wb') as image_file:
                        image_file.write(image_data[1])
            label.setPixmap(QPixmap.fromImage(root_path))
            label.setScaledContents(True)
        else:
            label.setPixmap(QPixmap.fromImage(self.resource_path('image.jpg')))
            label.setScaledContents(True)        
                
    #improvements to be done or change code here      
    def fetch_data_from_db(self,reference):
        data_json = json.loads(reference)
        try:
            student_reference=self.value_formater(data_json['reference'])
            db_cache=self.query_cache_database("SELECT * FROM tb_students INNER JOIN tb_student_study_details ON tb_students.student_reference=tb_student_study_details.student_reference WHERE tb_students.student_reference="+student_reference)
            if len(db_cache) > 0:
                self.server_logs('[CACHED]',db_cache[:2])
                self.update_interface_cache(db_cache)
                self.last_seen(data_json['reference'])
                print('Data from cache>>>>>>>>>>')
            else:
                path = 'C:\\ProgramData\\iAttend\\data\\student\\information.json'
                with open(path,'r') as content:
                    results = json.load(content)
                content.close()
                if  results['reference'] != self.ui.reference.text():
                    self.retreive_student_details_api_thread(reference)
                    winsound.Beep(1000,100)
                    self.show_info("Waiting for response from server...") 
                    print(results['reference'],self.ui.reference.text())
                else:
                    print(results['reference'],self.ui.reference.text())
                    print('Equal')
                    self.show_info("Response from server updated on interface...") 

                with open(path,'r') as content:
                    update = json.load(content)
                    if update['firstname'] != 'firstname':
                        self.update_interface(self.read_student_information_json())
                        self.last_seen(data_json['reference'])
                        print('Data from server>>>>>>>>>>')
        except Exception as e:
            self.alert_builder(str(e))   
   
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

    def retreive_student_details(self,data):
        data_json = json.loads(data)
        if isinstance(data, str):
                self.last_seen(data_json['reference'])
                db_data=self.fetch_data_from_db(data_json['reference'])
                if db_data:
                    student_reference = self.value_formater(db_data[1])
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
                    self.load_image_from_db("SELECT student_reference,student_image FROM tb_student_images WHERE student_reference="+student_reference,self.ui.image)
                    self.insert_into_cache_db(db_data)
                else:
                    self.loadUi_file()
                    self.show_info("Oops! student not found. Please register!")                


    def read_student_information_json(self):
        with open('C:\\ProgramData\\iAttend\\data\\student\\information.json','r') as content:
            data = content.read()
            try:
                return json.loads(data)
            except Exception as e:
                pass
            
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
            self.ui.type.setText(request_body_json['type'])
        else:
            self.loadUi_file()
            self.show_info("Oops! student not found. Please register!") 

    def retreive_student_details_api_thread(self,data):
        data_json = json.loads(data)
        details_url,images_url=self.restapi.get_field_text()
        if isinstance(data, str):
            details_request=details_url.replace('reference',data_json['reference'])
            self.data= RequestThread(url_details=details_request)
            if self.data.isRunning()==True:
                pass
            else:
                self.data.start()
           

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
        (db,my_cursor,connection_status) = self.database.my_cursor()
        cache_db = sqlite3.connect(self.get_cache_path())
        cursor = cache_db.cursor()
        attendance=self.attendance_data()
        check_state = self.database.check_state()
        details = []
        date="\'{}\'".format(current.now().date().strftime("%Y-%m-%d"))
        student_reference=self.value_formater(self.ui.reference.text())
        if self.ui.reference.text() != "Reference" and self.ui.reference.text() !="" :
            data=cursor.execute("SELECT student_reference,date_stamp FROM tb_attendance_temp WHERE student_reference="+student_reference+" and date_stamp="+date)
            data=cursor.fetchone()
            if data:
                for item in data:
                    details.append(item)
                db.commit()
            if not details:
                if check_state==True:
                    self.ui.label_notification.setText("Oops! no database configured...")
                else: 
                    cursor.execute("INSERT INTO tb_attendance_temp(student_reference,student_college,student_faculty,student_program,student_category,student_nationality,student_gender,student_disability,date_stamp,time_in,time_out,duration) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (attendance.student_reference,attendance.student_college,attendance.student_faculty,attendance.student_program,attendance.student_category,attendance.student_nationality,attendance.student_gender,attendance.student_disability,attendance.date_stamp,attendance.time_in,attendance.time_out,attendance.duration))
                    cache_db.commit()
            elif details:
                winsound.Beep(1000,100)
                self.show_info("Attendance taken, you can proceed!\nNext person please...")
            else:
                 self.show_info("Oops! something went wrong...")
        db.close()

    def connect_to_camera(self):
        if self.ui.comboBox.currentText():
            self.show_info("Connecting to selected device\nthis may take some few seconds...")
        pass

    def start_webcam(self):
        self.show_alert = AlertDialog()
        if self.ui.camera_ip.text() or self.ui.comboBox.currentText():
            ip_address = self.ui.camera_ip.text()
            system_attached_camera = self.ui.comboBox.currentText()
            self.network_capture = VideoCapture(ip_address)
            if ip_address:  
                if self.network_capture is None or not self.network_capture.isOpened():    
                    self.stop_webcam
                    self.show_alert.content("Oops! check the camera ip address\nconnetion or is already in use.") 
                    self.show_alert.show()
                else:
                    self.capture = VideoCapture(ip_address)    
            elif system_attached_camera:
                camera_id = int(system_attached_camera)
                self.system_capture = VideoCapture(camera_id)       
                if self.system_capture is None or not self.system_capture.isOpened():    
                    self.stop_webcam
                    self.show_alert.content("Oops! check the camera for\nconnetion or is already in use.")  
                    self.show_alert.show()
                else:
                    self.capture = VideoCapture(camera_id)                  
            elif self.system_capture.isOpened() and self.network_capture.isOpened():
                    self.capture = VideoCapture(camera_id)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            self.timer.timeout.connect(self.update_frame)
            self.show_info("Connected to selected device\nsuccessfully...") 
            self.timer.start(3)
        else:
            self.show_alert.content("Oops! your have no active cameras available")  
            self.show_alert.show()

    def retrieve_information(self,qr_code_data):
        path = 'C:\\ProgramData\\iAttend\\data\\student\\information.json'
        data_json = json.loads(qr_code_data)
        with open(path,'r') as content:
            results = json.load(content)
        content.close()
        if  results['reference'] != self.ui.reference.text():
            self.retreive_student_details_api_thread(qr_code_data)
            winsound.Beep(1000,100)
            self.show_info("Waiting for response from server...") 
            print(results['reference'],self.ui.reference.text())
        else:
            print(results['reference'],self.ui.reference.text())
            print('Equal')
            self.show_info("Response from server updated on interface...") 

        with open(path,'r') as content:
            update = json.load(content)
            if update['firstname'] != 'firstname':
                self.update_interface(self.read_student_information_json())
                self.last_seen(data_json['reference'])
                # self.mark_attendance_db()

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
            check_state = self.database.check_state()
            if check_state == True:
                self.ui.label_notification.setText("Oops! no database configured...")
                winsound.Beep(1000,100)
            else:
                self.fetch_data_from_db(qr_code_data)
                # self.retreive_student_details(qr_code_data)
                # self.retrieve_information(qr_code_data)
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
            update_information_file()
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
        self.database = Database()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui_login.btn_close.clicked.connect(self.close)
        self.ui_login.btn_minimize.clicked.connect(self.showMinimized)
        self.ui_login.btn_close.clicked.connect(self.close)
        self.ui_login.avater.setDisabled(True)
        self.ui_login.btn_login.clicked.connect(self.login)
        self.retrieve = ForgotPassword()
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
        if self.database.check_state():
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
        self.create_database_tables()
        self.populate_root_user_data()
        self.create_cache_database()
        self.show()       
        
    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.application_logs("Application bootstrapping process completed")
            # self.main = MainWindow()
            self.main = Authentication()
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

    def create_program_directory(self):
        root_dir = 'C:\\ProgramData\\iAttend\\data'
        list =('batch_logs','properties','qr_code',
        'email_details','reports','exports','cache',
        'images','partition','application_logs','student',
        'httpErrors','user','student_images')

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
        cache = ('database','logs')    
        for item in cache:
            path = os.path.join(cache_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)

        report_dir = 'C:\\ProgramData\\iAttend\\data\\reports'
        report = ('piechart','barchart','linegraph','visualize')    
        for item in report:
            path = os.path.join(report_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)
        
        export_dir = 'C:\\ProgramData\\iAttend\\data\\exports'
        export = ('csv','json')
        for item in export:
            path = os.path.join(export_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)

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

        json_data = {
            "details": "http://localhost/api/v1/user/details/reference",
            "images": "http://localhost/api/v1/user/images/reference"
        }
        path =os.path.join(root,'user\\api_routes.json')
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
        
        path =os.path.join(root,'student\\information.json')
        student_json={
            'firstname': 'firstname', 
            'othername': 'othername', 
            'lastname': 'lastname', 
            'reference': 'reference', 
            'index': 'index', 
            'nationality': 'nationality', 
            'college': 'college', 
            'type': 'type', 
            'gender': 'gender', 
            'disabled': 'disabled', 
            'department': 'department', 
            'faculty': 'faculty', 
            'validity': 'validity'
        }
        self.write_to_file(path,student_json,'json')

        path =os.path.join(root,'user\\user.json')
        user_json={
            'firstname': 'firstname', 
            'othername': 'othername', 
            'lastname': 'lastname',
            'reference': 'reference', 
            }
        self.write_to_file(path,user_json,'json')

        path =os.path.join(root,'properties\\students_restapi_endpoints.json')
        json_data = {
            "details":"http://localhost/api/v1/students/details/reference",
            "images":"http://localhost/api/v1/students/images/reference",
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

    def create_database_tables(self):
        db = sqlite3.connect(self.get_path())
        cursor = db.cursor()
        cursor.execute(create_tb_cameras_sqlite())
        cursor.execute(create_tb_user_details_sqlite())
        cursor.execute(create_tb_user_credentials_sqlite())
        cursor.execute(create_tb_user_profile_sqlite())
        cursor.execute(create_tb_user_sessions_sqlite())
        cursor.execute(create_tb_user_sessions_last_seen_sqlite())
        db.commit()

    def create_cache_database(self):
        db = sqlite3.connect(self.get_cache_path())
        cursor = db.cursor()
        cursor.execute(create_tb_students_sqlite())
        cursor.execute(create_tb_attendance_sqlite())
        cursor.execute(create_tb_images_sqlite())
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
        db = sqlite3.connect(self.get_path())
        cursor = db.cursor()
        details=self.query_user_data("SELECT * FROM tb_user_details WHERE user_reference="+root_reference)
        self.query_user_data("SELECT * FROM tb_user_credentials WHERE user_reference="+root_reference)
        if not details:
            password_hash = hash_password(root_password)
            cursor.execute("INSERT INTO tb_user_details (user_reference,user_firstname,user_lastname,user_contact,user_role,user_mail) VALUES (?,?,?,?,?,?)",
            (root_reference,root_firstname,root_lastname,root_contact,root_role,root_mail)) 
            cursor.execute("INSERT INTO tb_user_credentials (user_reference,user_username,user_password,user_status) VALUES (?,?,?,?)",
            (root_reference,root_username,password_hash,root_status))    
            db.commit()
            self.insert_profile_image(root_reference,self.resource_path('image.jpg'))
        pass 

    def insert_profile_image(self,reference,path):
        db = sqlite3.connect(self.get_path())
        cursor = db.cursor()
        with open(path,'rb') as image_data:
            data = image_data.read()
        cursor.execute("INSERT INTO tb_user_profile(user_reference,user_image) VALUES(?,?)",(reference,data))
        db.commit()    

    def get_path(self):
        return 'C:\\ProgramData\\iAttend\\data\\database\\attendance.db' 

    def query_user_data(self,query):
        db = sqlite3.connect(self.get_path())
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
        window.application_logs("Application bootstrapping process in progress")  
        sys.exit(application.exec_())
    except Exception as e:
        window.application_logs(str(e))