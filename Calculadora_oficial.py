# Variables a utilizar
si_no = ['n','N','s','S']

abecedario = ' abcdefghijklmnñopqrstuvwxyz ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

numeros = '1234567890 '

numeros = 

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
# Función para validar una respuesta que solo puede valor uno de los 4 valores siguientes: N,n,s y S
def validar_respuesta(answer,tipo_variable,lista_variables):
    while(recorrer_cadena(answer,lista_variables) > 0):
        answer = input(f'Su {tipo_variable} {answer} ¡ES INVÁLIDA!, favor de intentarlo de nuevo ({lista_variables}): ')
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
        # ¡PENDIENTE!
        peso = validar_respuesta(peso,'peso',)

