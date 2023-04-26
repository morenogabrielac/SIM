import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from src.widgets.generadorDatos import generar_datos_Distribucion
#from client.interface.components.formDatos import  Formulario
from client.interface.tablaIntervelos import TablaIntervalos
from client.interface.tablaDatosPrincipal import TablaGeneral
from client.interface.tablaChi import TablaChiCuadrado
from src.funcionesDistNormal import *
from src.funcionesDistExponencial import distribucion_Densidad as exponencial
from src.funcionesDistExponencial import distribucion_DensidadBase as exponencialBase
from src.funcionesDistUniforme import distribucion_Densidad as uniforme
from src.funcionesDistUniforme import distribucion_DensidadBase as uniformeBase
from src.funcionesDistPoisson import distribucion_Densidad as poisson
from src.funcionesDistPoisson import distribucion_DensidadBase as poissonBase

from client.interface.grafico import RandomDataHistogram as Grafico
from src.widgets.generadorVariablesAleatorias import prueba_chi

class InterfazGrafica(QWidget):
    def __init__(self):
        super().__init__()
        
        #Desv Standar es raiz cuadrada varianza
        # Crear la tabla 1
        #IMPORTANTE: tenemos que crear 
        
        #generate en el arreglo con los datos generados aleatoriamente
       

#----------------------------------------------------------------INTERFAZ DE BOTONES DISTRIBUCION----------------------------------------------------------------
        self.setGeometry(400, 400, 370, 280)
        self.setWindowTitle('Menú de Distribuciones')
        self.label= QLabel('Seleccione la distribucion:', self)
        self.label.setFont(QFont('Helvetica', 10))
        self.label.setGeometry(60, 10, 400, 50)
        
        # Crear un layout vertical para los botones
        layout = QVBoxLayout()

        # Crear un botón para abrir la segunda ventana
        self.button1 = QPushButton('Normal', self)
        self.button1.setFont(QFont('Helvetica', 14))
        self.button1.setStyleSheet("background-color: #1abc9c; color: #fff; border-radius: 5px; padding: 8px;")
        layout.addWidget(self.button1)
        self.button1.setGeometry(50, 60, 250, 40)

        self.button2 = QPushButton('Poisson', self)
        self.button2.setStyleSheet("background-color: #3498db; color: #fff; border-radius: 5px; padding: 8px;")
        self.button2.setFont(QFont('Helvetica', 14))
        layout.addWidget(self.button2)
        self.button2.setGeometry(50, 110, 250, 40)

        self.button3 = QPushButton('Exponencial Negativa', self)
        self.button3.setStyleSheet("background-color: #9b59b6; color: #fff; border-radius: 5px; padding: 8px;")
        self.button3.setFont(QFont('Helvetica', 14))
        layout.addWidget(self.button3)
        self.button3.setGeometry(50, 160, 250, 40)

        self.button4 = QPushButton('Uniforme', self)
        self.button4.setStyleSheet("background-color: #e67e22; color: #fff; border-radius: 5px; padding: 8px;")
        self.button4.setFont(QFont('Helvetica', 14))
        layout.addWidget(self.button4)
        self.button4.setGeometry(50, 210, 250, 40)
        
        # Conectar la señal clicked() del botón a la función abrir_ventana()
        self.button1.clicked.connect(self.open_window_normal)
        self.button2.clicked.connect(self.open_window_poisson)
        self.button3.clicked.connect(self.open_window_exponencial)
        self.button4.clicked.connect(self.open_window_uniforme)
        # Mostrar la ventana principal
        self.show()
        
    def open_window_normal(self):
        self.new_window = Formulario_Normal()
        self.new_window.show()        
    def open_window_poisson(self):
        self.new_window = Formulario_Poisson()
        self.new_window.show()        
    def open_window_exponencial(self):
        self.new_window = Formulario_Exponencial()
        self.new_window.show()        
    def open_window_uniforme(self):
        self.new_window = Formulario_Uniforme()
        self.new_window.show()        

#-----------------------------------------------------DISTRIBUCION NORMAL-------------------------------------------------
#--------------------------------------------Interfaz de distribucion NORMAL----------------------------------------------
class Formulario_Normal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formulario')
        self.setGeometry(100, 100, 400, 300)

        # Crear los widgets
        self.num_muestra_label = QLabel('Tamaño de muestra:')
        self.media_label = QLabel('Media:')
        self.de_label = QLabel('Desviacion Estandar:')
        self.cant_intervalo_label = QLabel('Cantidad Intervalos:')

        self.num_muestra_edit =  QLineEdit()
        self.media_edit = QDoubleSpinBox()
        self.media_edit.setRange(-1000, 1000)
        self.de_edit = QDoubleSpinBox()
        self.de_edit.setRange(-1000, 1000)
        self.cant_intervalo_edit = QLineEdit()

        self.guardar_btn = QPushButton('Generar')    
         
        self.guardar_btn.clicked.connect(self.open_window_normal_stats)

        # Crear el layout
        layout = QGridLayout()
        layout.addWidget(self.num_muestra_label, 0, 0)
        layout.addWidget(self.num_muestra_edit, 0, 1)
        layout.addWidget(self.media_label, 1, 0)
        layout.addWidget(self.media_edit,1, 1)
        layout.addWidget(self.de_label, 2, 0)
        layout.addWidget(self.de_edit, 2, 1)
        layout.addWidget(self.cant_intervalo_label, 3, 0)
        layout.addWidget(self.cant_intervalo_edit, 3, 1)
        layout.addWidget(self.guardar_btn, 4, 0, 1, 2)

        self.setLayout(layout)
        
   
       
    def open_window_normal_stats(self):
        n = int(self.num_muestra_edit.text())
        media = float(self.media_edit.value())
        desvE = float(self.de_edit.value())
        cantIntervalos = int(self.cant_intervalo_edit.text())
        
        datos = {
            'Numero de muestra': n,
            'Varianza': 0,
            'Media': media,
            'Desviacion Estandar': desvE,
            'Lambda': 0,
            'Intervalo Superior': 0,
            'Intervalo Inferior': 0,
            'Cantidad intervalos': cantIntervalos
        }
       
        self.new_window = Graficos_Normal(datos)
        self.new_window.show()    
  
        
#----------------------------------------------Graficos de distribucion NORMAL----------------------------------------------    
    
class Graficos_Normal(QWidget):
    def __init__(self,datosEntrantes):
        super().__init__()
        self.setWindowTitle('Distribucion Normal')
        self.setGeometry(100, 100, 400, 300)

        datosGenerados = generar_datos_Distribucion(3,datosEntrantes)
        vectorMC,vectorIIF_BASE,vectorDistribucionDensidad,vectorFO_BASE,vectorFE_BASE = distribucion_DensidadBase(datosGenerados,datosEntrantes['Cantidad intervalos'])
        vectorIntervalosInicioFin,vectorDensidad,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado,gradosLibertad=distribucion_Densidad(datosGenerados,datosEntrantes['Cantidad intervalos'])
        intervalo = int(len(vectorIIF_BASE)/2)
        
        # Crear los widgets
        tablaAleadorios = TablaIntervalos(vectorIIF_BASE,vectorMC,vectorFO_BASE,vectorDistribucionDensidad,vectorFE_BASE,10)

        tablaGeneral = TablaGeneral(datosGenerados)
        graficoNormal = Grafico(vectorFO_BASE,vectorMC,intervalo)
        tablaChi = TablaChiCuadrado(vectorIntervalosInicioFin,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado)
        pruebaChi = prueba_chi(3,intervalo,acumuladorCChiCuadrado)
                # Crear los widgets
        pruebaChi_label = QLabel(pruebaChi)

         
        # Crear el layout
        layout_texto = QGridLayout()
        layout = QHBoxLayout()
        layoutTablas = QVBoxLayout()
        layoutGrafico = QVBoxLayout()        
        layout.addWidget(tablaGeneral)
        layoutTablas.addWidget(tablaAleadorios)
        layoutTablas.addWidget(tablaChi)
        layoutTablas.addLayout(layout_texto)
        layoutGrafico.addWidget(graficoNormal)
        layout_texto.addWidget(pruebaChi_label, 0, 0)
        
        
        
        #layoutTablas.addWidget(tablaChi)
        layout.addLayout(layoutTablas)
        layout.addLayout(layoutGrafico)
    
        


        self.setLayout(layout)
        


        


        #self.setLayout()

#---------------------------------------------------DISTRIBUCION UNIFORME---------------------------------------------------------
#----------------------------------------------Interfaz de distribucion UNIFORME--------------------------------------------------
class Formulario_Uniforme(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formulario')
        self.setGeometry(100, 100, 400, 300)

        # Crear los widgets
        self.num_muestra_label = QLabel('Tamaño de muestra:')
        self.intervalo_superior_label = QLabel('Limite Superior:')
        self.intervalo_inferior_label = QLabel('Limite Inferior:')
        self.cant_intervalo_label = QLabel('Cantidad Intervalos:')

        self.num_muestra_edit = QLineEdit()
        self.intervalo_superior_edit = QLineEdit()
        self.intervalo_inferior_edit = QLineEdit()
        self.cant_intervalo_edit = QLineEdit()

        self.guardar_btn = QPushButton('Generar')
        self.guardar_btn.clicked.connect(self.open_window_uniforme_stats)
       

        # Crear el layout
        layout = QGridLayout()
        layout.addWidget(self.num_muestra_label, 0, 0)
        layout.addWidget(self.num_muestra_edit, 0, 1)
        layout.addWidget(self.intervalo_superior_label, 2, 0)
        layout.addWidget(self.intervalo_superior_edit, 2, 1)
        layout.addWidget(self.intervalo_inferior_label, 3, 0)
        layout.addWidget(self.intervalo_inferior_edit, 3, 1)
        layout.addWidget(self.cant_intervalo_label, 4, 0)
        layout.addWidget(self.cant_intervalo_edit, 4, 1)
        layout.addWidget(self.guardar_btn, 5, 0, 1, 2)

        self.setLayout(layout)
        
        
    
    def open_window_uniforme_stats(self):
        n = int(self.num_muestra_edit.text())
        a = int(self.intervalo_inferior_edit.text())
        b = int(self.intervalo_superior_edit.text())
        cantIntervalos = int(self.cant_intervalo_edit.text())

        datos = {
            'Numero de muestra': n,
            'Varianza': 0,
            'Media': 0,
            'Desviacion Estandar': 0,
            'Lambda': 0,
            'Intervalo Superior': b,
            'Intervalo Inferior': a,
            'Cantidad intervalos': cantIntervalos
        }
        print(datos)
        self.new_window = Graficos_Uniforme(datos)
        self.new_window.show()    

#----------------------------------------------Grafico de distribucion UNIFORME-------------------------------------------------
class Graficos_Uniforme(QWidget):
    def __init__(self,datosEntrantes):
        super().__init__()
        self.setWindowTitle('Distribucion uniforme')
        self.setGeometry(100, 100, 400, 300)

        datosGenerados = generar_datos_Distribucion(2,datosEntrantes)
        vectorMC,vectorIIF_BASE,vectorFO_BASE,vectorFE_BASE,vectorDistribucionDensidad = uniformeBase(datosGenerados,datosEntrantes['Cantidad intervalos'])
        vectorIntervalosInicioFin,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado,gradosLibertad=uniforme(datosGenerados,datosEntrantes['Cantidad intervalos'])
        intervalo = int(len(vectorIIF_BASE)/2)
        
        # Crear los widgets
        tablaAleadorios = TablaIntervalos(vectorIIF_BASE,vectorMC,vectorFO_BASE,vectorDistribucionDensidad,vectorFE_BASE,10)

        tablaGeneral = TablaGeneral(datosGenerados)
        graficoNormal = Grafico(vectorFO_BASE,vectorMC,intervalo)
        tablaChi = TablaChiCuadrado(vectorIntervalosInicioFin,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado)
        pruebaChi = prueba_chi(3,intervalo,acumuladorCChiCuadrado)
                # Crear los widgets
        pruebaChi_label = QLabel(pruebaChi)

         
        # Crear el layout
        layout_texto = QGridLayout()
        layout = QHBoxLayout()
        layoutTablas = QVBoxLayout()
        layoutGrafico = QVBoxLayout()        
        layout.addWidget(tablaGeneral)
        layoutTablas.addWidget(tablaAleadorios)
        layoutTablas.addWidget(tablaChi)
        layoutTablas.addLayout(layout_texto)
        layoutGrafico.addWidget(graficoNormal)
        layout_texto.addWidget(pruebaChi_label, 0, 0)        

         
        # Crear el layout

        
        
        #layoutTablas.addWidget(tablaChi)
        layout.addLayout(layoutTablas)
        layout.addLayout(layoutGrafico)
    
        


        self.setLayout(layout)
        


        


        #self.setLayout()
        


#----------------------------------------------DISTRIBUCION EXPONENCIAL NEGATIVA------------------------------------------------
#--------------------------------------Interfaz de distribucion EXPONENCIAL NEGATIVA--------------------------------------------
class Formulario_Exponencial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Formulario')
        self.setGeometry(100, 100, 400, 300)

        # Crear los widgets
        #cuidado con esto
        self.num_muestra_label = QLabel('Tamaño de muestra:')
        self.lambda_label = QLabel('Lambda')
        self.cant_intervalo_label = QLabel('Cantidad Intervalos:')

        self.num_muestra_edit = QLineEdit()
        self.lambda_edit = QLineEdit()
        self.cant_intervalo_edit = QLineEdit()

        self.guardar_btn = QPushButton('Generar')
        self.guardar_btn.clicked.connect(self.guardar_datos)

        # Crear el layout
        layout = QGridLayout()
        layout.addWidget(self.num_muestra_label, 0, 0)
        layout.addWidget(self.num_muestra_edit, 0, 1)
        layout.addWidget(self.lambda_label, 1, 0)
        layout.addWidget(self.lambda_edit, 1, 1)
        layout.addWidget(self.cant_intervalo_label, 2, 0)
        layout.addWidget(self.cant_intervalo_edit, 2, 1)
        layout.addWidget(self.guardar_btn, 3, 0, 1, 2)

        self.setLayout(layout)
    def guardar_datos(self):
        n = int(self.num_muestra_edit.text())
        lamb = float(self.lambda_edit.text())
        cantIntervalos =  int(self.cant_intervalo_edit.text())
        
        datos = {
            'Numero de muestra': n,
            'Varianza': 0,
            'Media': 0,
            'Desviacion Estandar': 0,
            'Lambda': lamb,
            'Intervalo Superior': 0,
            'Intervalo Inferior': 0,
            'Cantidad intervalos':cantIntervalos
        }
        print(datos)

        self.new_window = Graficos_Exponencial(datos)
        self.new_window.show()

#--------------------------------------Grafico de distribucion EXPONENCIAL NEGATIVA--------------------------------------------
class Graficos_Exponencial(QWidget):
    def __init__(self,datosEntrantes):
        super().__init__()
        self.setWindowTitle('Distribucion exponencial')
        self.setGeometry(100, 100, 400, 300)

        datosGenerados =generar_datos_Distribucion(4,datosEntrantes)
        vectorMC,vector1,vectorIIF_BASE,vectorDistribucionDensidad,vectorFO_BASE,vectorFE_BASE,gradosLibertad = exponencialBase(datosGenerados,datosEntrantes['Cantidad intervalos'])
        vectorIntervalosInicioFin,vectorDensidad,vector3,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado,gradosLibertad=exponencial(datosGenerados,datosEntrantes['Cantidad intervalos'])
        intervalo = int(len(vectorIIF_BASE)/2)

         # Crear los widgets
        tablaAleadorios = TablaIntervalos(vectorIIF_BASE,vectorMC,vectorFO_BASE,vectorDistribucionDensidad,vectorFE_BASE,10)

        tablaGeneral = TablaGeneral(datosGenerados)
        graficoNormal = Grafico(vectorFO_BASE,vectorMC,intervalo)
        tablaChi = TablaChiCuadrado(vectorIntervalosInicioFin,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado)
        pruebaChi = prueba_chi(3,intervalo,acumuladorCChiCuadrado)
                # Crear los widgets
        pruebaChi_label = QLabel(pruebaChi)

         
        # Crear el layout
        layout_texto = QGridLayout()
        layout = QHBoxLayout()
        layoutTablas = QVBoxLayout()
        layoutGrafico = QVBoxLayout()        
        layout.addWidget(tablaGeneral)
        layoutTablas.addWidget(tablaAleadorios)
        layoutTablas.addWidget(tablaChi)
        layoutTablas.addLayout(layout_texto)
        layoutGrafico.addWidget(graficoNormal)
        layout_texto.addWidget(pruebaChi_label, 0, 0)
        
        #layoutTablas.addWidget(tablaChi)
        layout.addLayout(layoutTablas)
        layout.addLayout(layoutGrafico)
    
        


        self.setLayout(layout)
        

#----------------------------------------------------DISTRIBUCION POISSON--------------------------------------------------------    
#----------------------------------------------Interfaz de distribucion POISSON--------------------------------------------------    
class Formulario_Poisson(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Distribucion Poisson')
        self.setGeometry(100, 100, 400, 300)

        self.num_muestra_label = QLabel('Tamaño de muestra:')
        self.lambda_label = QLabel('Lambda:')
        self.cant_intervalo_label = QLabel('cantidad Intervalos:')

        
        self.num_muestra_edit = QLineEdit()
        self.lambda_edit = QLineEdit()
        self.cant_intervalo_edit = QLineEdit()
        self.guardar_btn = QPushButton('Generar')
        self.guardar_btn.clicked.connect(self.guardar_datos)
        
        # Crear el layout
        layout = QGridLayout()
        layout.addWidget(self.num_muestra_label, 0, 0)
        layout.addWidget(self.num_muestra_edit, 0, 1)
        layout.addWidget(self.lambda_label, 1, 0)
        layout.addWidget(self.lambda_edit, 1, 1)
        layout.addWidget(self.cant_intervalo_label, 2, 0)
        layout.addWidget(self.cant_intervalo_edit, 2, 1)
        layout.addWidget(self.guardar_btn, 3, 0, 1, 2)
        self.setLayout(layout)
        
    def guardar_datos(self):
        n = int(self.num_muestra_edit.text())
        lamb = int(self.lambda_edit.text())
        cantIntervalos = int(self.lambda_edit.text())
        
        datos = {
            'Numero de muestra':n,
            'Varianza': 0,
            'Media': 0,
            'Desviacion Estandar': 0,
            'Lambda': lamb,
            'Intervalo Superior': 0,
            'Intervalo Inferior': 0,
            'Cantidad intervalos': cantIntervalos
        }
        print(datos)
        self.new_window = Graficos_Exponencial(datos)
        self.new_window.show()


#----------------------------------------------Grafico de distribucion POISSON--------------------------------------------------
class Graficos_Poisson(QWidget):
    def __init__(self,datosEntrantes):
        super().__init__()
        self.setWindowTitle('Distribucion Poisson')
        self.setGeometry(100, 100, 400, 300)

        datosGenerados = generar_datos_Distribucion(1,datosEntrantes)
        vectorMC,vectorDistribucionDensidad,vectorIIF_BASE,vectorFO_BASE,vectorFE_BASE = poissonBase(datosGenerados,datosEntrantes['Cantidad intervalos'])
        vectorIntervalosInicioFin,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado,gradosLibertad=poisson(datosGenerados,datosEntrantes['Cantidad intervalos'])
        intervalo = int(len(vectorIIF_BASE)/2)
        
        # Crear los widgets
        tablaAleadorios = TablaIntervalos(vectorIIF_BASE,vectorMC,vectorFO_BASE,vectorDistribucionDensidad,vectorFE_BASE,10)

        tablaGeneral = TablaGeneral(datosGenerados)
        graficoNormal = Grafico(vectorFO_BASE,vectorMC,intervalo)
        tablaChi = TablaChiCuadrado(vectorIntervalosInicioFin,vectorFrecuenciaObservada,vectorFrecuenciaEsperada,vectorCChiCuadrado,acumuladorCChiCuadrado)
        pruebaChi = prueba_chi(3,intervalo,acumuladorCChiCuadrado)
                # Crear los widgets
        pruebaChi_label = QLabel(pruebaChi)

         
        # Crear el layout
        layout_texto = QGridLayout()
        layout = QHBoxLayout()
        layoutTablas = QVBoxLayout()
        layoutGrafico = QVBoxLayout()        
        layout.addWidget(tablaGeneral)
        layoutTablas.addWidget(tablaAleadorios)
        layoutTablas.addWidget(tablaChi)
        layoutTablas.addLayout(layout_texto)
        layoutGrafico.addWidget(graficoNormal)
        layout_texto.addWidget(pruebaChi_label, 0, 0)        
        
        #layoutTablas.addWidget(tablaChi)
        layout.addLayout(layoutTablas)
        layout.addLayout(layoutGrafico)
    
        


        self.setLayout(layout)
        


        


        #self.setLayout()


    

#------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear la ventana de la interfaz gráfica
    ventana = InterfazGrafica()
    ventana.show()

    # Ejecutar el bucle de eventos
    sys.exit(app.exec_())