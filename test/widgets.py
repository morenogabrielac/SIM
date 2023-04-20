import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QTableWidgetItem
#from componentesPtQy5.tablaKS import TablaKS
from componentesPtQy5.grafico import HistogramWidget as NormalGraph
from componentesPtQy5.graficoTest import HistogramWidget
from componentesPtQy5.graficoTestGeneral import RandomDataHistogram as Graph
from componentesPtQy5.tablaDistribucionRandom import *
from componentesPtQy5.pruebaHabilitarBoton import MyTest
from gui.datosRnd import generar_datos_aleatorios as generate
class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Crear widget
        datos,distribucion = generate(50000)
        mytest = MyTest()


        # Crear el layout horizontal
        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()


        layout_vertical.addWidget(MyTest)
        layout_horizontal.addLayout(layout_vertical)
        
      

        # Establecer el layout vertical en la ventana
        self.setLayout(layout_horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec_())
