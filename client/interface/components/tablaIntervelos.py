from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaIntervalos(QTableWidget):
    def __init__(self):
        super().__init__()
        
        #Estructura base
        
        tabla = QTableWidget()
        tabla.setColumnCount(6)
        tabla.setRowCount(5)
        tabla.setHorizontalHeaderLabels(['Intervalos', 'Desde', 'Hastas','Frec. Observada','P()','Frec. Esperada'])
        for i in range(5):
            for j in range(6):
                tabla.setItem(i, j, QTableWidgetItem(f'Valor {i+1}-{j+1}'))
        
        
        
        #    
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(150)