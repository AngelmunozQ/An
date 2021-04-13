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

#################################################################################################################
#Funciones, hacer taller.
##############################################################
#crear clase de animal. #estudiar examen



