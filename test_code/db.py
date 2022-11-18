
import mysql.connector as connector

from dataclasses import dataclass
# import psycopg2
from datetime import datetime as dt

# from dataclasses import dataclass


db = connector.connect(
        port=3306,
        host="localhost",
        user = "root",
        password = '0552588647',
        database = "students"
        )

my_cursor =db.cursor()

# def reconstruct_date(date:str):
#         list_months = ['January', 'Febuary', 'March',
#                 'April', 'May', 'June', 'July',
#                 'August', 'September', 'October',
#                 'November', 'December']
#         date_value=str(date).split('-')
#         year = date_value[0]
#         day = date_value[2]
#         month = date_value[1]
#         month=list_months[int(month)-1]
#         return str(day+' '+month+' '+year)
        

# def last_seen(reference:str):  
#         cursor=my_cursor.execute("SELECT date_stamp,time_out,duration FROM tb_attendance WHERE st_reference = "+(reference)+" ORDER BY date_stamp DESC LIMIT 2")
#         cursor= my_cursor.fetchall()
#         last_seen_info = []
#         print(cursor)
#         if cursor:
#             for data in cursor:
#                 last_seen_info.append(data)
#             db.commit()
#         if last_seen_info:
#             print(last_seen_info[0])
#             details=reconstruct_date(last_seen_info[1][0])
#             time = last_seen_info[0][1]
#             duration = last_seen_info[0][2]
#             print(details+' @ '+time)
#             print(duration)           
#         else:
#             print("Oops! first timer")
#             print("00:00:00") 


# v = last_seen('20661163')
# print(v)
def query_database(query: str):
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        if cursor:
            for item in cursor:
                details.append(item)
            db.commit()
        return details

# def get_pichart_data():
#         query = query_database("SELECT DISTINCT program FROM tb_attendance")
#         result_set= []
#         for item in query: 
#             result_set.append(item[0])
#         print(query)
#         total:list = []
#         for item in result_set:
#             program = "\'{}\'".format(item)
#             sub_count = query_database("SELECT COUNT(*) FROM tb_attendance WHERE program="+program)
#             total.append(sub_count[0][0])
#         data = query_database("SELECT DISTINCT program FROM tb_attendance")
#         result= []
#         for item in data:
#             item = str(item[0]).split(' ')
#             result.append(item[1]) 
#         return total, result


# d = get_pichart_data()
# print(d)

# sql = """
    
# """

# my_cursor.execute("Select * from my_table")

# def method_connect(driver,port,user,password,host,database):
#         try:
#                 db = driver.connect(
#                 port=port,
#                 host=host,
#                 user = user,
#                 password = password,
#                 database = database
#                 )
#                 print ("Connecting to database")
#         except Exception as e:
#                 print(str(e))
# method_connect(driver=psycopg2,port=5432,host='localhost',user='postgres',password='0552588647',database='attendance_system')
# method_connect(driver=connector,port=3306,host='localhost',user='root',password='0552588647',database='students')

# data = pd.read_sql("SELECT * FROM tb_attendance",db)
# dataframe = pd.DataFrame(data)
# dataframe.to_csv(r'test_code\\data.csv',sep=',')
# db.commit()
# db.close()

# path = r'backend\\images\\face_images\\'
# cursor=my_cursor.execute("SELECT st_reference,image  from tb_images ")
# cursor= my_cursor.fetchall()
# image_data = []
# if cursor:
#     for data in cursor:
#         image_data.append(data)
#         with open(path+str(data[0])+'.jpeg','wb') as f:
#             f.write(data[1])
#     db.commit()

# print(len(image_data))

# for data in len(image_data):
#     with open(r'backend\\images\\face_images\\'+data+'.jpeg','wb') as f:
#         f.write(data)

# def load_face_images_from_db():
#     cursor=my_cursor.execute("SELECT st_reference,image  from tb_images ")
#     cursor= my_cursor.fetchall()
#     image_data = []
#     if cursor:
#         for data in cursor:
#             image_data.append(data)
#             with open(r'backend\\images\\face_images\\'+str(data[0])+'.jpeg','wb') as f:
#                 f.write(data[1])
#         db.commit()

# try:
#     with open("C:\\Users\\BTC OMEN\\Pictures\\20661163.jpeg", 'rb') as image:
#         data = image.read()
#         my_cursor.execute("insert into tb_images(st_reference,image) values(%s,%s)",(20661163,data))
#     db.commit()
# except:
#     print("Failed to load face images")



# data=my_cursor.execute("SELECT st_reference,date FROM tb_attendance WHERE st_reference=%s and date=%s ",(20661163,'22-10-2022'))
# data=my_cursor.fetchone()
# details = []
# if data:
#     for x in data:
#         details.append(x)
#     db.commit()
# print(len(details))

# def last_seen(reference:str):
#     list_months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',
#                      'August', 'September', 'October', 'November', 'December']
#     cursor=my_cursor.execute("SELECT date_stamp,time_out,duration FROM tb_attendance WHERE st_reference = "+(reference)+" ORDER BY date_stamp DESC LIMIT 2")
#     cursor= my_cursor.fetchall()
#     last_seen_info = []
#     if cursor:
#         for data in cursor:
#             last_seen_info.append(data)
#     db.commit()
#     print(last_seen_info)
#     print(last_seen_info[1][0])
#     if last_seen_info:
#         details=str(last_seen_info[1][0]).split('-')
#         year = details[0]
#         month = details[1]
#         day = details[2]
#         time = last_seen_info[0][1]
#         duration = last_seen_info[0][2]
#         construct_last_seen = str(list_months[int(month)]+' '+day+' '+year+' @ '+time)
#         print(details)
#     else:
#         return "No last seen available!"
# d=last_seen('20661163')

# #########################################################################
# def log_student_out(reference:str):
#     cursor=my_cursor.execute("SELECT time_in,time_out,duration FROM tb_attendance WHERE st_reference= %s and date_stamp= %s ",(reference,dt.now().date().strftime('%Y-%m-%d')))
#     cursor= my_cursor.fetchone()
#     details = []
#     if cursor:
#         for data in cursor:
#             details.append(data)
#     db.commit()
#     if details:
#         time_out =dt.now().time().strftime('%H:%M:%S')
#         time_out_split = str(time_out).split(':')
#         time_in = str(details[0]).split(':')
#         duration = (abs((int(time_out_split[0])-int(time_in[0]))),
#         abs((int(time_out_split[1])-int(time_in[1]))),
#         abs((int(time_out_split[2])-int(time_in[2]))))
#         new_duration = str(str(duration[0])+':'+str(duration[1])+':'+str(duration[2]))
#         print(details[2])
#         if str(details[2]) == "00:00:00":
#             cursor=my_cursor.execute("UPDATE tb_attendance SET time_out=%s, duration=%s  WHERE st_reference=%s and date_stamp=%s ",(time_out,new_duration,reference,dt.now().date().strftime('%Y-%m-%d')))
#             db.commit()
#             print(new_duration)
#             return "Hey! have successfully logged out"
#         else:
#             return "Oops! you are already logged out!"
#     else:
#         return "Oops! student details not found."
# m=log_student_out('20661163')
# print(m)

# import seaborn as sns
# def load_data_from_db_search_page():
   
#     cursor = my_cursor.execute("SELECT * FROM tb_attendance")
#     cursor = my_cursor.fetchall()
#     details = []
#     if cursor:
#         for item in cursor:
#             details.append(item)
#         db.commit()
#         cm=sns.light_palette('green',as_cmap=True)
#     data = pd.DataFrame(details,columns=['Id','Program','Date_stamp','Time_in','Time_out','Duration','Reference'])
#     data.style.background_gradient(cmap=cm)
#     data.to_csv(r'test_code\\data.xlsx',sep=',',index=False,ader=['Id','Program','Date_stamp','Time_in','Time_out','Duration','Reference'])
#     data.to_json(r'test_code\\results.json',orient='records',indent=4)

  
# load_data_from_db_search_page()

# import numpy as np
# import math


# ref=math.floor(np.random.random(1)*10000000)
# time=dt.now().time().strftime('%H:%M:%S %p')
# date=dt.now().date().strftime('%Y-%m-%d')
# duration= "00:00:00"
# data = ['BSc. Physics','BSc. Statistics','BSc. Chemistry','BSc. Mathematics','Doctor of Optometry','BSc. Biochemistry','BSc. Computer Science',
#         'BSc. Actuarial Science','BSc. Biological Science','BSc. Environmental Science','BSc. Food Science and Technology','BSc. Meterology and Climate Science']
# @dataclass
# class Attendance():
#     st_reference:str
#     program:str
#     date:str
#     time_in:str
#     time_out:str
#     duration:str

# for i in range(12):
#     ref=math.floor(np.random.random(1)*1000000)
#     attendance = Attendance(
#             ref,
#             data[i%6],
#             str(dt.now().date().strftime("%Y-%m-%d")),
#             str(dt.now().time().strftime("%H:%M:%S")),
#             str(dt.now().time().strftime("%H:%M:%S")),
#             duration
#         )      
#     try:
#         my_cursor.execute("INSERT INTO tb_attendance(st_reference,program,date_stamp,time_in,time_out,duration) VALUES(%s,%s,%s,%s,%s,%s)",
#                 (attendance.st_reference,attendance.program,attendance.date,
#                 attendance.time_in,attendance.time_out,attendance.duration))
#         db.commit()
#         print("Done inserting")
#     except:
#         print("Not inserted")

# # def fetch_details(reference:str):
# #     cursor=my_cursor.execute("SELECT time_in,time_out,duration FROM tb_attendance WHERE st_reference= %s and date_stamp= %s ",(reference,dt.now().date().strftime('%Y-%m-%d')))
# #     cursor= my_cursor.fetchone()
# #     details = []
# #     if cursor:
# #         for data in cursor:
# #             details.append(data)
# #     db.commit()
# #     return details
# # m = fetch_details('20661163')
# # print(m)

# # def log_out():
# #     if len(m) > 1:
# #         time_out =dt.now().time().strftime('%H:%M:%S')
# #         time_out_split = str(time_out).split(':')
# #         time_in = str(m[0]).split(':')
# #         duration = (abs((int(time_out_split[0])-int(time_in[0]))),
# #         abs((int(time_out_split[1])-int(time_in[1]))),
# #         abs((int(time_out_split[2])-int(time_in[2]))))
# #         new_duration = str(str(duration[0])+':'+str(duration[1])+':'+str(duration[2]))
# #         print(m[2])
# #         if str(m[2]) == "00:00:00":
# #             cursor=my_cursor.execute("UPDATE tb_attendance SET time_out=%s, duration=%s  WHERE st_reference=%s and date_stamp=%s ",(time_out,new_duration,reference,dt.now().date().strftime('%Y-%m-%d')))
# #             my_cursor.fetchone()
# #             db.commit()
# #             print(new_duration)
# #             return "Hey! have successfully logged out"
# #         else:
# #             return "Oops! you are already logged out!"
# #     else:
# #         return "Oops! student details not found."

# # def fetch_details(reference:str):
# #         cursor=my_cursor.execute("SELECT id,reference FROM tb_students WHERE reference= " +reference)
# #         cursor= my_cursor.fetchone()
# #         db.commit()
# #         details = []
# #         if cursor:
# #             for data in cursor:
# #                 details.append(data)
# #             return details

# # m = fetch_details('20661163')
# # print(m[1])

# def log_student_out(reference:str):
#         cursor=my_cursor.execute("SELECT id,reference FROM tb_students WHERE reference= " +reference)
#         cursor= my_cursor.fetchone()
#         db.commit()
#         results = []
#         if cursor:
#             for data in cursor:
#                 results.append(data)
#             cursor=my_cursor.execute("SELECT time_in,duration FROM tb_attendance WHERE st_reference=%s and date_stamp=%s ",(str(results[1]),dt.now().date().strftime("%Y-%m-%d")))
#             cursor=my_cursor.fetchall()
#             db.commit()
#             details = []
#             if cursor:
#                 for data in cursor:
#                     details.append(data)
#                 db.commit()
#                 time_out =dt.now().time().strftime('%H:%M:%S')
#                 time_out_split = str(time_out).split(':')
#                 time_in = str(details[0][0]).split(':')
#                 construct_duration = (abs((int(time_out_split[0])-int(time_in[0]))),
#                 abs((int(time_out_split[1])-int(time_in[1]))),
#                 abs((int(time_out_split[2])-int(time_in[2]))))
#                 new_duration = str(str(construct_duration[0])+':'+str(construct_duration[1])+':'+str(construct_duration[2]))
#                 print(details)
#                 print(time_in)
#                 if str(details[0][1]) == "00:00:00":
#                     my_cursor.execute("UPDATE tb_attendance SET time_out= %s, duration=%s  WHERE st_reference=%s and date_stamp=%s ",(time_out,new_duration,reference,dt.now().date().strftime('%Y-%m-%d')))
#                     db.commit()
#                     return "Hey! have successfully logged out"
#                 else:
#                     return "Oops! you are already logged out!"
#         else:
#              return "Oops! student details not found."

# m=log_student_out('20661163')
# print(m)



# def get_names(date:str,end:str):
#     start_date="\'{}\'".format(date)
#     end_date="\'{}\'".format(end)
#     data = query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp BETWEEN "+start_date+" AND "+end_date)
#     result= []
#     for item in data:
#         item = str(item[0]).split(' ')
#         result.append(item[1][0:4].upper())   
#     return result
# d=get_names('2022-10-24','2022-10-27')
# print(d)

# def count_programs_by_date(date:str,end:str):
#         start_date="\'{}\'".format(date)
#         end_date="\'{}\'".format(end)
#         data = query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp BETWEEN "+start_date+" AND "+end_date)
#         result= []
#         for item in data: 
#             result.append(item[0])
#         total:list = []
#         for item in result:
#             program = "\'{}\'".format(item)
#             sub_count = query_database("SELECT COUNT(*) FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" and "+end_date+" and program="+program)
#             total.append(sub_count[0][0])
#         return total
# u = count_programs_by_date('2022-10-24','2022-10-27')
# print(u)


# def count_programs():
#     data = query_database("SELECT DISTINCT program FROM tb_attendance")
#     result= []
#     for item in data: 
#         result.append(item[0])
#     total:list = []
#     for item in result:
#         program = "\'{}\'".format(item)
#         sub_count = query_database("SELECT COUNT(*) FROM tb_attendance WHERE program="+program)
#         total.append(sub_count[0][0])
#     return total

# g =count_programs()    
# print(g)

# def get_names(program:str):
#     results_list = []
#     program_="\'{}\'".format(program)
#     for date in range(len(dates)):
#         # date_values="\'{}\'".format(dates[date])
#         results=query_database("SELECT COUNT(*)  distinct date_stamp FROM tb_attendance where program="+program_)
#         results_list.append(results[0][0])
#     return results_list
    
# dates = ['2022-10-24','2022-10-27','2022-10-25']   
# d=get_names('BSc. Chemistry')
# print(d)

# def get_all_distinct_dates_for_line_plot(program:str):
#     program_="\'{}\'".format(program)
#     results_list = []
#     results=query_database("SELECT DISTINCT date_stamp FROM tb_attendance where program="+program_)
#     for date in results:
#             results_list.append(date[0])
#     return results_list    

# d=get_all_distinct_dates_for_line_plot('BSc. Mathematics')
# print(d)



# def reconstruct_date(date:str):
#         list_months = ['January', 'Febuary', 'March',
#                 'April', 'May', 'June', 'July',
#                 'August', 'September', 'October',
#                 'November', 'December']
#         date_value=str(date).split('-')
#         year = date_value[0]
#         month = date_value[1]
#         day = date_value[2]
#         month=list_months[int(date_value[1])]
#         return str(day+' '+month+' '+year)


# def count_attendance_for_all_distinct_dates(program:str):
#     program_="\'{}\'".format(program)
#     results_list = []
#     results=query_database("SELECT DISTINCT date_stamp FROM tb_attendance where program="+program_+" order by date_stamp asc")
#     for date in results:
#         results_list.append(date[0])    
#     values =[]
#     for date in results_list:
#         date_values="\'{}\'".format(date)
#         result_set=query_database("SELECT COUNT(*) FROM tb_attendance where date_stamp="+date_values + " and program="+program_)
#         values.append(result_set[0][0])
#     return values, results[0][0], results[-1][-1]

# v =count_attendance_for_all_distinct_dates('BSc. Chemistry')
# print(v[1])
# d=reconstruct_date(v[1])
# print(d)


# def get_data_barchart():
#         query_result = query_database("SELECT DISTINCT program FROM tb_attendance")
#         result_list= []
#         for item in query_result: 
#             result_list.append(item[0])
#         total:list = []
#         for item in result_list:
#             program = "\'{}\'".format(item)
#             sub_count = query_database("SELECT COUNT(*) FROM tb_attendance WHERE program="+program)
#             total.append(sub_count[0][0])
#         data = query_database("SELECT DISTINCT program FROM tb_attendance")
#         results= []
#         for item in data:
#             item = str(item[0]).split(' ')
#             results.append(item[1][0:4].upper()) 
#         return total,results
# v = get_data_barchart()
# print(v[1])

# def get_names_all(self):
#         data = self.query_database("SELECT DISTINCT program FROM tb_attendance")
#         result= []
#         for item in data:
#             item = str(item[0]).split(' ')
#             result.append(item[1][0:4].upper()) 
#         return result

# def get_data_by_date_range(start_, end_):
#         start_date="\'{}\'".format(start_, end_)
#         end_date="\'{}\'".format(end_)
#         query_result = query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp BETWEEN "+start_date+" AND "+end_date)
#         result_list= []
#         for item in query_result: 
#             result_list.append(item[0])
#         total:list = []
#         for item in result_list:
#             program = "\'{}\'".format(item)
#             sub_count = query_database("SELECT COUNT(*) date_stamp FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" and "+end_date+" and program="+program)
#             total.append(sub_count[0][0])
#         print(total)
#         data = query_database("SELECT DISTINCT program FROM tb_attendance where date_stamp BETWEEN "+start_date+" AND "+end_date)
#         result= []
#         for item in data:
#             item = str(item[0]).split(' ')
#             result.append(item[1][0:4].upper())   
#         return total, result, start_date,end_date


# d = get_data_by_date_range('2022-10-27','2022-10-28')
# print(d)
# print(d[0])

# import sqlite3
# sql= """
#         CREATE TABLE IF NOT EXISTS tb_students(id INTEGER PRIMARY KEY AUTOINCREMENT, reference int NOT NULL UNIQUE, index_ int NOT NULL UNIQUE,
#         firstname TEXT NOT NULL, lastname TEXT NOT NULL, college TEXT NOT NULL,program TEXT NOT NULL,nationality TEXT NOT NULL,
#         startdate TEXT NOT NULL, enddate TEXT NOT NULL)
#     """
# con = sqlite3.connect(r'backend\\sqlite\\attendance_system.db')
# c = con.cursor()
# c.execute(sql)
# con.commit()

# def fetch_data_by_program_and_date(start,prog): 
#         start_date="\'{}\'".format(start)
#         program="\'{}\'".format(prog)
#         results = query_database("SELECT * FROM tb_attendance WHERE program="+program+" and date_stamp="+start_date)
#         return results
# d = fetch_data_by_program_and_date('2022-11-07','BSc. Chemistry')
# print(d)

import json
def tryy(start,end,prog): 
        start_date="\'{}\'".format(start)
        end_date="\'{}\'".format(end)
        program="\'{}\'".format(prog)
        results = query_database("SELECT * FROM tb_attendance WHERE date_stamp BETWEEN "+start_date+" and "+end_date+" and program="+program)
        return results
c = tryy('2022-10-27','2022-11-07','BSc. Chemistry')
print(json.dumps(c))