from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaIntervalos(QTableWidget):
    def __init__(self,vectorIIF_BASE,vectorMC,vectorFO_BASE,vectorDistribucionDensidad,vectorFE_BASE,intervalo):
    
        super().__init__()
        
        #Estructura base
        header = ['Desde', 'Hastas','Marca de Clase','Frec. Observada','P()','Frec. Esperada']
        intervalo= int(len(vectorIIF_BASE)/2)
        self.setColumnCount(len(header))
        self.setRowCount(intervalo)
        self.setHorizontalHeaderLabels(header)
        for i in range(intervalo):    
            if(i != 0): 
                self.setItem(i, 0, QTableWidgetItem(str(vectorIIF_BASE[i*2])))
                self.setItem(i, 1, QTableWidgetItem(str(vectorIIF_BASE[(i*2)+1])))
                self.setItem(i, 2, QTableWidgetItem(str(vectorMC[i])))                
                self.setItem(i, 3, QTableWidgetItem(str(vectorFO_BASE[i])))                
                self.setItem(i, 4, QTableWidgetItem(str(vectorDistribucionDensidad[i])))                
                self.setItem(i, 5, QTableWidgetItem(str(vectorFE_BASE[i])))                            
            else:
                self.setItem(i, 0, QTableWidgetItem(str(vectorIIF_BASE[i])))
                self.setItem(i, 1, QTableWidgetItem(str(vectorIIF_BASE[i+1])))
                self.setItem(i, 2, QTableWidgetItem(str(vectorMC[i])))                
                self.setItem(i, 3, QTableWidgetItem(str(vectorFO_BASE[i])))                
                self.setItem(i, 4, QTableWidgetItem(str(vectorDistribucionDensidad[i])))                
                self.setItem(i, 5, QTableWidgetItem(str(vectorFE_BASE[i])))                
 
                
        
        
        
        #   
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(770)
        self.setFixedHeight(350)