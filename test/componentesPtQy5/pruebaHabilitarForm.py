from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear el menú y los campos
        self.menu = QComboBox()
        self.menu.addItem("Seleccione su Distribucion preferida")
        self.menu.addItem("Distribución-1")
        self.menu.addItem("Distribución-2")
        self.field1 = QLineEdit()
        self.field2 = QLineEdit()
        self.field3 = QLineEdit()

        # Crear el layout y agregar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.field1)
        layout.addWidget(self.field2)
        layout.addWidget(self.field3)

        # Crear el widget central y asignar el layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Conectar la señal currentIndexChanged del menú a la función on_menu_changed
        self.menu.currentIndexChanged.connect(self.on_menu_changed)

    def on_menu_changed(self, index):
        # Habilitar/deshabilitar los campos según la opción seleccionada
        if index == 1: # Distribución-1
            self.field1.setEnabled(True)
            self.field2.setEnabled(False)
            self.field3.setEnabled(False)
        elif index == 2: # Distribución-2
            self.field1.setEnabled(False)
            self.field2.setEnabled(True)
            self.field3.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
