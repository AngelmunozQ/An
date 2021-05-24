#PUNTO #1#
def calcu (a,b,name):
    IMC=a/b**2
    if a and b < 0:
        print("por favor verifique lo que ingreso")
    elif  b == int:
        print("Por favor ingrese un numero float")
    elif a == float:
        print("Por favor ingrese un numero entero")
    elif name == int or float:
        print("Recuerde que es importante que dijite su nombre")
    else:
        a and b == 0
        print ("Los numeros no son calculables")
    print(IMC)
    return name, IMC

def largo(contenido):
    contenido=parrafo
    palabras=contenido.split()
    print("Cantidad de palabras", len(palabras))
    i=0
    for i in range(1, len(palabras)):
            print("elemento mayor", max(parrafo))
            print("elemento menor", min(parrafo))

pregunta= "Quieres volver a repetir el ciclo ?: "
print("""
1.Calcular IMC
2.Corregir Parrafo
3.Almacenamiento
""")
eleccion=input("Ingrese una opcion valida: ")
while (eleccion >= 1 and eleccion <= 3 and pregunta=="si"):
    if eleccion=="1":
        a=input(int("Dame un numero entero en KG: "))
        b=(input(float("Dame una estatura: ")))
        calcu(a,b)

    elif eleccion=="2":
        parrafo=input(str("Ingresa un texto de el tema que quiera, recuerde que el texto debe terminar en punto final: "))
        largo(parrafo)

    elif eleccion=="3":
        with open("RUTA/texto.txt","w") as matenimiento:
            matenimiento.write()

    else:
        print(pregunta)
