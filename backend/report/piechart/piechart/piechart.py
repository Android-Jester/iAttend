
from cProfile import label
from hashlib import sha1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import mysql.connector as connector
from datetime import datetime as dt
import pandas as pd
from regex import P


db = connector.connect(
        host="localhost",
        user = "root",
        passwd = "0552588647",
        database = "students"
        )
my_cursor =db.cursor()


class Canvas(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(10, 10),
        sharey = True, facecolor='#2d2d2d')
        super().__init__(self.fig)

        total =self.count_programs()
        names = self.get_names()
        names[4]='Optometry'
        plt.title('Percentage of programs', size= 20, family = 'Arial',pad=30, color='white')
        
        self.ax.pie(total,labels=names,autopct = '%1.1f%%', labeldistance = 1.1
        , radius=0.4, startangle =90, pctdistance = 0.4,textprops={'color':"w",'fontsize':13})
        self.ax.axis('equal')
        plt.savefig(r'D:\\Commons\\backend\\report\\piechart\\piechart\\pie.png',dpi = 300, edgecolor='none')

    def query_database(self,query: str):
        details = []
        cursor = my_cursor.execute(query)
        cursor = my_cursor.fetchall()
        if cursor:
            for item in cursor:
                details.append(item)
            db.commit()
        return details

    def count_programs(self):
        data = self.query_database("SELECT DISTINCT program FROM tb_attendance")
        result= []
        for item in data: 
            result.append(item[0])
        total:list = []
        for item in result:
            program = "\'{}\'".format(item)
            sub_count = self.query_database("SELECT COUNT(*) FROM tb_attendance WHERE program="+program)
            total.append(sub_count[0][0])
        return total

    def get_names(self):
        data = self.query_database("SELECT DISTINCT program FROM tb_attendance")
        result= []
        for item in data:
            item = str(item[0]).split(' ')
            result.append(item[1]) 
        return result

c = Canvas()

