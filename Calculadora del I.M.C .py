# Inicialización del Programa, Calculo del IMC: 

# Definiendo funciones:
def regs(param):
    if(len(param) == 0): 
        while(len(param) == 0):
            param = input(f'Ingrese el dato{param} faltante nuevamente porfavor: ')

'''
¡---DISTINTOS ERROES A PREVENIR---!
● Comenzar con letras o guion bajo, no números.
● Sin espacios y sin símbolos, solo guion bajo.
● Son sensitivas a minúsculas y mayúsculas.
● Nombrarlas en minúsculas.
● No palabras reservadas.
● No usar acentos
'''

# Inicialización del Formulario: 
nombre_usuario = input('Ingrese su Nombre: ')
regs(nombre_usuario)

apellido_paterno = input('Ingrese su apellido paterno (solo el paterno): ')
apellido_materno = input('Ingrese su apellido materno (solo el materno): ')
edad = input('Ingrese su Edad: ')
try:
    int(edad) 
except ValueError as errF01:
    while(type(edad) != int):
        edad = input('Ingrese nuevamente su edad porfavor: ')
        if(type(edad == int)): break
    
    
# if(type(edad) == 'str'):
#     while(type(edad) != 'int'):
#             edad = input('Intente ingresar nuevamente su edad: ')
    
# elif(type(edad) == 'int'): 
#     exit()
    
peso = input('Ingrese su Peso: ')
estatura = input('Ingrese su Estatura: ')
imc = (peso)/(estatura)^2