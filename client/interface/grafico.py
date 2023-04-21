import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class RandomDataHistogram(QWidget):
    def __init__(self,intervalo ,parent=None):
        super(RandomDataHistogram, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        data  = np.random.normal(0, 1, 50000)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        #bins = np.linspace(min(data), max(data), intervalo)
        bins = np.linspace(data.min(), data.max(), intervalo)
        self.ax.hist(data, bins=bins, alpha=0.5)
        self.ax.set_title('Histograma de Datos')
        self.ax.set_xlabel('Valor')
        self.ax.set_ylabel('Frecuencia')
        self.canvas.draw()

       

      


        """La función linspace recibe tres argumentos: el valor mínimo, el valor máximo y el número
        de elementos que queremos en el array. En este caso, estamos creando 50 valores entre el valor
        mínimo y máximo de la variable data, que se utilizarán como los intervalos o "bins" para
        construir el histograma.
        Este enfoque de especificar los bins es comúnmente utilizado en la creación de histogramas,
        ya que permite definir de manera explícita los límites de los intervalos en los que se agruparán
        los datos para generar las barras del histograma."""    
