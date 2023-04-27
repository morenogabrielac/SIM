import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class poissonGrafico(QWidget):
    def __init__(self, valores_obtenidos,frecuencia_observada, parent=None):
    
        super(poissonGrafico, self).__init__(parent)
        

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)        

        self.ax.bar(valores_obtenidos,frecuencia_observada)

        self.ax.set_title('Histograma de Datos')
        self.ax.set_xlabel('Valor')
        self.ax.set_ylabel('Frecuencia')  
        self.canvas.draw()    

