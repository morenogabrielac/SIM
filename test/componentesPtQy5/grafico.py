


from PyQt5.QtWidgets import  QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import numpy as np

class HistogramWidget(QWidget):
    def __init__(self, parent=None):
        super(HistogramWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        self.create_histogram()
        
        
    def create_histogram(self):
        """
        bins es el número de contenedores que se usarán para el histograma y 
        alpha es la opacidad de las barras del histograma.
        """
        data = np.random.normal(0, 1, 50400)
        #subplot hace referencia a la cantidad de subtramas que quiero en mi grafico, 
        # y como vamos a creaer un solo grafico la notacion "111" hace referencia a eso mismo.
        ax = self.figure.add_subplot(111)
        ax.hist(data, bins=100, alpha=0.75)
        ax.set_title('Histograma de Datos')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frecuencia')
        self.canvas.draw()
        
        
        
        #    
        """self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(150)"""