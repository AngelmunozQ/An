"""x=int(input("DAME EL ELEMENTO: "))
y=str(input("DAME UN NOMBRE: "))
u=float(input("INGRESEME EL DECI: "))
lista=[x,y,u]
print(lista)
Usuario=str(input("Quieres Agregar algo a la lista ?: "))
while (Usuario=="si"):
    Usuario=str(input("Quieres Agregar algo a la lista ?: "))
    aggusuario=str(input("agrega un usuario a la lista: "))
    lista.append(aggusuario)
    print(lista)"""

#LEER NUMEROS ENTEROS DE TECLADO, HASTA QUE EL USUARIO INGRESE EL 0.Finalamente,mostrar la sumatoria de todos
#los numeros ingresados.
"""suma=0
numeros=int(input("Dame NUMEROS: "))
lista=[numeros]
while(numeros!=0):
    numeros=int(input("Dame NUMEROS: "))
    if numeros!=0:
        lista.append(numeros)
    else:
        for numeros in lista:
            suma += numeros
        lista=[numeros]
        print(suma)
        break"""
#Programa que pida dos numeros enteros. El pograma pedira de nuevo el segundo numero
#mientras no sea mayor que el primero. El programa Terminara escribiendo los dos numeros.
""""num1= int(input("Dame un numero: "))
num2=int(input("Dame otro numero: "))
while(num1>num2):
    pre= int(input("Dame otro numero: "))
    if pre>num1:
        print(f"{num1} y {pre}");break"""
#Escriba un programa que pida numeros enteros que sean cada vez mas grandes.
"""num1= int(input("Numero: "))
num2=int(input("Numero: "))
while(num1>=num2):
    print(f"{num2} no es mayor que el {num1}");
    num2= int(input("Intentalo otra vez: "))"""

#Crear un programa que permita al usuario ingresar los costos de las compras de 
#un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar 
#en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el 
#monto 0................................
#Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un 
#nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las 
#ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

"""total=0
monto=float(input("Monto de una venta: $"))
while monto!=0:
    if monto<0:
        print("Monto no válido.")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))
if total>1000:
    total-=total*0.1
print("Monto total a pagar: $", total)"""

#Permitir que el usuario ingrese C para mostrar la lista en pesos 
#colombianos dólares notifique que no es necesaria una conversión, D en 
#dólares (se sabe que un peso es 0,00027 dolares) y E para convertir en 
#euros (se sabe que un peso es 0,00023 euros). En caso de que el usuario 
#ingrese una letra diferente notifíquele que ingreso una entrada no válida y 
#regrese al menú principal. 
#Permita que el usuario agregue un nuevo valor a la lista, al final muéstrela

listaPesos = [20000,30000,4000,2500,1000,7600]

conversionpesosc=("No es necesario la lista ya esta en pesos colombianos")
conversionesdolares= ("Esta seria la conversion de pesos colombianos a dolares")
conversionesaeuros=("Esta seria la convercion de Euros a pesos colombianos")
letradiferente=("lo sentimos a cometido un error")   

print("""
1.  Quieres ver la lista en Pesos colombianos.
2.  Quieres ver la lista en Euros. 
3.  Quieres ver la lista en Dolares.
""")

eleccion= (input("Selecciona una opcion por favor: "))

while(eleccion!=4):

    if eleccion=="1":
        print(listaPesos)
        print(conversionpesosc)

        print("""
        A.  Agregar a la lista
        B.  Eliminar de la lista
        C.  Ver maximo,minimo y promedio.
        """)

        eleccion1=(input("Selecciona una letra: "))

        if eleccion1=="A":
            x=1
            while(x!=0):
                x=float(input("Agregue el elemento: "))
                listaPesos.append(x)
                print(listaPesos)

        elif eleccion1=="B":
            i=int(input("elemento a eliminar: "))
            listaPesos.pop(i)
            print(listaPesos)






    elif eleccion=="2":
        listaeuros=[]
        for i in listaPesos:
            conversor = round(i*0.00023,2)
            listaeuros.append(conversor)
            print(listaeuros)
            print(conversionesaeuros)
    elif eleccion=="3":
        listadolares=[]
        for i in listaPesos:
            conver=round(i*0.00027,3)
            listadolares.append(conver)
            print(listadolares)
            print(conversionesdolares)
    else:
        print("ERROR")
    eleccion= (input("Selecciona una opcion por favor: "))

