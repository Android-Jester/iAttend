
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Piechart(FigureCanvas):
    def __init__(self):
        pass
    def piechart(self,data:list,title:str,colors:list,startangle,area,dpi,labeldistance,pctdistance,xlabel):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(area, area),
        sharey = False, facecolor='#2d2d2d')
        super().__init__(self.fig)
        plt.title(title, size= 15, family = 'Arial',pad=30, color='white')
        plt.xlabel(xlabel, size= 15, family = 'Arial',labelpad=30, color='white') 
        self.ax.pie(data[1],labels=data[0],autopct = '%1.1f%%', colors=colors, labeldistance = labeldistance
        , radius=0.4, startangle =startangle, pctdistance = pctdistance,textprops={'color':"w",'fontsize':13})
        self.ax.axis('equal')
        plt.savefig('C:\\ProgramData\\iAttend\\data\\reports\\visualize\\piechart.png',dpi = dpi, edgecolor='none')

    def save_chart(self,name):
        plt.savefig('C:\\ProgramData\\iAttend\\data\\reports\\piechart\\'+name+'.pdf',dpi = 1000, edgecolor='none')
        
