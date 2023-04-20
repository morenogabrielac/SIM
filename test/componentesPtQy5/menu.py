import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar() # Se crea una instancia de la barra de menú
        fileMenu = menubar.addMenu('Archivo') # Se crea un menú "Archivo"

        exitAction = QAction('Salir', self) # Se crea una acción "Salir"
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit) # Se conecta la acción a la función qApp.quit, que sale de la aplicación

        fileMenu.addAction(exitAction) # Se añade la acción "Salir" al menú "Archivo"

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Menú básico')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
