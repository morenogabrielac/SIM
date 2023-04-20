import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class RandomDataHistogram(QWidget):
    def __init__(self, parent=None):
        super(RandomDataHistogram, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.comboBox = QComboBox()
        self.comboBox.addItem("Exponencial Negativo")
        self.comboBox.addItem("Uniforme")
        self.comboBox.addItem("Poisson")
        self.layout.addWidget(self.comboBox)

        self.button = QPushButton("Crear Histograma")
        self.button.clicked.connect(self.create_histogram)
        self.layout.addWidget(self.button)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def create_histogram(self):
        distribution = self.comboBox.currentText()
        if distribution == "Exponencial Negativo":
            data = np.random.exponential(2, 1000)
        elif distribution == "Uniforme":
            data = np.random.uniform(0, 10, 1000)
        elif distribution == "Poisson":
            data = np.random.poisson(5, 1000)
            
        """La función linspace recibe tres argumentos: el valor mínimo, el valor máximo y el número
        de elementos que queremos en el array. En este caso, estamos creando 50 valores entre el valor
        mínimo y máximo de la variable data, que se utilizarán como los intervalos o "bins" para
        construir el histograma.
        Este enfoque de especificar los bins es comúnmente utilizado en la creación de histogramas,
        ya que permite definir de manera explícita los límites de los intervalos en los que se agruparán
        los datos para generar las barras del histograma."""    

        bins = np.linspace(data.min(), data.max(), 15)
        self.ax.hist(data, bins=bins, alpha=0.5)
        self.ax.set_title('Histograma de Datos')
        self.ax.set_xlabel('Valor')
        self.ax.set_ylabel('Frecuencia')
        self.canvas.draw()
