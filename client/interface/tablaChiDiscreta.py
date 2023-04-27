from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaChiCuadradoDiscreta(QTableWidget):
    def __init__(self,valores, fe, fo,c):
        super().__init__()
        
        #Estructura base
        
        header =  ['Valor/es','Frec. Observada','Frec. Esperada','c']
        intervalo = len(valores)
        self.setColumnCount(len(header))
        self.setRowCount(intervalo)
        self.setHorizontalHeaderLabels(header)
        for i in range(intervalo):    

                self.setItem(i, 0, QTableWidgetItem(str(valores[i])))
                self.setItem(i, 1, QTableWidgetItem(str(fo[i])))
                self.setItem(i, 2, QTableWidgetItem(str(fe[i])))                
                self.setItem(i, 3, QTableWidgetItem(str(c[i])))                
          
      
        
        
        
        #    
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(560)
        self.setFixedHeight(350)