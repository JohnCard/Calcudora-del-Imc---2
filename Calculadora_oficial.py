import math
# Variables a utilizar
abecedario = 'abcdefghijklmnñopqrstuvwxyz ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

numeros = '1234567890'

# Funciones a utilizar:

# Funcion para recorrer una variable:
def recorrer_cadena(cadena,variables):
    '''Esta funcion recorrera el parametro "cadena", y si en uno de caracteres detecta que no se encuentra en el parametro variables, se le aumentará un uno al cont,
    es decir, si encuentra un solo error significa que el "cont" que retorne será mayor a 0
    '''
    cont = 0
    for letra in cadena:
        if letra not in variables:
            cont += 1
    return cont
# Función para validar una respuesta 
def validar_respuesta(answer,tipo_variable,lista_variables):
    '''
    El trabajo de esta función es que su ciclo while no se dejará de repetir hasta que el usuario digite
    correctamente una serie de caracyeres que van de acuerdo a lo que se le pide, si por ejemplo se le
    pide un nombre, solo puede digitar letras en el abecedario y uno que otro espacio por si su nombre 
    es algo largo, y si pide una edad, solo se pueden digitar numeros.
    '''
    while((recorrer_cadena(answer,lista_variables) > 0) or (evaluar_variable(answer,'.') > 1) or (evaluar_variable(answer,' ') > 1)):
        answer = input(f'Su {tipo_variable} {answer} ¡ES INVÁLIDO!, favor de intentarlo de nuevo: ')
        
    return tipo_variable.capitalize()+': '+answer

# Función para verificar que un determinado parametro no se repita mas de una vez en una cadena:
def evaluar_variable(cadena,variable):
    '''
    Esta funcion recibe el parametro cadena, y en base a al parametro variable, esta función recorrerà el
    parametro cadena con un ciclo for y si detecta que el parametro "variable" se encuentra en la
    cadena, se le irà aumentando aun 1 al "cont" que inicializamos con 0
    '''
    cont = 0
    for letra in variable:
        if letra in cadena:
            cont += 1
    return cont

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
print('''
Se bienvenido al programa que te permite calcular tu Índeice de Masa Corporal 😁😎😝👦
''')
# le asignamos un valor a "answer" para que en el while de la linea 53 no lanze un ¡ERROR!
answer = 's'
while(answer == ('s' or 'S')):
    nombre = input('Digite su nombre: ')
    nombre = validar_respuesta(nombre,'nombre',abecedario)
    apellido_paterno = input('Digite su apellido paterno: ')
    apellido_paterno = validar_respuesta(apellido_paterno,'apellido paterno',abecedario)
    apellido_materno = input('Digite su apellido materno: ')
    apellido_materno = validar_respuesta(apellido_materno,'apellido materno',abecedario)
    edad = input('Digite su edad: ')
    edad = validar_respuesta(edad,'edad',numeros)
    peso = input('Digite su peso: ')
    peso = validar_respuesta(peso,'peso',numeros+'.')
    estatura = input('Ingrese su estatura: ')
    estatura = validar_respuesta(estatura,'estatura',numeros+'.')
    imc = float(peso[6:])/(math.pow(float(estatura[10:]),2))
    if(imc < 18.9):
        mensaje = 'Mensaje de conclusión: peso bajo'
    elif(imc >= 18.50 and imc <= 24.99):
        mensaje = 'Mensaje de conclusión: peso normal'
    elif(imc >= 25.00 and imc <= 29.99):
        mensaje = 'Mensaje de conclusión: sobrepeso'
    elif(imc >= 30.00 and imc <= 34.99):
        mensaje = 'Mensaje de conclusión: obesidad leve'
    elif(imc >= 35.00 and imc <= 39.99):
        mensaje = 'Mensaje de conclusión: obesidad media'
    elif(imc > 40.00):
        mensaje = 'Mensaje de conclusión: obesidad mórbida'
    imc = f'{float(peso[6:])/(math.pow(float(estatura[10:]),2)): .3f}'
    imc = f'Indice de masa corporal: {imc}'
    lista_atributos = [nombre,apellido_paterno,apellido_materno,edad,peso,estatura,imc,mensaje]
    mensaje_final = '\n|------------------------------------------------------------------------------------------|\n'
    for atributo in lista_atributos:
        matriz = '                                                                                   '
        mensaje_secundario = f'|\t{atributo}'
        for i in range(len(matriz)-len(atributo)):
            mensaje_secundario += ' '
        mensaje_secundario += '|\n'
        mensaje_final += mensaje_secundario
    mensaje_final += '|------------------------------------------------------------------------------------------|\n'
    print(mensaje_final)
    answer = input('Desea salir ya del programa?, o desea calcular otro indice de masa corporal (S/N)? ')
    while(answer != 'n' and answer != 's' and answer != 'N' and answer != 'S'):
        answer = input(f'La respuesta {answer} es ¡INVÁLIDA!, Digite su respuesta de nuevo (S/N): ')
        
print('El programa ha llegado a su final, muchas gracias. ')
