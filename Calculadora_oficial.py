# Variables a utilizar
si_no = ['n','N','s','S']

abecedario = ' abcdefghijklmnñopqrstuvwxyz ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

numeros = '1234567890'

numeros_decimales = '1234567890.'

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
        answer = input(f'Su {tipo_variable} {answer} ¡ES INVÁLIDA!, favor de intentarlo de nuevo ({lista_variables}): ')
# Función para verificar que un determinado parametro no se repita mas de una vez en una cadena:
def evaluar_variable(cadena,variable):
    '''
    Esta funcion recibe el parametro cadena, y en base a al parametro variable, esta función recorrerà el
    parametro cadena con un ciclo for y si detecta que el parametro "variable" se encuentra en la
    cadena, se le irà aumentando aun 1 al "cont" que inicializamos con 0
    '''
    cont = 0
    for letra in cadena:
        if variable in cadena:
            cont += 1
    return cont

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
print('''
Se bienvenido al programa que te permite calcular tu Índeice de Masa Corporal 😁😎😝👦
''')
while(answer != 'n'):
    # answer = input('Para empezar, esta usted interesado en conocer su IMC?, si desea salir del programa, solo debe oprimir "N": ')
    # answer = validar_respuesta(answer)
    if(answer == ('s' or 'S')):
        nombre = input('Digite su nombre: ')
        nombre = validar_respuesta(nombre,'nombre',abecedario)
        apellido_paterno = input('Digite su apellido paterno: ')
        apellido_paterno = validar_respuesta(apellido_paterno,'apellido paterno',abecedario)
        apellido_materno = input('Digite su apellido materno: ')
        apellido_materno = validar_respuesta(apellido_materno,'apellido materno',abecedario)
        edad = input('Digite su edad: ')
        edad = validar_respuesta(edad,'edad',numeros)
        peso = input('Digite su peso: ')
        peso = validar_respuesta(peso,'peso',numeros_decimales)
        peso = float(peso)
        estatura = input('Ingrese su estatura: ')
        estatura = validar_respuesta(estatura,'estatura',numeros_decimales)
        estatura = float(estatura)
        imc = peso/(math.pow(estatura,2))
        print(f'''
        Nombre: {nombre}
        Apellido Paterno: {apellido_paterno}
        Apellido Materno: {apellido_materno}
        Edad: {edad}
        Peso: {peso}
        Estatura: {estatura}
        Índice de masa corporral: {imc}
        ''')
    print('Digite un 1 para continuar en el programa o un 2 para salir del programa! ')
    answer = input('Desea salir ya del programa?, o desea calcular otro indice de masa corporal? ')
    