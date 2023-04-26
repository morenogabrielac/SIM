from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaChiCuadradoDiscreta(QTableWidget):
    def __init__(self):
        super().__init__()
        
        #Estructura base
        
        header =  ['Valor','Frec. Observada','Frec. Esperada','c']
        
        self.setColumnCount(len(header))
        self.setRowCount(10)
        self.setHorizontalHeaderLabels(header)
        for i in range(10):    

                self.setItem(i, 0, QTableWidgetItem())
                self.setItem(i, 1, QTableWidgetItem())
                self.setItem(i, 2, QTableWidgetItem())                
                self.setItem(i, 3, QTableWidgetItem())                
          
      
        
        
        
        #    
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(470)
        self.setFixedHeight(350)