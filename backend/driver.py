################################################################################
##
## BY: Asamani Redolf
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

from packages.misc import *
from packages.mail import *
from packages.pyqt import *
from packages.model import *
from packages.system import *
from packages.camera import *
from packages.report import *
from packages.startup import *
from packages.globals import *
from packages.computing import *
from packages.processing import *

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
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        # self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        self.ui.btn_clear_label.clicked.connect(self.loadUi_file)
        #########################################################################################

        #########################################################################################################
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_admin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.admin))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.database))
        self.ui.btn_help.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))
        self.ui.btn_report.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report))
        self.ui.btn_batch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.batch))
        ##########################################################################################################

        #########################################################################################################
        self.piechart = Piechart()
        self.barchart = Barchart()
        self.line_graph = Line_plot()
        ########################################################################################################
        self.create_program_data_dir()
        self.set_sender_details()
        #########################################################################################
        self.open_exit_camera = ExitCameraFeed()
        self.ui.btn_open_exit_camera_ui.clicked.connect(lambda: self.open_exit_camera.show())
        
        self.database = Database()
        self.ui.btn_open_database.clicked.connect(lambda: self.database.show())

        self.mail = Mail()
        self.ui.btn_mail_report_or_data.clicked.connect(lambda: self.mail.show())

        self.directory = Images()
        self.ui.btn_batch_folder.clicked.connect(lambda: self.directory.show())
        
        self.user = User()
        self.ui.btn_login_user.clicked.connect(lambda: self.user.show())

        self.config = Configuration()
        self.ui.btn_camera.clicked.connect(lambda: self.config.show())
        self.camera_1 = Camera_One()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_1.show())
        self.camera_2 = Camera_Two()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_2.show())
        self.camera_3 = Camera_Three()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_3.show())
        self.camera_4 = Camera_Four()
        self.ui.btn_camera.clicked.connect(lambda: self.camera_4.show())

        self.login = Authentication()
        # self.ui.btn_logout.clicked.connect(lambda: self.login.show())
        self.ui.btn_logout.clicked.connect(self.logout)
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
        self.ui.btn_register.clicked.connect(self.register_student)
        self.ui.btn_clear.clicked.connect(self.resets_fileds)
        self.ui.btn_update.clicked.connect(self.update_student)
        self.ui.btn_remove.clicked.connect(self.remove_student)
        self.ui.btn_browse_reg.clicked.connect(self.browse_image_files)
        self.ui.btn_send_mail.clicked.connect(self.send_mail)
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

        ##################################################################################################
        self.ui.btn_load.clicked.connect(self.data_visualization_thread)
        self.ui.report_start_date.textChanged.connect(self.report_start_date_value_change)
        self.ui.btn_refresh.clicked.connect(self.hot_reload_thread)
        self.ui.btn_save.clicked.connect(self.save_report)
        self.ui.btn_backup.clicked.connect(self.backup_database)
        #################################################################################################

        college,programs=self.get_programs_CoS()
        completer = QCompleter(programs)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.search_box.setCompleter(completer)
        country_completer = QCompleter(self.country_names('C:\\ProgramData\\iAttend\\data\\json_file\\data_json.json'))
        country_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.reg_nationality.setCompleter(country_completer)
        
        self.ui.reg_college_2.addItem(college,programs)
        self.ui.reg_college_2.currentIndexChanged.connect(self.update_program_combo)
        self.update_program_combo(self.ui.reg_college_2.currentIndex())
        self.ui.college_comboBox.addItem(college)
        self.ui.college_courses.addItems(programs)
        self.ui.btn_remove_combox_item.clicked.connect(self.remove_item_from_comboBox)
        self.ui.btn_scan_range.clicked.connect(self.camera_thread)
        self.ui.btn_batch_browse.clicked.connect(self.browse_batch_data)
        self.ui.btn_start_job.clicked.connect(self.insert_records_thread)
        self.ui.btn_batch_images.clicked.connect(self.insert_images_thread)
        self.ui.btn_batch_mail.clicked.connect(self.send_code_thread)

        self.ui.user_image_browse.clicked.connect(self.user_profile_image)
        self.ui.btn_user_register.clicked.connect(self.register_user)
        self.ui.btn_user_status.clicked.connect(self.update_user_status)
        self.ui.btn_user_update.clicked.connect(self.update_user_details)
        self.ui.btn_user_clear.clicked.connect(self.clear_user_details)
        ##################################################################################################

    def search_user():
        pass
    
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
        check_state = self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        self.alert = AlertDialog()
        if self.ui.user_reference.text():
            if check_state == True:
                my_cursor.execute("UPDATE tb_user_credentials SET user_status =? WHERE user_reference=?",
                (self.ui.user_status.currentText(),self.ui.user_reference.text()))
                db.commit()
                my_cursor.close()
                self.alert.content(f"User with {self.ui.user_reference.text()} status updated\nto {self.ui.user_status.currentText()}")
                self.alert.show()
            else:
                my_cursor.execute("UPDATE tb_user_credentials SET user_status =%s WHERE user_reference=%s",
                (self.ui.user_status.currentText(),self.ui.user_reference.text()))
                db.commit()
                my_cursor.close()
                self.alert.content(f"User with {self.ui.user_reference.text()} status updated\nto {self.ui.user_status.currentText()}")
                self.alert.show()
        else: 
            self.alert.content("Oops! can't change status for\nundefined user.")
            self.alert.show()

    def update_user_details(self):
        check_state = self.database.check_state()
        user = self.set_user_details()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        self.alert = AlertDialog()
        if self.ui.user_reference.text() and self.ui.user_contact.text() and self.ui.user_email.text():
            if check_state == True:
                my_cursor.execute("UPDATE tb_user_details SET user_contact =?, user_role =?, user_mail =? WHERE user_reference=?",
                (user.contact,user.role,user.mail,user.reference))
                db.commit()
                my_cursor.close()
                self.alert.content(f"User with {self.ui.user_reference.text()} some details\nupdated")
                self.alert.show()
            else:
                my_cursor.execute("UPDATE tb_user_details SET user_contact =%s, user_role =%s, user_mail =%s WHERE user_reference=%s",
                (user.contact,user.role,user.mail,user.reference))
                db.commit()
                my_cursor.close()
                self.alert.content(f"User with {self.ui.user_reference.text()} some details\nupdated")
                self.alert.show()
        else: 
            self.alert.content("Oops! can't change status for\nundefined user.")
            self.alert.show()

    def register_user(self):
        self.alert = AlertDialog()
        user = self.set_user_details()
        credentials = self.set_user_credentials()
        check_state=self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        root_path = 'C:\\ProgramData\\iAttend\\data\\images\\image.jpg'
        if self.ui.user_reference.text() and self.ui.user_contact.text() and self.ui.user_firstname.text():
            details=self.query_user_data("SELECT * FROM tb_user_details WHERE user_reference="+user.reference)
            if not details:
                if check_state == True:
                    my_cursor.execute("INSERT INTO tb_user_details (user_reference,user_firstname,user_lastname,user_contact,user_role,user_mail) VALUES (?,?,?,?,?,?)",
                    (user.reference,user.firstname,user.lastname,user.contact,user.role,user.mail)) 
                    my_cursor.execute("INSERT INTO tb_user_credentials (user_reference,user_username,user_password,user_status) VALUES (?,?,?,?)",
                    (credentials.reference,credentials.username,credentials.password,credentials.status))    
                    db.commit()
                    if self.ui.user_image_file.text():
                        with open(self.ui.user_image_file.text(), 'rb') as image_data:
                            data = image_data.read()
                        my_cursor.execute("INSERT INTO tb_user_profile(user_reference,user_image) VALUES(?,?)",(user.reference,data))
                        db.commit()
                    else:
                        with open(root_path, 'rb') as image_data:
                            data = image_data.read()
                        my_cursor.execute("INSERT INTO tb_user_profile(user_reference,user_image) VALUES(?,?)",(user.reference,data))
                        db.commit()
                    my_cursor.close()         
                else:   
                    my_cursor.execute("INSERT INTO tb_user_details (user_reference,user_firstname,user_lastname,user_contact,user_role,user_mail) VALUES (%s,%s,%s,%s,%s,%s)",
                    (user.reference,user.firstname,user.lastname,user.contact,user.role,user.mail))   
                    my_cursor.execute("INSERT INTO tb_user_credentials (user_reference,user_username,user_password,user_status) VALUES (%s,%s,%s,%s)",
                    (credentials.reference,credentials.username,credentials.password,credentials.status))
                    db.commit()
                    if self.ui.user_image_file.text():
                        with open(self.ui.user_image_file.text(), 'rb') as image_data:
                            data = image_data.read()
                        my_cursor.execute("INSERT INTO tb_user_profile(user_reference,user_image) VALUES(%s,%s)",(user.reference,data))
                        db.commit()
                    else:
                        with open(root_path, 'rb') as image_data:
                            data = image_data.read()
                        my_cursor.execute("INSERT INTO tb_user_profile(user_reference,user_image) VALUES(%s,%s)",(user.reference,data))
                        db.commit()
                    my_cursor.close()
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
            self.ui.user_role.currentText(),
            self.ui.user_email.text()
        )
        return user

    def set_user_credentials(self):
        user = self.set_user_details()
        credentials = LoginUser(
            user.reference,
            user.firstname,
            user.contact,
            self.ui.user_status.currentText()
        )
        return credentials
    
    def set_user_session(self):
        session = UserDetails(

        )
        return session
        pass

    def user_profile_image(self):
        path= QFileDialog.getOpenFileName(self, "Select File","","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png)")
        if path:
            self.ui.user_image_file.setText(path[0])
            self.ui.user_image.setPixmap(QPixmap.fromImage(path[0]))
            self.ui.user_image.setScaledContents(True)
        
    def logout(self):
        self.main = MainWindow()
        self.close()
        self.login.show()
        
    def hot_reload_thread(self):
        self.pool = QThreadPool()
        self.work = SendThread(self.hot_reload)
        self.pool.start(self.work)
        
    def data_visualization_thread(self):
        self.pool = QThreadPool()
        self.work = SendThread(self.data_visualization)
        self.pool.start(self.work)

    def send_code_thread(self):
        student_data_path = self.ui.batch_browse.text()
        if student_data_path and self.connected_to_internet()==True:
            self.pool = QThreadPool()
            self.work = SendThread(self.generate_code_and_send)
            self.pool.start(self.work)
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid file path or check\ninternet connectivity.....")
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
                    "index":student.index,
                    "reference":student.reference,
                    "mail_address":student.email_address
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
        path = self.directory.directory_path()
        if path:
            self.pool = QThreadPool()
            self.work = ImageThread(self.insert_images)
            self.pool.start(self.work)
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid file path...")
            self.alert.show()

    def insert_images(self):
        path = self.directory.directory_path()
        images_extension = ['jpg', 'jpeg', 'png'] 
        self.ui.batch_notification.setText("Saving images in progress...") 
        for item in os.listdir(path):
            image = os.path.join(path,item)
            image = os.path.abspath(image)
            image_name = os.path.basename(image)
            extension = image_name.split('.')[1]
            student_reference = image_name.split('.')[0]
            if extension in images_extension:
                check_state = self.database.check_state()
                (db,my_cursor,connection_status) = self.database.my_cursor()
                with open(image, 'rb') as image_data:
                    data = image_data.read()
                    if check_state == True:
                        my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(?,?)",(student_reference,data))
                        db.commit()
                        my_cursor.close()
                    else:
                        my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(%s,%s)",(student_reference,data))
                        db.commit()
                        my_cursor.close()
        self.ui.batch_notification.setText("All images saved successfully...")         

    def insert_records_thread(self): 
        path = self.directory.directory_path()
        if path:
            self.pool = QThreadPool()
            self.work = ImageThread(self.batch_insert_student_data)
            self.pool.start(self.work)
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid file path...")
            self.alert.show()

    def batch_insert_student_data(self):
        check_state=self.database.check_state()
        (db,my_cursor,connection_status) = self.database.my_cursor()
        student_list = self.load_batch_data()
        file_path = self.ui.batch_browse.text()
        date=datetime.now().strftime('%d_%B_%Y_%I_%M_%S_%p')
        name = str('record_logs')
        path = str('C:\\ProgramData\\iAttend\\data\\batch_logs\\'+name+'_'+date+'.txt')
        table=self.ui.tableWidget_batch.item(0,0)
        if file_path and table:
            self.ui.batch_notification.setText("Saving records in progress...")  
            if check_state == True:
                for student in student_list:
                    name = str(student[0]).split(' ')
                    date = str(student[6]).split('-')
                    firstname  = name[0]+' '+name[1]
                    details=self.fetch_data_from_db(str(student[2]))
                    if not details:
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (?,?,?,?,?,?,?,?,?)",
                        (student[2],student[1],firstname,name[2],student[4],student[3],student[5],date[0],date[1]))   
                        db.commit()
                    else:
                        with open(path,'a+') as file: 
                            file.writelines('\n'+str(student))
                        file.close
                self.ui.batch_notification.setText("Valid records saved successfully...")
            else:
                for student in student_list:
                    name = str(student[0]).split(' ')
                    date = str(student[6]).split('-')
                    firstname  = name[0]+' '+name[1]
                    details=self.fetch_data_from_db(str(student[2]))
                    if not details:
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (student[2],student[1],firstname,name[2],student[4],student[3],student[5],date[0],date[1]))   
                        db.commit()
                    else:
                        with open(path,'a+') as file:
                            file.writelines('\n'+str(student))
                        file.close
                self.ui.batch_notification.setText("Valid records saved successfully...")
        else:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid file path or content is empty...")
            self.alert.show()
       
    def load_batch_data(self):
        results_list = []
        path = self.ui.batch_browse.text()
        if path:
            with open(path,'r') as filename:
                data=csv.reader(filename)
                next(data)
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
        self.ui.tableWidget_batch.setColumnWidth(0,230)
        self.ui.tableWidget_batch.setColumnWidth(1,140)
        self.ui.tableWidget_batch.setColumnWidth(2,140)
        self.ui.tableWidget_batch.setColumnWidth(3,200)
        self.ui.tableWidget_batch.setColumnWidth(4,100)
        self.ui.tableWidget_batch.setColumnWidth(5,190)
        self.ui.tableWidget_batch.setColumnWidth(6,180)
        self.ui.tableWidget_batch.setColumnWidth(7,200)
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
            row_count = row_count+1
        
    def browse_batch_data(self):
        file_type = "CSV Files(*.csv)"   
        path= QFileDialog.getOpenFileName(self, "Select File","C:\\Users\\BTC OMEN\\Documents",file_type)
        if path:
            self.ui.batch_browse.setText(path[0])
            try:
                self.batch_table(self.load_batch_data())
                self.alert = AlertDialog()
                self.alert.content("Please the header was skipped...")
                self.alert.show()
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str("Oops! invalid file format\n"+str(e)))
                self.alert.show()

    def get_programs_CoS(self):
        path = 'C:\\ProgramData\\iAttend\\data\\programs\\CoS_programs.txt'
        with open(path,'r') as file:
            basedir = os.path.basename(path)
            basedir=basedir.split("_")[0]
            programs_list = []
            programs = file.read().split(',')
            for program in programs:
                programs_list.append(program)
            return basedir,programs_list

    def clear_camera_comboBoxes(self):
        self.ui.comboBox.clear()
        self.ui.reg_camera_combo.clear()
        self.open_exit_camera.set_combo_items('')
        self.open_surveillance_camera_one.set_combo_items('')
        self.surveillance_camera_three.set_combo_items('')
        self.surveillance_camera_two.set_combo_items('')
        self.surveillance_camera_four.set_combo_items('')
        self.ui.camera_three_comboBox.clear()
        self.ui.camera_two_comboBox.clear()
        self.ui.camera_one_comboBox.clear()
        self.ui.camera_four_comboBox.clear()
        

    def get_active_cameras(self,camera:list):
        self.ui.comboBox.addItems(camera)
        self.ui.reg_camera_combo.addItems(camera)
        self.open_exit_camera.set_combo_items(camera)
        count = [self.ui.comboBox.itemText(i) for i in range(self.ui.comboBox.count())]
        self.ui.scan_range_label.setText("Active camera(s): "+str(len(count)))
        self.ui.label_notification.setText("Done scanning for available cameras...")           

    def camera_thread(self):
        scan_range = self.ui.scan_range.text()
        if scan_range:
            self.clear_camera_comboBoxes()
            self.ui.scan_range_label.setText('')
            self.active = ActiveCameras(scan_range)
            self.active.start()
            self.active.cameras.connect(self.get_active_cameras)
            self.ui.label_notification.setText("Scanning for available cameras...")
        else:
            self.alert_builder("Oops! no scan range provided...")
    
    def backup_history(self):
        path =Path('C:\\ProgramData\\iAttend\\data\\backup\\backup_history.txt')
        path.touch(exist_ok=True)
        file = open(path)
        time =datetime.now().time().strftime('%I:%M:%S %p')
        date=datetime.now().date().strftime('%a %b %d %Y')
        if os.path.exists(path):
            with open(path,'a+') as file:
                file.writelines(f'\n{date},{time}')
            file.close()         

    def backup_database(self):
        path='C:\\ProgramData\\iAttend\\data\\backup'
        db_path = 'C:\\ProgramData\\iAttend\\data\\database\\attendance_system.db'
        if os.path.exists(path):
            shutil.copy2(db_path,path)
            self.backup_history()
            self.alert = AlertDialog()
            self.alert.content("Database successfully backed up...")
            self.alert.show()

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
   
    def save_report(self):
        filename = self.ui.file_name.text()
        date=datetime.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        transformed_name=filename+date
        if self.ui.bar_chart.isChecked():    
            if self.ui.file_name.text():
                self.barchart.save_chart(transformed_name)
                self.alert = AlertDialog()
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert = AlertDialog()
                self.alert.content("Oops! please provide file name")
                self.alert.show()         
        elif self.ui.line_graph.isChecked():
            if self.ui.file_name.text():
                self.line_graph.save_chart(transformed_name)
                self.alert = AlertDialog()
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert = AlertDialog()
                self.alert.content("Oops! please provide file name")
                self.alert.show() 
        elif self.ui.pie_chart.isChecked():
            if self.ui.file_name.text():
                self.piechart.save_chart(transformed_name)
                self.alert = AlertDialog()
                self.alert.content("Document saved successfully")
                self.alert.show()
            else:
                self.alert = AlertDialog()
                self.alert.content("Oops! please provide file name")
                self.alert.show() 
     
    def reconstruct_date(self,date:str):
        date_value=str(date).split('-')
        date_transformed = datetime.date(int(date_value[0]),int(date_value[1]),int(date_value[2])).strftime("%a %d %b, %Y")
        return date_transformed

    def create_program_data_dir(self):
        root_dir = 'C:\\ProgramData\\iAttend\\data'
        list =('batch_logs','programs','properties','qr_code',
        'barchart','piechart','linechart','json_export','csv_export',
        'backup','email_details','json_file','samples','settings',
        'footage','reports','exports')

        if not os.path.exists(root_dir):
            os.makedirs(root_dir)
        for item in list:
            path = os.path.join(root_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)
        self.create_files()

        report_dir = 'C:\\ProgramData\\iAttend\\data\\reports'
        report = ('piechart','barchart','linegraph','visualize')    
        for item in report:
            path = os.path.join(report_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)

        fortage_dir = 'C:\\ProgramData\\iAttend\\data\\footage'
        footage = ('camera_1','camera_2','camera_3','camera_4','settings')
        for item in footage:
            path = os.path.join(fortage_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)
        
        export_dir = 'C:\\ProgramData\\iAttend\\data\\exports'
        export = ('csv','json')
        for item in export:
            path = os.path.join(export_dir,item)
            if not os.path.exists(path):
                os.mkdir(path)

    def create_files(self):
        path =Path('C:\\ProgramData\\iAttend\\data\\properties\\properties.txt')
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                if os.path.getsize(path)==0:
                    file.write("Username,Password,Hostname,Port,Database")
            file.close() 

        path =Path('C:\\ProgramData\\iAttend\\data\\programs\\CoS_programs.txt')
        path.touch(exist_ok=True)
        file = open(path)
        if os.path.exists(path):
            with open(path,'a+') as file:
                if os.path.getsize(path)==0:
                    file.write('BSc. Physics,BSc. Statistics,BSc. Chemistry,'
                    +'BSc. Mathematics,Doctor of Optometry,BSc. Biochemistry,'
                    +'BSc. Computer Science,BSc. Actuarial Science,BSc. Biological Science,'
                    +'BSc. Environmental Science,BSc. Food Science and Technology,'
                    +'BSc. Meterology and Climate Science')
            file.close() 

        details_path =Path('C:\\ProgramData\\iAttend\\data\\email_details\\detail.txt')
        details_path.touch(exist_ok=True)
        d_file = open(details_path)
        if os.path.exists(details_path):
            with open(details_path,'a+') as d_file:
                if os.path.getsize(details_path)==0:
                    d_file.write("Subject,example@gmail.mail, Sender,Password")
            d_file.close() 

        content = """
        Hello name,
                Please attached to this message is your
            attendance code. Please keep it safe as you 
            will need this everytime you would want to 
            access the facility. 
                Attend Today, Acheive Tomorrow!
                                            Thank you! """
        content_path =Path('C:\\ProgramData\\iAttend\\data\\email_details\\content.txt')
        content_path.touch(exist_ok=True)
        content_file = open(content_path)
        if os.path.exists(content_path):
            with open(content_path,'a+') as content_file:
                if os.path.getsize(content_path)==0:
                    content_file.write(content)
            content_file.close() 

        report_content = """
        Hello name,
    	        Please attached to this message is the
            report or data you requested for. Feel free 
            to contact us for our services at anytime.
                                        Thank you! """
        content_path =Path('C:\\ProgramData\\iAttend\\data\\email_details\\content_report.txt')
        content_path.touch(exist_ok=True)
        content_file = open(content_path)
        if os.path.exists(content_path):
            with open(content_path,'a+') as content_file:
                if  os.path.getsize(content_path)==0:
                    content_file.write(report_content)
            content_file.close()        
    

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
        path = 'C:\\ProgramData\\iAttend\\data\\reports\\visualize\\'
        if self.ui.bar_chart.isChecked():
            if not self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_data_barchart()
                if len(data[0])>=1:
                    self.barchart.bar_plot_single_view(data[0], data[1],width,"Statictics","Number of students","Programs",
                    colors[:len(data[0])])
                    self.ui.plot_area_2.setPixmap(QPixmap.fromImage(path+'barchart.png'))
                    self.ui.plot_area_2.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()
            elif self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_data_by_date()
                if len(data[0])>=1:
                    self.barchart.bar_plot_single_view(data[0], data[1],width,"Statictics ","Number of students",
                    self.get_report_start_date(),colors[:len(data[0])])
                    self.ui.plot_area_2.setPixmap(QPixmap.fromImage(path+'barchart.png'))
                    self.ui.plot_area_2.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()
            elif self.ui.report_end_date.text() and self.ui.report_end_date.text():
                data = self.get_data_by_date_range()
                if len(data[0])>=1:      
                    self.barchart.bar_plot_single_view(data[0], data[1],width,"Statictics","Number of students",
                    self.get_report_start_date()+" <> "+self.get_report_end_date(),colors[:len(data[0])])
                    self.ui.plot_area_2.setPixmap(QPixmap.fromImage(path+'barchart.png'))
                    self.ui.plot_area_2.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()   
        elif self.ui.line_graph.isChecked():
            program=self.ui.college_courses.currentText()
            if self.ui.date_range_comboBox.currentText():
                y_values =self.line_plot_values()
                if len(y_values)>=1:
                    self.line_graph.plot_graph(y_values,title="Trend in attendance for "+program,label_="Trends",
                    y_label="Number of students",x_label="Date")
                    self.ui.plot_area_2.setPixmap(QPixmap.fromImage(path+'linegraph.png'))
                    self.ui.plot_area_2.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()
            elif not self.ui.date_range_comboBox.currentText():
                y_values=self.count_attendance_for_all_distinct_dates()
                if len(y_values[0])>=1:
                    self.line_graph.plot_graph(y_values[0],title="Trend in attendance for "+program,label_="Trends",
                    y_label="Number of students",x_label=self.reconstruct_date(y_values[1])+'<>'+self.reconstruct_date(y_values[2]))
                    self.ui.plot_area_2.setPixmap(QPixmap.fromImage(path+'line_plot.png'))
                    self.ui.plot_area_2.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()
        elif self.ui.pie_chart.isChecked():
            if self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_data_by_date()
                if len(data[0])>=1:
                    self.piechart.piechart(data,self.get_report_start_date())
                    self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'piechart.png'))
                    self.ui.plot_area.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show()
            elif self.ui.report_end_date.text() and self.ui.report_end_date.text():
                data = self.get_data_by_date_range()
                if len(data[0])>=1:      
                    self.piechart.piechart(data,self.get_report_start_date()+" <> "+self.get_report_end_date())
                    self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'piechart.png'))
                    self.ui.plot_area.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show() 
            elif not self.ui.report_start_date.text() and not self.ui.report_end_date.text():
                data = self.get_pichart_data()
                if len(data[0])>=1:
                    self.piechart.piechart(data,"Percentages of programs")
                    self.ui.plot_area.setPixmap(QPixmap.fromImage(path+'piechart.png'))
                    self.ui.plot_area.setScaledContents(True)
                else:
                    self.alert = AlertDialog()
                    self.alert.content("Oops! your data is not enough to\ngenerate charts..")
                    self.alert.show() 


    def export_data_to_csv(self):
        table=self.ui.tableWidget.item(0,0)
        date=datetime.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iAttend\\data\\exports\\csv\\students_data'+date+'.csv'
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
        date=datetime.now().strftime('_%d_%B_%Y-%I_%M_%S_%p')
        path = 'C:\\ProgramData\\iAttend\\data\\exports\\json\\students_data'+date+'.json'
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
        self.ui.tableWidget.setColumnWidth(1,230)
        self.ui.tableWidget.setRowCount(len(details))
        self.ui.tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for data in details:
            self.ui.tableWidget.setItem(row_count,1,QTableWidgetItem(str(data[1])))
            self.ui.tableWidget.setItem(row_count,2,QTableWidgetItem(str(data[2])))
            self.ui.tableWidget.setItem(row_count,3,QTableWidgetItem(str(data[3])))
            self.ui.tableWidget.setItem(row_count,4,QTableWidgetItem(str(data[4])))
            self.ui.tableWidget.setItem(row_count,5,QTableWidgetItem(str(data[5])))
            self.ui.tableWidget.setItem(row_count,0,QTableWidgetItem(str(data[6])))
            row_count = row_count+1

    def fetch_details_for_card_view(self):
        try:
            results=self.query_database("SELECT * FROM tb_attendance WHERE st_reference="+str(self.ui.search_box.text()))
            self.ui_table(results)
            if self.ui.search_box.text():
                db_data=self.fetch_data_from_db(self.ui.search_box.text())
                if len(db_data) > 0:
                    start_date = (str(db_data[8])).split(' ')
                    student_year=(int(datetime.now().date().strftime('%Y'))-int(start_date[1]))    
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
                    self.ui.db_college.setText(db_data[5])
                    self.ui.db_nationality.setText(db_data[7])
                    self.ui.db_programe.setText(db_data[6])
                    self.ui.db_year.setText(level)
                    self.ui.db_validity.setText(db_data[8]+" - "+db_data[9])
                    self.load_image_from_db(self.ui.search_box.text(),self.ui.db_image_data)
                else:
                    self.alert_builder("Student details not found. Please enter\nyour details to register!")
            else:
                self.alert_builder("Oops! search field can't be empty.")
        except:
            self.alert = AlertDialog()
            self.alert.content("Oops! invalid search parameter...")
            self.alert.show()

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
        results = self.query_database("SELECT * FROM tb_attendance WHERE program="+program+" and date_stamp="+start_date)
        self.ui_table(results)
        return results

    def query_database_for_data(self):
        if self.ui.checkBox.isChecked():
            if self.ui.search_box.text() and self.ui.db_start_date.text() and  self.ui.db_end_date.text():
                start = self.ui.db_start_date.text()
                start_date="\'{}\'".format(start)
                end = self.ui.db_end_date.text()
                end_date="\'{}\'".format(end)
                prog = self.ui.search_box.text()
                program="\'{}\'".format(prog)
                results_ = self.query_database("SELECT * FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" and "+end_date+" and program="+program)
                self.ui_table(results_)
                return results_
            elif self.ui.search_box.text() and self.ui.db_start_date.text():
                self.fetch_data_by_program_and_date()
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
        else:
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
        self.ui.email_from.setText(details[2])
        self.ui.email_sender.setText(details[1])
        self.ui.email_subject.setText(details[0])
        self.ui.sender_password.setText(details[3])
    
    def get_details(self):
        path = 'C:\\ProgramData\\iAttend\\data\\email_details\\detail.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read().split(',')
            return details
    
    def get_mail_content(self):
        path = 'C:\\ProgramData\\iAttend\\data\\email_details\\content.txt'
        if os.path.exists(path):
            with open(path,'r') as f:
                details = f.read()
            return details.replace('name',self.ui.reg_firstname.text())

    def convert_to_json(self, code:Code):
        to_json = json.dumps(code)
        return to_json

    def generate_code(self):
        code = Code(
            index=self.ui.reg_index.text(),
            reference=self.ui.reg_student_ref.text(),
            email_address=self.ui.reg_email.text()
        )
        if code.reference !='':
            code ={
            "index":code.index,
            "reference":code.reference,
            "email_address":code.email_address}
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
        if self.connected_to_internet()==True and self.ui.reg_email.text():
            try:
                self.prepare_email()
                self.alert = AlertDialog()
                self.alert.content("Hey! mail sent successfully...")
                self.alert.show()
            except Exception as e:
                self.alert = AlertDialog()
                self.alert.content(str(e))
                self.alert.show()
        else:
                self.alert = AlertDialog()
                self.alert.content("Oops! something went wrong mail\nnot sent...")
                self.alert.show()

    def send_mail(self):
        self.prepare_email_to_send()
        
        
    def fetch_data_from_db(self,reference):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        detail =my_cursor.execute("SELECT * FROM tb_students WHERE reference="+reference)
        detail= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
        return db_data

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
            details=self.fetch_data_from_db(self.ui.reg_student_ref.text())
            root_path = 'C:\\ProgramData\\iAttend\\data\\images\\'
            if not details:
                if check_state == True:
                    if self.ui.image_file_reg.text() and self.ui.file_system.isChecked():
                        with open(self.ui.image_file_reg.text(), 'rb') as image:
                            data = image.read()
                            my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(?,?)",(student.reference,data))
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (?,?,?,?,?,?,?,?,?)",
                        (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))   
                        db.commit()
                        my_cursor.close() 
                        self.alert_builder("Student registered successfully")   
                    elif self.ui.online_image.isChecked() and self.ui.image_file_reg.text():
                        path = path = root_path+'image.jpg'
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
                    elif self.ui.image_less.isChecked():
                        path = root_path+'img.jpg'
                        with open(path, 'rb') as image:
                            data = image.read()
                            my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(?,?)",(student.reference,data))
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (?,?,?,?,?,?,?,?,?)",
                        (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))   
                        db.commit()
                        my_cursor.close() 
                        self.alert_builder("Student registered successfully")   
                else:
                    if self.ui.image_file_reg.text() and self.ui.file_system.isChecked():
                        with open(self.ui.image_file_reg.text(), 'rb') as image:
                            data = image.read()
                            my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(%s,%s)",(student.reference,data))
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))   
                        db.commit()
                        my_cursor.close() 
                        self.alert_builder("Student registered successfully")    
                    elif self.ui.online_image.isChecked() and self.ui.image_file_reg.text():
                        path = root_path+'image.jpg'
                        if os.path.exists(path):
                            with open(path, 'rb') as image:
                                data = image.read()       
                                my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(%s,%s)",(student.reference,data))
                            my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))
                            db.commit()
                            my_cursor.close()
                            os.remove(path)
                            self.alert_builder("Student registered successfully")    
                        else:
                            self.alert_builder("Oops! something went wrong while\nprocessing your request") 
                    elif self.ui.image_less.isChecked():
                        path = root_path+'img.jpg'
                        with open(path, 'rb') as image:
                            data = image.read()       
                            my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(%s,%s)",(student.reference,data))
                        my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))
                        db.commit()
                        my_cursor.close()
                        os.remove(path)
                        self.alert_builder("Student registered successfully")    
            else:
                self.alert_builder("Oops! student with this reference\nalready exists")
        else:
            self.alert_builder("Oops! something went wrong while\nprocessing your request")

    def alert_builder(self, message:str):
        self.alert = AlertDialog()
        self.alert.content(message)
        self.alert.show()
          

    def load_image_from_db(self,reference,label):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        cursor=my_cursor.execute("SELECT st_reference,image from tb_images WHERE st_reference="+reference)
        cursor= my_cursor.fetchone()
        db.commit()
        my_cursor.close()
        image_data = []
        root_path = 'C:\\ProgramData\\iAttend\\data\\images\\'
        path = root_path +'db_image.jpg'
        if cursor:
            for data in cursor:
                image_data.append(data)
            if len(image_data)>0:
                with open(path,'wb') as image_file:
                        image_file.write(image_data[1])
            label.setPixmap(QPixmap.fromImage(path))
            label.setScaledContents(True)
        else:
            label.setPixmap(QPixmap.fromImage(root_path+'image.jpg'))
            label.setScaledContents(True)

    def search_thread(self):
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
        
    def search_student(self):
        self.search_thread()
        

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
                    my_cursor.close()
                else:
                    my_cursor.execute("UPDATE tb_images SET image =%s WHERE st_reference=%s",(data,ref))
                    db.commit()
                    my_cursor.close()
            self.alert_builder("Hey! Student image updated successfully.")
        elif self.ui.reg_student_ref.text() and self.ui.image_file_reg.text() and self.ui.online_image.isChecked():
            ref = self.ui.reg_student_ref.text()
            path = 'C:\\ProgramData\\iAttend\\data\\images\\image.jpeg'
            if os.path.exists(path):
                with open(path, 'rb') as image:
                    data = image.read()
                    if check_state == True:
                        my_cursor.execute("UPDATE tb_images SET image =? WHERE st_reference=?",(data,ref))
                        db.commit()
                        my_cursor.close()
                    else:
                        my_cursor.execute("UPDATE tb_images SET image =%s WHERE st_reference=%s",(data,ref))
                        db.commit()
                        my_cursor.close()
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
            my_cursor.close()
            self.resets_fileds()
            self.alert_builder("Student data removed successfuly!")
        except:
            self.alert_builder("Oops! internal server error!")

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
            link = requests.get(self.ui.image_file_reg.text())
            if self.connected_to_internet()==True:
                try:
                    path = 'C:\\ProgramData\\iAttend\\data\\images\\db_images.jpg'
                    wget.download(link.url,path)
                    self.ui.reg_image.setPixmap(QPixmap.fromImage(path))
                    self.ui.reg_image.setScaledContents(True)
                except Exception as e:
                    self.alert_builder("Oops! check your image url!")
            elif self.connected_to_internet()==False:
                 self.alert_builder("Oops! check you internet connection!")         

    def loadUi_file(self):
        self.ui.firstname.setText("Firstname")
        self.ui.middlename.setText("Middlename")
        self.ui.lastname.setText("Lastname")
        self.ui.refrence.setText("Reference")
        self.ui.index.setText("Index")
        self.ui.coledge.setText("College")
        self.ui.nationality.setText("Nationality")
        self.ui.validity.setText("Validity")
        self.ui.program.setText("Program")
        self.ui.year.setText("Year")
        self.ui.last_in.setText("Duration")
        self.ui.last_out.setText("Last seen")
        self.ui.image.setPixmap(QPixmap(u":/icons/asset/image.svg"))
        self.ui.label_notification.setText("Notification")


    def last_seen(self,reference:str):  
        (db,my_cursor,connection_status) = self.database.my_cursor()
        cursor=my_cursor.execute("SELECT date_stamp,time_out,duration FROM tb_attendance WHERE st_reference = "+(reference)+" ORDER BY date_stamp DESC LIMIT 2")
        cursor= my_cursor.fetchall()
        db.commit()
        my_cursor.close()
        last_seen_info = []
        if cursor:
            for data in cursor:
                last_seen_info.append(data)
        if len(last_seen_info)>=2:
            details=str(last_seen_info[1][0]).split('-')
            details = datetime.date(int(details[0]),int(details[1]),int(details[2])).strftime("%a %d %b, %Y")
            time = last_seen_info[1][1]
            duration = last_seen_info[1][2]
            self.ui.last_out.setText(details+' @ '+time)
            self.ui.last_in.setText(duration)           
        else:
            self.ui.last_out.setText("Oops! first timer")
            self.ui.last_in.setText("00:00:00") 

    def retreive_student_details(self,data):
        data_json = json.loads(data)
        if isinstance(data, str):
                self.last_seen(data_json['reference'])
                db_data=self.fetch_data_from_db(data_json['reference'])
                if len(db_data) > 0:
                    start_date = (str(db_data[8])).split(' ')
                    end_date=str(db_data[9]).split(' ')
                    student_year=(int(datetime.now().date().strftime('%Y'))-int(start_date[1]))
                    start_month = strptime(start_date[0],'%b')
                    start_month=start_month.tm_mon
                    end_month = strptime(end_date[1],'%b')
                    end_month=end_month.tm_mon
                    issued_date_transformed = datetime.date(int(start_date[1]),start_month,int(2)).strftime("%b %Y")
                    expiry_date_transformed = datetime.date(int(end_date[2]),end_month,int(2)).strftime("%b %Y")
                    validity = issued_date_transformed+' - '+expiry_date_transformed
                      
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
                    self.ui.firstname.setText(helper[0])
                    self.ui.middlename.setText(helper[1])
                    self.ui.lastname.setText(db_data[4])
                    self.ui.refrence.setText(str(db_data[1]))
                    self.ui.index.setText(str(db_data[2]))
                    self.ui.coledge.setText(db_data[5])
                    self.ui.nationality.setText(db_data[7])
                    self.ui.validity.setText(validity)
                    self.ui.year.setText(level)
                    self.ui.program.setText(db_data[6])
                    self.load_image_from_db(data_json['reference'],self.ui.image)
                else:
                    self.loadUi_file()
                    self.show_info("Oops! student not found. Please register!")                

    def mark_attendance_db(self):
        (db,my_cursor,connection_status) = self.database.my_cursor()
        attendance = Attendance(
            self.ui.refrence.text(),
            self.ui.program.text(),
            str(datetime.now().date().strftime("%Y-%m-%d")),
            str(datetime.now().time().strftime("%H:%M:%S")),
            str(datetime.now().time().strftime("%H:%M:%S")),
            "00:00:00"
        )
        check_state = self.database.check_state()
        details = []
        date="\'{}\'".format(datetime.now().date().strftime("%Y-%m-%d"))
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
        db.close()

    def retrive_registration_from_qrcode(self,qr_code_data):
        json_data = json.loads(qr_code_data)
        self.ui.reg_firstname.setText(json_data['firstname'])
        self.ui.reg_middlename.setText(json_data['middle_name'])
        self.ui.reg_lastname.setText(json_data['lastname'])
        self.ui.reg_student_ref.setText(json_data['reference'])
        self.ui.reg_index.setText(json_data['index'])
        self.ui.reg_college.setText(json_data['college'])
        self.ui.reg_nationality.setText(json_data['nationality'])
        self.ui.reg_start_date.setText(json_data['issued_date'])
        self.ui.reg_end_date.setText(json_data['expiry_date'])
        self.ui.reg_programs.setCurrentText(json_data['program'])
        self.ui.reg_college_2.setCurrentText(json_data['college'])
        self.ui.image_file_reg.setText(json_data['image_url'])
             
    def start_webcam_registration(self):
        if self.ui.camera_ip.text() or self.ui.comboBox.currentText():
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
                    self.capture = VideoCapture(camera_id) 

            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            self.saveTimer.timeout.connect(self.update_frame_registration)
            self.saveTimer.start(3)
        else:
            self.show_alert = AlertDialog()
            self.show_alert.content("Oops! your have no active cameras available")  
            self.show_alert.show()
        

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
        self.now = datetime.now()
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
            self.retrive_registration_from_qrcode(qr_code_data)
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
        if self.saveTimer.isActive():
            self.show_alert.content("Hey! wait a second while system\nrelease camera") 
            self.show_alert.show()
            self.ui.reg_cap_frame.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui.reg_cap_frame.setScaledContents(False)
            self.saveTimer.stop() 
        else:
            self.show_alert.content("Oops! you have no active camera\nto disconnect from.") 
            self.show_alert.show()

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
        if self.ui.camera_ip.text() or self.ui.comboBox.currentText():
            ip_address = self.ui.camera_ip.text()
            system_attached_camera = self.ui.comboBox.currentText()
            self.network_capture = VideoCapture(ip_address)
            if ip_address:  
                if self.network_capture is None or not self.network_capture.isOpened():    
                    self.stop_webcam
                    self.show_alert = AlertDialog()
                    self.show_alert.content("Oops! check the camera ip address\nconnetion or is already in use.") 
                    self.show_alert.show()
                else:
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(ip_address)    
            elif system_attached_camera:
                camera_id = int(system_attached_camera)
                self.system_capture = VideoCapture(camera_id)       
                if self.system_capture is None or not self.system_capture.isOpened():    
                    self.stop_webcam
                    self.show_alert = AlertDialog()
                    self.show_alert.content("Oops! check the camera for\nconnetion or is already in use.")  
                    self.show_alert.show()
                else:
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(camera_id)                  
            elif self.system_capture.isOpened() and self.network_capture.isOpened():
                    self.show_info("Hey! wait a second while system\ninitializes camera")
                    self.capture = VideoCapture(camera_id)
            # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            # self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            self.timer.timeout.connect(self.update_frame)  
            self.timer.start(3)
        else:
            self.show_alert = AlertDialog()
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

        self.text = str(time.strftime("%I:%M:%S %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-110,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255),font=cv2.FONT_HERSHEY_SIMPLEX)
        self.now = datetime.now()
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
        if self.timer.isActive():
            self.show_alert.content("Hey! wait a second while system\nrelease camera") 
            self.show_alert.show()
            self.ui.camera_view.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui.camera_view.setScaledContents(False)
            self.timer.stop() 
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