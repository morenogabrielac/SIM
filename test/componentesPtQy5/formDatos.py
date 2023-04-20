import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton


class Formulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formulario')
        self.setGeometry(100, 100, 400, 300)

        # Crear los widgets
        self.num_muestra_label = QLabel('Numero de muestra:')
        self.varianza_label = QLabel('Varianza:')
        self.media_label = QLabel('Media:')
        self.de_label = QLabel('Desviacion Estandar:')
        self.lambda_label = QLabel('Lambda:')
        self.intervalo_superior_label = QLabel('Intervalo Superior:')
        self.intervalo_inferior_label = QLabel('Intervalo Inferior:')
        self.cant_intervalo_label = QLabel('cantidad Intervalos:')

        self.num_muestra_edit = QLineEdit()
        self.varianza_edit = QLineEdit()
        self.media_edit = QLineEdit()
        self.de_edit = QLineEdit()
        self.lambda_edit = QLineEdit()
        self.intervalo_superior_edit = QLineEdit()
        self.intervalo_inferior_edit = QLineEdit()
        self.cant_intervalo_edit = QLineEdit()

        self.guardar_btn = QPushButton('Generar')
        self.guardar_btn.clicked.connect(self.guardar_datos)

        # Crear el layout
        layout = QGridLayout()
        layout.addWidget(self.num_muestra_label, 0, 0)
        layout.addWidget(self.num_muestra_edit, 0, 1)
        layout.addWidget(self.varianza_label, 1, 0)
        layout.addWidget(self.varianza_edit, 1, 1)
        layout.addWidget(self.media_label, 2, 0)
        layout.addWidget(self.media_edit, 2, 1)
        layout.addWidget(self.de_label, 3, 0)
        layout.addWidget(self.de_edit, 3, 1)
        layout.addWidget(self.lambda_label, 4, 0)
        layout.addWidget(self.lambda_edit, 4, 1)
        layout.addWidget(self.intervalo_superior_label, 5, 0)
        layout.addWidget(self.intervalo_superior_edit, 5, 1)
        layout.addWidget(self.intervalo_inferior_label, 6, 0)
        layout.addWidget(self.intervalo_inferior_edit, 6, 1)
        layout.addWidget(self.cant_intervalo_label, 7, 0)
        layout.addWidget(self.cant_intervalo_edit, 7, 1)
        layout.addWidget(self.guardar_btn, 8, 0, 1, 2)

        self.setLayout(layout)

    def guardar_datos(self):
        datos = {
            'Numero de muestra': self.num_muestra_edit.text(),
            'Varianza': self.varianza_edit.text(),
            'Media': self.media_edit.text(),
            'Desviacion Estandar': self.de_edit.text(),
            'Lambda': self.lambda_edit.text(),
            'Intervalo Superior': self.intervalo_superior_edit.text(),
            'Intervalo Inferior': self.intervalo_inferior_edit.text(),
            'Cantidad intervalos': int(self.cant_intervalo_edit.text())
        }
        print(datos)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    formulario = Formulario()
    formulario.show()
    sys.exit(app.exec_())
