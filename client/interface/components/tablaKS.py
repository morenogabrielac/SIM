from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaKS(QTableWidget):
    def __init__(self):
        super().__init__()
        
        #Estructura base
        cabezera = ['Intervalos','Desde', 'Hastas','Frec. Observada','Frec. Esperada','Po()','Pe()','Po(Acu)','Pe(Acu)','|Po(Acu)-Pe(Acu)|','Maximo']
        
        self.setColumnCount(len(cabezera))
        self.setRowCount(5)
        self.setHorizontalHeaderLabels(cabezera)
        for i in range(5):
            for j in range(len(cabezera)):
                self.setItem(i, j, QTableWidgetItem(f'Valor {i+1}-{j+1}'))
        
        
        
        #    
        """self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(150)"""