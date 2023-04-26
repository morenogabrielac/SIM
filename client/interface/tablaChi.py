from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QSizePolicy

class TablaChiCuadrado(QTableWidget):
    def __init__(self,vectorIntervalosInicioFin,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado):
        super().__init__()
        
        #Estructura base
        
        header =  ['Desde', 'Hastas','Frec. Observada','Frec. Esperada','c']
        intervalo= int(len(vectorIntervalosInicioFin)/2)
        self.setColumnCount(len(header))
        self.setRowCount(intervalo)
        self.setHorizontalHeaderLabels(header)
        for i in range(intervalo):    
            if(i != 0): 
                self.setItem(i, 0, QTableWidgetItem(str(vectorIntervalosInicioFin[i*2])))
                self.setItem(i, 1, QTableWidgetItem(str(vectorIntervalosInicioFin[(i*2)+1])))
                self.setItem(i, 2, QTableWidgetItem(str(vectorFrecuenciaObservada[i])))                
                self.setItem(i, 3, QTableWidgetItem(str(vectorFrecuenciaEsperada[i])))                
                self.setItem(i, 4, QTableWidgetItem(str(vectorCChiCuadrado[i])))                
                #self.setItem(i, 5, QTableWidgetItem(str(acumuladorCChiCuadrado[i])))                            
            else:
                self.setItem(i, 0, QTableWidgetItem(str(vectorIntervalosInicioFin[i])))
                self.setItem(i, 1, QTableWidgetItem(str(vectorIntervalosInicioFin[(i)+1])))
                self.setItem(i, 2, QTableWidgetItem(str(vectorFrecuenciaObservada[i])))                
                self.setItem(i, 3, QTableWidgetItem(str(vectorFrecuenciaEsperada[i])))                
                self.setItem(i, 4, QTableWidgetItem(str(vectorCChiCuadrado[i])))                
               # self.setItem(i, 5, QTableWidgetItem(str(acumuladorCChiCuadrado[i])))      
        
        
        
        #    
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFixedWidth(770)
        self.setFixedHeight(350)