import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QFormLayout, QLineEdit, QSizePolicy
from src.widgets.generadorDatos import generar_datos_Distribucion
from client.interface.tablaDatosPrincipal import TablaGeneral


class InterfazGrafica(QWidget):
    def __init__(self):
        super().__init__()
        


        # Crear la tabla 1
        #IMPORTANTE: tenemos que crear 
        mis_datos = {"media": 1,"desviacion":0,"lambda":5,"limiteSuperior":20,"limiteInferior":0}
        #generate en el arreglo con los datos generados aleatoriamente
        datos_distribucion = generar_datos_Distribucion(50000,2,mis_datos)
        tablaGeneral = TablaGeneral(datos_distribucion)
        # Modificar el tamaño del contenedor de TablaGeneral
        tablaGeneral.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        tablaGeneral.setFixedWidth(350)



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
        layout.addWidget(tablaGeneral)
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