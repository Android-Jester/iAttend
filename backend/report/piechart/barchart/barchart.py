import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Barchart(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(10, 10),
        sharey = True, facecolor='#2d2d2d')
        super().__init__(self.fig)
        self.ax.set_facecolor('#2d2d2d')
        self.ax.spines['top'].set_color('#2d2d2d')
        self.ax.spines['right'].set_color('#2d2d2d')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['bottom'].set_color('white')
        width = 0.2

        students = ['CSE', 'ISE', 'MECH', 'EEE', 'ESC', 'BCH']
        boys = [20, 30, 46, 10, 15, 40]
        girls = [10, 40, 46, 20, 30, 50]
        some = [5, 19, 30, 10, 35, 55]
        bar_1 = np.arange(len(students))
        bar_2 = [i+width for i in bar_1]
        bar_3 = [i+width for i in bar_2]
       
        self.ax.bar(bar_1, boys, width, label = "boys")   
        self.ax.bar(bar_2, girls, width, label = "girls") 
        self.ax.bar(bar_3, some, width, label = "some")

        plt.title('Barchart', size= 20, family = 'Arial',pad=30, color='white')
        plt.xlabel("Courses",color='white',size= 20)
        plt.ylabel("Students",color='white',size= 20)
        plt.xticks(bar_1+width/3, students,color='white',size= 10)
        plt.yticks(color='white',size= 10)
        plt.legend(labelcolor = '#2d2d2d')
        plt.savefig(r'D:\\Commons\\backend\\report\\piechart\\barchart\\bar.png',dpi = 300, edgecolor='none')
b= Barchart()

    