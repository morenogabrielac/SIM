import numpy as np
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class HistogramWidget(QWidget):
    def __init__(self, parent=None):
        super(HistogramWidget, self).__init__(parent)

        # Crear el layout principal y el canvas para el gráfico
        self.layout = QVBoxLayout(self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Crear un layout horizontal para los botones de selección
        button_layout = QHBoxLayout()
        self.layout.addLayout(button_layout)

        # Agregar un botón para generar el histograma exponencial negativo
        exponential_button = QPushButton("Exponencial Negativa")
        exponential_button.clicked.connect(self.create_exponential_histogram)
        button_layout.addWidget(exponential_button)

        # Agregar un botón para generar el histograma uniforme
        uniform_button = QPushButton("Uniforme")
        uniform_button.clicked.connect(self.create_uniform_histogram)
        button_layout.addWidget(uniform_button)

        # Agregar un botón para generar el histograma de Poisson
        poisson_button = QPushButton("Poisson")
        poisson_button.clicked.connect(self.create_poisson_histogram)
        button_layout.addWidget(poisson_button)

    def create_exponential_histogram(self):
        # Generar datos con distribución exponencial negativa
        data = np.random.exponential(scale=2, size=1000)

        # Crear un subplot y agregar el histograma
        ax = self.figure.add_subplot(111)
        ax.hist(data, bins=50, alpha=0.5)

        # Configurar el título y etiquetas de los ejes
        ax.set_title('Histograma de Distribución Exponencial Negativa')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frecuencia')

        # Actualizar el canvas
        self.canvas.draw()

    def create_uniform_histogram(self):
        # Generar datos con distribución uniforme
        data = np.random.uniform(size=1000)

        # Crear un subplot y agregar el histograma
        ax = self.figure.add_subplot(111)
        ax.hist(data, bins=50, alpha=0.5)

        # Configurar el título y etiquetas de los ejes
        ax.set_title('Histograma de Distribución Uniforme')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frecuencia')

        # Actualizar el canvas
        self.canvas.draw()

    def create_poisson_histogram(self):
        # Generar datos con distribución de Poisson
        data = np.random.poisson(lam=3, size=1000)

        # Crear un subplot y agregar el histograma
        ax = self.figure.add_subplot(111)
        ax.hist(data, bins=50, alpha=0.5)

        # Configurar el título y etiquetas de los ejes
        ax.set_title('Histograma de Distribución de Poisson')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frecuencia')

        # Actualizar el canvas
        self.canvas.draw()
