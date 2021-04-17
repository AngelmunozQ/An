#1
"""def Calcu (num1,num2,num3):
    Z=(num1*num2*num3)
    f=(num1/num2/num3)
    W=(num1**num2**num3)
    print(f"{Z},{f},{W}")


print("""
#1. Multiplicacion,Potencia y Division. 
#2.Salir
""")

Eleccion = (input("seleccione una opcion : ")) 

if Eleccion == "1":
    a = int(input("ingresa numero : "))
    y = int(input("ingresa numero : "))
    p = int(input("ingrese numero:  "))

    Calcu(a,y,p)

else:
    (print("Adios"));"""

#3
""""def triangulo (r1,r2):
    J=(r1*r2/2)
    print(J)

print("Ingresa la base y altura del triangulo para calcular el AREA.")
i=float(input("Ingresa base: "))
k=float(input("ingresa Altura: "))
triangulo(i,k)"""

#2
"""def list ():
    lista1=[1,3,4]
    lista2=[3,4,3]
    lista3=[3,2,1]
    print(f"{lista1},{lista2},{lista3}");"""

#4
"""AB= [36,37,38,35,36,38]
def encontrar ():
    print("Elemento mayor", max(AB))
    print("Elemento menor",min(AB))
    suma=0
    for i in AB:
        suma+=i
    promedio =suma/6
    print(promedio)"""

#5
def fib(n):
    a=0
    b=1
    l1=[fib]
    while a<n:
        print(a,end="")
        a=b
        b=a+b
    print()
fib(100000000000000000)






