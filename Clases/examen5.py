###################Examen o quiz ###################################5 
#Pida a un usuario que ingrese sus 5 
#snacks favoritos y sus precios luego realice un gráfico de 
#barras con la información ingresada (recuerde poner titulo al 
#gráfico y a sus ejes también recuerde guardar el resultado en 
#un archivo png)
################################################## Solucion #############################################################
import matplotlib.pyplot as plt
def addele(a,r):
    D=[]
    P=[]
    i=0
    while i <=5:
        print(f"solo puede ingresar 5 veces datos y lleva {i+1}")
        D.append(input(a))
        P.append (float(input(r)))
pregunta ="Ingrese su dulce favorito: "
pregunta2 ="Ingrese el precio del Dulce: "
listadulces,listaprecios = addele(pregunta,pregunta2)
print(listadulces,listaprecios)
plt.bar(listadulces, listaprecios)
plt.show()
#####
P3="Ingrese su ciudad favorita: "
P4="Ingrese la poblacion: "
listaciuda, listapoblacion = addele(P3,P4)
print(listaciuda, listapoblacion)
plt.pie(listapoblacion, labels = listaciuda)
#######################################################
#Dada las dos señales biomédicas 
#enviadas junto con este examen, muestre en pantalla la 
#definición de cada prueba diagnóstica (investigue que es un 
#ecg y un ppg y muéstrelo en pantalla) luego dibuje los dos 
#gráficos (recuerde poner titulo al gráfico y a sus ejes también 
#recuerde guardar el resultado en un archivo png)
################################(  ECG )
import pandas as pd
import matplotlib.pyplot as plt

ecgDatos = pd.read_csv('ecgExamen.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print (ecgDatos.keys ())

muestras = list(ecgDatos['muestra'].values())
print (muestras)

valor = list(ecgDatos['valor'].values())
print (valor)

plt.plot(muestras, valor)
plt.title('Electrogardiograma')
plt.savefig('EcgExamen.png')
plt.show()

#################################### ( PPG )
import pandas as pd
import matplotlib.pyplot as plt

datosPpg = pd.read_csv ('ppgExamen.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print (datosPpg.keys())

muestras = list(datosPpg['muestra'].values())
print (muestras)
voltaje = list(datosPpg['valor'].values())
print (voltaje)

plt.plot(muestras, voltaje)
plt.title('Fotopletismografía Paciente Urgencias')
plt.xlabel('Tiempo (seg)')
plt.savefig('ppgExamen.png')
plt.show()


