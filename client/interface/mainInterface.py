import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout
from src.widgets.generadorDatos import generar_datos_Distribucion
from client.interface.tablaDatosPrincipal import TablaGeneral
from client.interface.grilla import Grilla


class InterfazGrafica(QWidget):
    def __init__(self):
        super().__init__()
        


        # Crear la tabla 1
        #IMPORTANTE: tenemos que crear 
        mis_datos = {"media": 1,"desviacion":0,"lambda":5,"limiteSuperior":20,"limiteInferior":0}
        #generate en el arreglo con los datos generados aleatoriamente
        datos_distribucion = generar_datos_Distribucion(50000,2,mis_datos)
        tablaDatos = TablaGeneral(datos_distribucion)
        # Modificar el tamaño del contenedor de TablaGeneral
        tablaDatos.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        tablaDatos.setFixedWidth(350)


        # Crear el layout vertical principal
        layout_general = QVBoxLayout()

        # Crear el layout horizontal 1
        sub_layout_Horizontal1 = QHBoxLayout()

        # Crear el primer container
        container1 = QWidget()
        container1.setLayout(tablaDatos)
        container1.setStyleSheet("background-color: red;") # Estilo para identificar el container
        sub_layout_Horizontal1.addWidget(container1)

        # Crear el segundo container
        container2 = QWidget()
        container2.setStyleSheet("background-color: green;") # Estilo para identificar el container
        sub_layout_Horizontal1.addWidget(container2)

        # Agregar el layout horizontal 1 al layout general
        layout_general.addLayout(sub_layout_Horizontal1)

        # Crear el container 3
        container3 = QWidget()
        container3.setStyleSheet("background-color: blue;") # Estilo para identificar el container
        layout_general.addWidget(container3)

        # Crear una instancia de MiGrilla
        mi_grilla = Grilla()

        # Agregar la instancia de MiGrilla al layout general
        layout_general.addWidget(mi_grilla)

        # Establecer el layout general como el layout principal de la ventana
        self.setLayout(layout_general)

if __name__ == '__main__':
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear la ventana de la interfaz gráfica
    ventana = InterfazGrafica()
    ventana.show()

    # Ejecutar el bucle de eventos
    sys.exit(app.exec_())