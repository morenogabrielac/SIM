from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaChiCuadrado(QTableWidget):
    def __init__(self):
        super().__init__()
        
        #Estructura base
        
        
        self.setColumnCount(6)
        self.setRowCount(5)
        self.setHorizontalHeaderLabels(['Desde', 'Hastas','Frec. Observada','Frec. Esperada','c','C(acu)'])
        for i in range(5):
            for j in range(6):
                self.setItem(i, j, QTableWidgetItem(f'Valor {i+1}-{j+1}'))
        
        
        
        #    
        """self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(150)"""