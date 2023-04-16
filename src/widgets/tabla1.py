from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class Tabla1(QTableWidget):
    def __init__(self, datos):
        super().__init__()
        
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['Datos Aleatorios'])
        


        # Configurar la tabla para mostrar solo 15 datos
        self.setRowCount(15)
        for i in range(15):
            self.setItem(i, 0, QTableWidgetItem(str(datos[i])))

            
            

            

