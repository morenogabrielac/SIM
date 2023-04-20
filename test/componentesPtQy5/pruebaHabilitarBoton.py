import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout

class Formulario(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Crear etiquetas y campos de entrada
        self.lbl1 = QLabel('Campo 1', self)
        self.lbl2 = QLabel('Campo 2', self)
        self.lbl3 = QLabel('Campo 3', self)
        self.txt1 = QLineEdit(self)
        self.txt2 = QLineEdit(self)
        self.txt3 = QLineEdit(self)

        # Crear el menú desplegable
        self.combo = QComboBox(self)
        self.combo.addItem("Seleccione la distribucion")
        self.combo.addItem("Distribucion-1")
        self.combo.addItem("Distribucion-2")

        # Establecer la función que se llama cuando se selecciona una opción del menú
        self.combo.currentIndexChanged.connect(self.selectionchange)

        # Crear el layout vertical para el formulario
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.txt1)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.txt2)
        vbox.addWidget(self.lbl3)
        vbox.addWidget(self.txt3)
        vbox.addWidget(self.combo)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Formulario')

    def selectionchange(self, i):
        # Obtener la opción seleccionada del menú
        selected_option = self.combo.currentText()

        # Deshabilitar los campos de entrada según la opción seleccionada
        if selected_option == "Distribucion-1":
            self.txt1.setEnabled(False)
        elif selected_option == "Distribucion-2":
            self.txt2.setEnabled(False)
            self.txt3.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    formulario = Formulario()
    formulario.show()
    sys.exit(app.exec_())
