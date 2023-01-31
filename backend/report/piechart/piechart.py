
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Canvas(FigureCanvas):
    def __init__(self):
        pass
    def piechart(self,data:list,title:str):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(10, 10),
        sharey = False, facecolor='#2d2d2d')
        super().__init__(self.fig)
        plt.title(title, size= 15, family = 'Arial',pad=30, color='white')  
        self.ax.pie(data[0],labels=data[1],autopct = '%1.1f%%', labeldistance = 1.1
        , radius=0.4, startangle =90, pctdistance = 0.4,textprops={'color':"w",'fontsize':13})
        self.ax.axis('equal')
        plt.savefig('C:\ProgramData\iAttend\data\samples\\piechart.png',dpi = 300, edgecolor='none')
        plt.savefig('C:\ProgramData\iAttend\data\samples\\piechart.pdf',dpi = 300, edgecolor='none')
