from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class Tabla1(QTableWidget):
    def __init__(self, datos,dist):
        super().__init__()
        
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['Datos Aleatorios',"Distribucion"])
        


        # Configurar la tabla para mostrar solo 15 datos
        self.setRowCount(15)
        for i in range(15):
            self.setItem(i, 0, QTableWidgetItem(str(datos[i])))
            self.setItem(i, 1, QTableWidgetItem(str(dist[i])))
            
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(150)
            
            

            

