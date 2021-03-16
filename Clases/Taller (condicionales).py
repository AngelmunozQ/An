#Dado dos numeros determine si son iguales o cual es el mayo
"""x = int(input("Ingrese el numero : "))
y = int(input("Ingrese el numero : "))
if x>y:
    print(f"[x] mayor a [y]")
elif x<y:
    print(f"[y] mayor a [x]")
elif x==y:
    print(f"[x] igual a [y]")
else:
    print("no es invalida")"""

#Pida la edad del usuaria y muestre en pantalla la siguiente informacion:
# Si tiene menos de 18 años diga que es menor de edad
#Desde 18 hasta 25 es joven
#Desde 26 hasta 60 Adulto
#Mayor a 60 años es Adulto Mayor

"""Edad = int(input("Que edad tienes : "))
if Edad<=18:
    print("Tu eres menor de edad")
elif Edad>=18 and Edad<26:
    print("Estas joven campeon")
elif Edad>=26 and Edad<61:
    print("Adulto")
else: 
    print("Adulto mayor")"""

#Escriba un programa que pida el año actual y un año cualquiera 
#y que escriba cuantos años han pasado desde ese año a cuantos años faltan para llegar a ese año.
"""def operacion (Añoactual,Año2):
    resultado=Añoactual-Año2
    print(resultado)
Añoactual= int(input("Dame el año actual: "))
Año2=int(input("Dame el año a calcular: "))
if Añoactual>=0 and Añoactual>Año2:
    x = Añoactual
    y = Año2
    operacion(x,y)
    print(f"{y} le faltan {Añoactual-Año2} años para llegar a {x} ")
elif Añoactual>=0 and Año2>Añoactual:
    x = Añoactual
    y = Año2
    print(f" desde {x} faltan {Año2-Añoactual} años para {y}")
else:
    ("ERROR 044")"""

#Escriba un programa que pida una distancia en centimetros
#y que escriba esa distancia en kilometros,metros y centimetros (escribiendo todas las unidades)

"""T = int(input("dame la distancia en centimentros: "))
resultado=""
if T>=1:
    print(f"{T/100} M, {T/1000} KM, {T} CM")
else:
    print("ERROR 044")"""

print("""
1.Ingresar costos del usuario
2.Agregar
3.Elimina
4.Descuento
""")








