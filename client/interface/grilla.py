from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton


class Grilla(QWidget):
    def __init__(self):
        super().__init__()
 # Crear la grilla con 5 espacios
        grilla = QGridLayout()

        # Crear el primer espacio y agregar un QLabel
        label = QLabel("Texto en espacio 1")
        grilla.addWidget(label, 0, 0)

        # Crear los dos botones y agregarlos en los últimos dos espacios
        boton1 = QPushButton("Chi cuadrado") 
        boton2 = QPushButton("Kolmogorov-Smirnov")
        grilla.addWidget(boton1, 0, 3)
        grilla.addWidget(boton2, 0, 4)
        
        
        
        # Establecer la grilla como el layout del widget           
        self.setLayout(grilla)

        
