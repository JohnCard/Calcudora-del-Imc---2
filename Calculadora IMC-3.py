import math
from pickle import FALSE

def regs(param_prim, param_seg,):
    try:
        float(param_prim)
    except:
        while((str.isnumeric(param_prim) == False) or (('.' not in param_prim) == True)):
            param_prim = input(f'Ingrese nuevamente su {param_seg} por favor: ')
    finally:
        return float(param_prim)
 
''' 
Aqui definiremos otra función, la cual será usada en el
transcurso del formulario para pedir tipos de datos numericos o asegurarse de que no queden vacios
'''
def regs_dos(num, numero_parametro):
    try:
        int(num) 
    except:
        while((str.isdigit(num) == False) or (len(num) == 0)):
            num = input(f'Ingrese nuevamente su {numero_parametro} por favor: ')
    finally: 
        return int(num) 

''' 
Aqui definiremos la funcion que nos permitirá saber si un dato es de tipo caracter (string o str),
poque de lo contrario imprimira un error
'''
def regs_tres(pram, pram_do):
    while((pram.isdigit()) or (len(pram) == 0)):
            pram = input(f'Ingrese correctamente su {pram_do} porfavor o no podremos continuar: ')
    return pram

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
if((nombre_usuario.isdigit()) or (len(nombre_usuario) == 0)):
    nombre_usuario = regs_tres(nombre_usuario, 'Nombre')

apellido_paterno = input('Ingrese su apellido paterno (solo el paterno): ')
if((apellido_paterno.isdigit()) or (len(apellido_paterno) == 0)):
    apellido_paterno = regs_tres(apellido_paterno, 'Apellido paterno')

apellido_materno = input('Ingrese su apellido materno (solo el materno): ')
if((apellido_materno.isdigit()) or (len(apellido_materno) == 0)):
    apellido_materno = regs_tres(apellido_materno, 'Apellido Materno')

edad = input('Ingrese su Edad: ')
edad = regs_dos(edad, 'Edad')

peso = input('Ingrese su peso: ')
if(('.' not in peso) or (str.isdigit(peso) == False) or (len(peso) == 0)):
    peso = regs(peso,'Peso')

estatura = input('Ingrese su estatura: ')
if(('.' not in estatura) or (str.isdigit(estatura) == False) or (len(estatura) == 0)):
    estatura = regs(estatura, 'Estatura')

imc = (peso)/(math.pow(estatura,2))

# Devolviendo todos los datos ingresados por el usuario: 
print(f'''
Nombre: {nombre_usuario}
Apellido paterno: {apellido_paterno}
Apellido materno: {apellido_materno}
Edad: {edad}
Peso: {peso}
Estatura: {estatura}
Indice de Masa Corporal: {imc}
''')