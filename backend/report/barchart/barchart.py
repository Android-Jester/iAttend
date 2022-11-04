import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Barchart(FigureCanvas):
    def __init__(self):
        pass

    def bar_plot_single_view(self, y_value:list,x_labels:list,bar_width:int,title:str,y_label:str,x_label:str,colors:list):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(10, 10),
        sharey = False, facecolor='#2d2d2d')
        super().__init__(self.fig)
        self.ax.set_facecolor('#2d2d2d')
        self.ax.spines['top'].set_color('#2d2d2d')
        self.ax.spines['right'].set_color('#2d2d2d')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['bottom'].set_color('white')     
        plt.bar(x_labels,y_value,width=bar_width,alpha=0.8,color=colors)    
        plt.title(title, size= 20, family = 'Arial',pad=30, color='white')
        plt.xlabel(x_label,color='white',size= 15,labelpad= 13)
        plt.ylabel(y_label,color='white',size= 15,labelpad= 13)
        plt.yticks(color='white',size= 12)
        plt.xticks(color='white',size= 12)
        plt.savefig(r'backend\\report\\barchart\\barchart.png',dpi = 300, edgecolor='none')
        plt.savefig(r'backend\\report\\barchart\\barchart.pdf',dpi = 300, edgecolor='none')



    