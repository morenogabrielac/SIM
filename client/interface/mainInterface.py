import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QFormLayout, QLineEdit, QSizePolicy
from src.widgets.datosRnd import generar_datos_aleatorios
from src.widgets.tabla1 import Tabla1


class InterfazGrafica(QWidget):
    def __init__(self):
        super().__init__()
        



        # Crear la tabla 1
        #generate en el arreglo con los datos generados aleatoriamente
        datos,distribucion = generar_datos_aleatorios(50000)
        self.tabla1 = Tabla1(datos,distribucion)
        # Modificar el tamaño del contenedor de Tabla1
        self.tabla1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.tabla1.setFixedWidth(350)



        # Crear la tabla 2
        self.tabla2 = QTableWidget()
        self.tabla2.setColumnCount(4)
        self.tabla2.setHorizontalHeaderLabels(['Columna 1', 'Columna 2', 'Columna 3', 'Columna 4'])


        # Crear el formulario
        self.formulario = QFormLayout()

        # Agregar elementos al formulario
        self.formulario.addRow('Campo 1:', QLineEdit())
        self.formulario.addRow('Campo 2:', QLineEdit())
        self.formulario.addRow('Campo 3:', QLineEdit())

        # Crear diseño vertical para la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.tabla1)
        layout.addWidget(self.tabla2)        
        layout.addLayout(self.formulario)

        # Establecer el diseño en la ventana
        self.setLayout(layout)

if __name__ == '__main__':
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear la ventana de la interfaz gráfica
    ventana = InterfazGrafica()
    ventana.show()

    # Ejecutar el bucle de eventos
    sys.exit(app.exec_())