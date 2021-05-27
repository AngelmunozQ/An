from matplotlib import pyplot

def alimentosfavoritos(a,r):
    lista1=[]
    lista2=[]
    i=0
    while i <=8:
        print(f"solo puede ingresar 8 veces datos y lleva {i+1}")
        lista1.append(input(a))
        lista2.append (float(input(r)))
pregunta ="Ingrese su dulce favorito: "
pregunta2 ="Ingrese el precio del Dulce: "
listadulces,listaprecios = alimentosfavoritos(pregunta,pregunta2)
print(listadulces,listaprecios)
print.title("Dulces favoritos y sus precios")
pyplot.bar(listadulces,listaprecios, width=0.5)
pyplot.show
pyplot.savefig("Grafica.png")

###################################################################-1-
def validateFloat(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = float (input(pregunta))
            isCorrectData = True
        except ValueError:
            print('datos incorrectos ingrese nuevamente')
        return valor 
def validateString(pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.isalpha())
            isCorrectData = True
        except AssertionError:
            print('datos incorrectos ingrese nuevamente')
        return valor 
def datos ():
    pregunta1= "Ingrese su nombre: "
    pregunta2= "Ingrese su dinero en dolares: "
    nombre=validateString(pregunta1)
    dolares=validateFloat(pregunta2)
    return nombre, dolares

def calculardinero():
    nombreIn, dolaresIn = datos()
    conversion= dolaresIn*0.82
    return nombreIn, conversion

conversion, nombreIn=calculardinero()
print(nombreIn,conversion)
print(f"tu nombre es {nombreIn} y tu dinero en euros es {conversion} esta es la exchange rate actualmente 27-05-2021")
####################################################################-3-

def Bucandoarchivo(nombreArchivo, descripcion):
    try:
        archivo = open(nombreArchivo)
        return True
    except FileNotFoundError:
        archivo = open(nombreArchivo, 'Neurologia', encoding='UTF-8')
        print("2")
        archivo.writelines(descripcion)
        return False

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open(nombreArchivo,'Neurologia, pacientes,descripcion de la enfermedad y precio de consulta. ')
    archivo.writelines(lineaIn)

    nameFile = "Neurologia.txt"
    isValidate = Bucandoarchivo(nameFile, 'Seguimiento de pacientes con un estado neurologico afectado')
    if (isValidate):
        estadopaciente= input('Ingrese la descripción del estado neurologico del paciente : ')
        nombrep = validateString('Ingrese el nombre del paciente :')
        precioc = validateFloat('Ingrese el precio de consulta : ')
        linea ='\nDescripcion'+ estadopaciente+ ' nombre técnico: ' + nombrep + ' precio acordado: '+ str(precioc)
    guardarLinea(nameFile, linea)
else: print("se creó el archivo")
#########################################################################-4- 

class Humano:
    def __init__(self,edad,sexo,nombre):
        self.edad = 26
        self.nombre = "Daniel de Jesus Toro Hernandez"
        self.sexo = "Masculino"
    def hablar(self,mensaje):
        print(mensaje)
Daniel=Humano()
print(f"Hola, soy {Daniel.nombre} tengo {Daniel.edad} y mi genero es {Daniel.sexo}")
Daniel.hablar("Me gusta viajar y conocer el mundo")

class Doctor(Humano):
    def saludpublica(self,especialista):
        print("Voy a calcular tu IMC amiguito porque soy especialista en", especialista)
    def calcular(peso,altura):
        peso=float(input("Dame tu masa corporal en KG: "))
        altura=input("Dame tu altura en CM: ")
        IMC=peso/altura**2
        print(IMC)
Doctor.saludpublica("Nutriologo")
#####################################################-2-