
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Line_plot(FigureCanvas):
    def __init__(self):
        pass

    def plot_graph(self,y_values:list,title:str,label_:str,y_label:str,x_label:str):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(10, 10),
        sharey = True, facecolor='#2d2d2d')
        super().__init__(self.fig)
        self.ax.set_facecolor('#2d2d2d')
        self.ax.spines['top'].set_color('#2d2d2d')
        self.ax.spines['right'].set_color('#2d2d2d')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['bottom'].set_color('white')

        plt.plot(y_values,label=label_,marker='D')
        
        plt.title(title, size= 15, family = 'Arial',pad=30, color='white')
        plt.xlabel(x_label,color='white',size= 15,labelpad = 13)
        plt.ylabel(y_label,color='white',size= 15,labelpad = 13)
        plt.yticks(color='white',size= 12)
        plt.xticks(color='white',size= 12)
        plt.legend(label_,labelcolor = '#2d2d2d',handletextpad=0.5)
        plt.savefig('C:\\ProgramData\\iAttend\\data\\reports\\visualize\\linegraph.png',dpi = 300, edgecolor='none')

    def save_chart(self,name):
        plt.savefig('C:\\ProgramData\\iAttend\\data\\reports\\linegraph\\'+name+'.pdf',dpi = 300, edgecolor='none')


