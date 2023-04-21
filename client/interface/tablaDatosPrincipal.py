from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem,QSizePolicy

class TablaGeneral(QTableWidget):
    def __init__(self, datos):
        super().__init__()
        
        self.setColumnCount(1)
        self.setHorizontalHeaderLabels(['Datos Aleatorios'])
        


        # Configurar la tabla para mostrar solo 15 datos
        self.setRowCount(50)
        for i in range(50):
            self.setItem(i, 0, QTableWidgetItem(str(datos[i])))

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(150)            
            

            

