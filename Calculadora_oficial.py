print()
# Variables a utilizar
si_no = ['n','N','s','S']

abecedario =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

numeros = '1234567890 '

# Función para validar una respuesta que solo puede valor uno de los 4 valores siguientes: N,n,s y S
def validar_respuesta(answer,tipo_variable,lista_variables):
    while(answer not in lista_variables):
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
        edad = input('Digite su edad: ')
        edad = validar_respuesta(edad,'edad',numeros)

