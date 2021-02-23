
def trigli (t):
    if t < 150:
        print(f"{t} mg/dl es optimo")
    elif t>=150 and t<=199:
        print(f"{t} esta sobre el limite (mg/dl )")
    elif t>=200 and t<=499:
        print(f"{t} Esta  Alto (mg/dl )")
    elif t>=500:
        print(f"{t} Esta Demaciado Alto (mg/dl )")
    else:
        print("ERROR 00")


def homocis (u):
    if u >= 2 and u<=15:
        print(f"{u} entre 2 y 15 Umol/L es optimo")
    elif u>=15 and u<=30:
        print(f"{u} esta sobre el limite ( Umol/L)")
    elif u>=30 and u<=100:
        print(f"{u} esta alto ( Umol/L)")
    elif u>100:
        print(f"{u} muy alto ( Umol/L)")
    else:
        print("ERROR 00")




print("""
1. Trigliceridos
2. Homocisteina
""")

Eleccion = (input("seleccione una opcion : ")) 


if Eleccion == "1":
    X= int(input("Ingrese el nivel de trigliceridos: "))
    trigli(X)



elif Eleccion== "2":
    Y=int(input("Ingresa el nivel de homocisteina: "))
    homocis(Y)

else:
    print("ERROR")


respuesta=input(str("Quieres volver a repetir ? : "))


while(respuesta=="si"):
    respuesta=input(str("Quieres volver a repetir ? : "))


    print("""
1. Trigliceridos
2. Homocisteina
""")

    Eleccion = (input("seleccione una opcion : ")) 


    if Eleccion == "1":
        X= int(input("Ingrese el nivel de trigliceridos: "))
        trigli(X)

    elif Eleccion== "2":
        Y=int(input("Ingresa el nivel de homocisteina: "))
    homocis(Y)









