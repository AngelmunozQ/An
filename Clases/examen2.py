TC = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]


print("""
1. F
2. K
3. C
4. Salir del programa
""")

E=input("Eleccion: ")

while(E!=5):

    if E=="1":
        l1=[]
        for i in TC:
            Conver=round((i*9/5)+32,2)
            l1.append(Conver)
        print(l1)

    elif E=="2":
        l2=[]
        for i in TC:
            Conver=round(273+i,2)
            l2.append(Conver)
        print(l2)

    elif E=="4":
        print("Adios")
        break

    elif E=="3":
        print("la lista ya esta en grados C")
        print(TC)

        print("""
        A.Temperaturas
        B.Maxima Temperatura
        C.Minima Temperatura
        """)
        o=input("Seleccione una letra: ")

        
        if o=="A":
            x=1
            lista3=[]
            while x!=0:
                x=float(input("Temperatura: "))
                lista3.append(x)
                if x<36.6:
                    print("Hipotermia")
                elif x>37.6:
                    print("Fiebre")
                elif x>=36 and x<=37:
                    print("Normal") 
                print(lista3)

            print("Ingrese 0 para retornar al menu principal 1.F , 2.K , 3.C , 4.SALIR DEL PROGRAMA, ")

        elif o=="B":
            print("Elemento mayor", max(lista3))
        
        elif o=="C":
            print("Elemento menor", min(lista3))  


    else:
        print("ERROR CX0045 ")
    E= input("Ingrese una opcion valida: ")

    
