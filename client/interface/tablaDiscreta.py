from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaDiscreta(QTableWidget):
    def __init__(self,valor,fo,densidad,fe):
    
        super().__init__()
        
        #Estructura base
        header = ['Valor','Frec. Observada','P()','Frec. Esperada']
        largo = len(valor)
        self.setColumnCount(len(header))
        self.setRowCount(largo)
        self.setHorizontalHeaderLabels(header)
        for i in range(largo):    
 
                self.setItem(i, 0, QTableWidgetItem(str(valor[i])))
                self.setItem(i, 1, QTableWidgetItem(str(fo[i])))
                self.setItem(i, 2, QTableWidgetItem(str(densidad[i])))                
                self.setItem(i, 3, QTableWidgetItem(str(fe[i])))                
                self.setItem(i, 4, QTableWidgetItem())                
                           

                
        
        
        
        #   
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(560)
        self.setFixedHeight(350)