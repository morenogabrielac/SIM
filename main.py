from PyQt5.QtWidgets import QApplication
from client.interface.mainInterface import InterfazGrafica as UI
import sys

# Función para ejecutar la aplicación
def run_app():
    app = QApplication(sys.argv)
    ventana = UI()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_app()
