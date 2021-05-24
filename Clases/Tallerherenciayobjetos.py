class mecanico ():
    '''
CARACTERISTICAS:
        Forma: tipo de persona precio: el precio del servicio Altura: altura del aparato*mostrarAtributos() muestra los atributos del usuario
    '''
    def __init__ (self,formaEntrada,precioEntrada,alturaEntrada):
        print ('Domicilio del mecanico')
        self.forma = formaEntrada
        self.precio = precioEntrada
        self.altura = alturaEntrada

    def mostrarAtributos (self):
        print (f'''
        {self.forma}
        con a precio {self.precio} y tiene {self.altura} cm de altura
        ''')
"PUNTO 2"
class clase ():
    def __init__ (self,edadEntrada,nombreEntrada,idEntrada,carreraEntrada,semestreEntrada):
        print ('soy un estudiante de primer semestre')
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestreEntrada = semestreEntrada
    def mostrarAspiracion (self,asignatura,tiempoEstudio):
        
        print (f'''
        Hola soy {self.nombre}, tengo {self.edad} y soy estudiante de {self.carrera}
        este semestre voy a ver {asignatura} y me tomará {tiempoEstudio} semanas cursarla
        ''')
"PUNTO 7"
class urologo ():
    def __init__ (self, edadEntrada,nombreEntrada,universidadEntrada):
        self.edad =edadEntrada
        self.nombre =nombreEntrada
        self.universidad = universidadEntrada
        print (f'soy {self.nombre}, egresado de la universidad {self.universidad} y hoy voy a calcular tu IMC, pero primero debes darme unos datos')
    def calcularimc (self,nombrePaciente):
        pesoIMC = int (input (f'{nombrePaciente}, ¿Cuál es tu peso actual?'))
        alturaIMC = float (input(f'{nombrePaciente}¿Cuanto mides en metros?'))
        print ('su IMC es de ' ,(pesoIMC/alturaIMC**2))
urologo1 = urologo (15,'jesus','EAFIT')
urologo1.calcularimc ('cesar')
torta1 = DIETA ('cuadrada','fresa',80)
torta1.mostrarAtributos ()
class Persona ():
    def __init__ (self, idEntrada, nombreEntrada, edadEntrada):
        print ('Hola, estoy a tu disposición')
        self.id = idEntrada
        self.nombre = nombreEntrada
        self.edad = edadEntrada
#Punto 1
    def hablar (self, mensaje):
        print (f'soy {self.nombre} y estoy aquí para ti')
    def caminar (self, cantidadPasos):
        for i in range (cantidadPasos):
            print (f'Hoy he caminado {i+1} pasos')
def linedesign(cantidad = 567, simbolo = '='):
        print (simbolo *cantidad)
        return None
#Herencia 
class Doctor (Persona):
    def __init__(self,idEntrada,nombreEntrada, edadEntrada,especialidadEntrada):
        Persona.__init__(self, idEntrada,nombreEntrada,edadEntrada)
        self.especialidad = especialidadEntrada
    def tratarEnfermedad (self, enfermedad):
        print (f'''Hola, soy {self.nombre}
                especialista en {self.especialidad} y procedo a 
                tratar la {enfermedad} que aqueja al paciente
        ''')
class medico (Persona):
    def _init_ (self,idEntrada,nombreEntrada,edadEntrada,universidadEntrada):
        Persona.__init__(self,idEntrada,nombreEntrada,edadEntrada)
        self.universidad = universidadEntrada
    def calcularimc (self,alturaEntrada,pesoEntrada):
        pesoIMC = int (input ('¿Cuál es tu peso actual?'))
        alturaIMC = float (input('¿Cuanto mides en metros?'))
        print ('su IMC es de ' ,pesoIMC/(alturaIMC**2))
    def presentarse (self, texto1):
        print (f'soy {self.nombre}, tu nutricionista y hoy voy a calcular tu IMC, pero primero debes darme unos datos')
"Punto 4"
class inspector (Persona):
    def __init__(self,idEntrada,nombreEntrada, edadEntrada,especialidadDerecho,universidadAtributo):
        Persona.__init__(self, idEntrada,nombreEntrada,edadEntrada)
        self.especialidadAbogado = especialidadDerecho
        self.sobreMiU = universidadAtributo
    def representar (self,nombre,caso):
        print (f'Soy el abogado {self.nombre} y procedo a representar al  {nombre} en su caso de {caso}')
estudiante1 = Persona (934853583,'jacobo',14)
estudiante1.hablar ('mensaje')
estudiante1.caminar (42)
linedesign (20, '.......')
especialista1 = Doctor (129218311,'fernando',65,'neurologo')
especialista1.tratarEnfermedad ('Miocardiopatía')
linedesign (7, '.......')
medico1 = medico (99678,'fredo',67)
medico1.presentarse ('.')
medico1.calcularimc (2,4)
linedesign (7, '.......')
inspector1 = inspector (24342434,'sergio',83,'gestionador de casos','tutela')
inspector1.representar ('ARES','violencia')
