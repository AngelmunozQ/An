

def sum (num1, num2):
    print(num1+num2)
def mult (num1,num2):
    print(num1*num2)
def divi (num1,num2):
    print(num1/num2)
def res (num1,num2):
    print(num1-num2)

print("""
1. Suma
2. Multiplicacion
3. Division
4. Resta
""")

Eleccion = (input("seleccione una opcion : ")) 

if Eleccion == "Suma":
    x = int(input("ingresa numero : "))
    y = int(input("ingresa numero : "))
    sum(x,y)

elif Eleccion == "Multiplicacion":
    x = int(input("ingresa numero: "))
    y = int(input("ingresa numero: "))
    mult(x,y)

elif Eleccion == "Division":
    x = float(input("Ingresa numero: "))
    y = float(input("Ingresa numero: "))
    divi(x,y)

elif Eleccion == "Resta":
    x = int(input("Ingresa numero: "))
    y = int(input("ingresa numero: "))
    res(x,y)

else:
    print("Opcion no es valida")


Respuesta = str(input("Quiere volver a repetir el ciclo ?: "))
while (Respuesta == "si"):
    Respuesta = str(input("Quiere volver a repetir el ciclo ?: "))
    print("""
1. Suma
2. Multiplicacion
3. Division
4. Resta
""")

    Eleccion = (input("seleccione una opcion : ")) 

    if Eleccion == "Suma":
        x = int(input("ingresa numero : "))
        y = int(input("ingresa numero : "))
        sum(x,y)

    elif Eleccion == "Multiplicacion":
        x = int(input("ingresa numero: "))
        y = int(input("ingresa numero: "))
        mult(x,y)

    elif Eleccion == "Division":
        x = float(input("Ingresa numero: "))
        y = float(input("Ingresa numero: "))
        divi(x,y)

    elif Eleccion == "Resta":
        x = int(input("Ingresa numero: "))
        y = int(input("ingresa numero: "))
        res(x,y)

    else:
        print("Opcion no es valida")

