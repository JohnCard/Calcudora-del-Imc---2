# Todas estas variables fueron creadas con el proposito de que las distintas funciones declaradas hacia
# abajo puedan leerlas y devolver distintas conclusiones dependiendo de los datos datos a estudiar, para 
# saber si el usuario introduce un digito que no tenga sentido o escriba algo por error
rb = 'ZXCVBNMASDFGHJKLÑQWERTUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbnmasdfghjklñqwertuiop 1234567890.'
rt = 'ZXCVBMASDFGHJKLÑQWERTUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbmasdfghjklñqwertuiop 1234567890.'
c = 'ZXCVBNMASDFGHJKLÑQWERTYUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbnmasdfghjklñqwertyuiop'; b = '1234567890.'
a = 'ZXCVBNMASDFGHJKLÑQWERTYUIOPzxcvbnmasdfghjklñqwertyuiop '; d = '¨¨+*~[]^``/|¬°!"#$%&()=-_;:1234567890.'

# Esta función fue creada para cuando llegase el momento de pedirle al usuario si esque desea saber o no
# su imc y en el caso de que si, al terminar, preguntarle por si gusta calcular otro mas, aunque tambien esta 
# modificada para el caso de si el usuario ingresa una respuesta invalida
def ley_params(answer_seg):
    while(answer_seg == 'y' or answer_seg == 'Y' or len(answer_seg) == 0 or tir_seg(answer_seg) > 0 or ('yy' in answer_seg) or ('YY' in answer_seg) or ('nn' in answer_seg) or ('NN' in answer_seg)):
        if(answer_seg == 'y' or answer_seg == 'Y'):
            CalC_IMC()
            answer_seg = input('\n Desea calcular otro indice (Y/N): ')
        elif(tir_seg(answer_seg) > 0 or ('yy' in answer_seg) or ('YY' in answer_seg) or ('nn' in answer_seg) or ('NN' in answer_seg)):
            answer_seg = input('Respuesta ¡INCORRECTA!, desea intentarlo de nuevo (Y/N): ')
        elif(len(answer_seg) == 0):
            answer_seg = input('No se digito nada, desea intentarlo de nuevo (Y/N): ')
    else:
        print('''\n Usted ha llegado al Final del Programa
\n''')
        
# Esta función fue creada con el proposito de que, ya que como en un principio, explicamos que hay 
# variables con distintos digitos para ser estudiadas por otras funciones y evitar que el usuario pase por alto 
# algun error, con lo que si llega a ingresar tansolo un digito que se encuentre en estas variables
# de arriba a estudiar por las distintas funciones, se incrementará en uno lo que devuelva el return y asi,
# mientras se cumpla la condicion de que lo que devuelva sea mayor a 0, quiere decir que ingreso algo mal
def leer_params(pirm, let):
        ty = 0
        for hj in pirm:
            if(let.find(hj) >= 0):
                ty += 1
        return ty

# El campo de estudio para esta función será la variable "rt" 
def tir_seg(ull_seg):
    return leer_params(ull_seg,rt)

# El campo de estudio para esta función será la variable "b"
def hall(letter):
    return leer_params(letter,b)

# El campo de estudio para esta función será la variable "c"
def hall_seg(letter_seg):
    return leer_params(letter_seg, c)

# Esta función se llamará para evitar que en el peso o estatura, el usuario no pueda digitar mas de un 
# solo punto
def hall_ter(letter_ter):
    ag = 0
    for t in letter_ter:
        if(t == '.'):
            ag += 1
    return ag

# El campo de estudio para esta función será la variable "a"
def hall_curt(letter_curt):
    return leer_params(letter_curt, a)

# El campo de estudio para esta función será la variable "d"
def hall_quint(letter_quint):
    return leer_params(letter_quint, d)

# Esta función fue creada para que el usuario estrictamente solo pueda agregar ya sean numeros enteros 
# o flotantes en el peso y la estatura, ya que de lo contrario, le preguntará hasta que ingrese el 
# dato correctamente
def regs(param_prim, param_seg):
    
    while(((hall(param_prim)) == 0) or ((hall_seg(param_prim)) > 0) or ((hall_ter(param_prim)) > 1) or (' ' in param_prim)):
            param_prim = input(f'Ingrese nuevamente su {param_seg} por favor: ')
    return float(param_prim)

# Esta función fue creada para que el usuario suba estricta y solamente datos enteros en su edad
def regs_dos(num, numero_parametro):
    while((num.isnumeric() == False) or (' ' in num)):
            num = input(f'Ingrese nuevamente su {numero_parametro} por favor: ')
    return int(num) 

# Esta función fue creada para que el usuario solo pueda ingresar letras y un solo espacio por si
# su nombre es algo largo o para los apellidos
def regs_tres(pram, pram_do):
    while(((hall_curt(pram)) == 0) or ((hall_quint(pram)) > 0) or ('  ' in pram) or (pram.startswith(' '))):
        pram = input(f'Ingrese correctamente su {pram_do} porfavor o no podremos continuar: ')
    return pram

'''
Aqui se encontraría la función principal que como objetivo tiene llamar a las demas funciones declaradas 
por arriba para usarlas en su correcto orden para lo que es desde el nombre hasta la estatura 
para aqui mismo calcular el IMC y mostrarlo todo por consola en esta misma funcion ( "CalC_IMC()" )
'''
def CalC_IMC():
    import math
    '''
    ¡---DISTINTOS ERROES A PREVENIR---!
    Para la declaración de variables: 
    ● Comenzar con letras o guion bajo, no números.
    ● Sin espacios y sin símbolos, solo guion bajo.
    ● Son sensitivas a minúsculas y mayúsculas.
    ● Nombrarlas en minúsculas.
    ● No palabras reservadas.
    ● No usar acentos.
    '''
    # Inicialización del Formulario: 
    nombre_usuario = input('\n Ingrese su Nombre: ')
    nombre_usuario = regs_tres(nombre_usuario, 'Nombre')

    apellido_paterno = input('\n Ingrese su apellido paterno (solo el paterno): ')
    apellido_paterno = regs_tres(apellido_paterno, 'Apellido paterno')

    apellido_materno = input('\n Ingrese su apellido materno (solo el materno): ')
    apellido_materno = regs_tres(apellido_materno, 'Apellido Materno')

    edad = input('\n Ingrese su Edad: ')
    edad = regs_dos(edad, 'Edad')

    peso = input('\n Ingrese su peso: ')
    peso = regs(peso,'Peso')

    estatura = input('\n Ingrese su estatura: ')
    estatura = regs(estatura, 'Estatura')
    
    imc = (peso)/(math.pow(estatura,2))
    
    if(imc < 18.9):
        message = 'Indice de Masa Corporal Bajo'
    elif(imc > 18.5 and imc < 24.9):
        message = 'Indice de Masa Corporal Normal'
    elif(imc > 25 and imc < 29.9):
        message = 'Indice de Masa Corporal Ascendido'
    elif(imc > 30 and imc < 34.9):
        message = 'Indice de Masa Corporal Alto'
    elif(imc > 35 and imc < 39.9):
        message = 'Indice de Masa Corporal Peligroso'
    elif(imc > 40):
        message = 'Indice de Masa Corporal Morbido'
        
    # Devolviendo todos los datos ingresados por el usuario: 
    print(f'''
        \n
        \tNombre: {nombre_usuario}
        \tApellido paterno: {apellido_paterno}
        \tApellido materno: {apellido_materno}
        \tEdad: {edad}
        \tPeso: {peso}
        \tEstatura: {estatura}
        \tIndice de Masa Corporal: {imc: .3f}
        \tMensaje de conclusión: {message}
        ''')
    
    message_seg = input('\n Le gusto nuestro Servicio: (Y/N): ')
    if(tir_seg(message_seg) > 0 or len(message_seg) == 0 or ('yy' in message_seg) or ('YY' in message_seg) or ('nn' in message_seg) or ('NN' in message_seg)):
            while(tir_seg(message_seg) > 0 or len(message_seg) == 0 or ('yy' in message_seg) or ('YY' in message_seg) or ('nn' in message_seg) or ('NN' in message_seg)):
                message_seg = input('Respuesta Incorrecta, ingresela de nuevo: (Y/N): ')
            if(message_seg == 'n' or message_seg == 'N'):
                print('\n Gracias por su opinión')
            elif(message_seg == 'y' or message_seg == 'Y'):
                print('\n Gracias por su preferencia')
    elif(message_seg == 'n' or message_seg == 'N'):
        print('\n Gracias por su opinión')
    else:
        print('\n Gracias por su preferencia')
            
answer = input('\n Desea calcular su indice de masa corporal (Y/N): ')
if(answer == 'y' or answer == 'Y'):
    ley_params(answer)
elif(answer == 'n' or answer == 'N'):
    print('''\n Usted ha llegado al Final del Programa
\n''')
elif(tir_seg(answer) > 0):
    ley_params(answer)
elif(len(answer) == 0):
    ley_params(answer)
elif(('yy' in answer) or ('YY' in answer) or ('nn' in answer) or ('NN' in answer)):
    ley_params(answer)
