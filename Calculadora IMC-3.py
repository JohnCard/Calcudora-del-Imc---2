rb = 'ZXCVBNMASDFGHJKLÑQWERTUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbnmasdfghjklñqwertuiop 1234567890.'
rt = 'ZXCVBMASDFGHJKLÑQWERTUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbmasdfghjklñqwertuiop 1234567890.'
c = 'ZXCVBNMASDFGHJKLÑQWERTYUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbnmasdfghjklñqwertyuiop'; b = '1234567890.'
a = 'ZXCVBNMASDFGHJKLÑQWERTYUIOPzxcvbnmasdfghjklñqwertyuiop '; d = '¨¨+*~[]^``/|¬°!"#$%&()=-_;:1234567890.'

def ley_params(answer_seg):
    while(answer_seg == 'y' or answer_seg == 'Y' or len(answer_seg) == 0 or tir_seg(answer_seg) > 0):
        if(answer_seg == 'y' or answer_seg == 'Y'):
            CalC_IMC()
            answer_seg = input('Desea calcular otro indice (Y/N): ')
        elif(tir_seg(answer_seg) > 0):
            answer_seg = input('Respuesta ¡INCORRECTA!, desea intentarlo de nuevo (Y/N): ')
        elif(len(answer_seg) == 0):
            answer_seg = input('No se digito nada, desea intentarlo de nuevo (Y/N): ')
    else:
        print('Final del Programa')
        
def leer_params(pirm, let):
        ty = 0
        for hj in pirm:
            if(let.find(hj) >= 0):
                ty += 1
        return ty

def tir_seg(ull_seg):
    return leer_params(ull_seg,rt)

def hall(letter):
    return leer_params(letter,b)

def hall_seg(letter_seg):
    return leer_params(letter_seg, c)

def hall_ter(letter_ter):
    ag = 0
    for t in letter_ter:
        if(t == '.'):
            ag += 1
    return ag

def hall_curt(letter_curt):
    return leer_params(letter_curt, a)

def hall_quint(letter_quint):
    return leer_params(letter_quint, d)

def regs(param_prim, param_seg):
    while(((hall(param_prim)) == 0) or ((hall_seg(param_prim)) > 0) or ((hall_ter(param_prim)) > 1) or (' ' in param_prim)):
            param_prim = input(f'Ingrese nuevamente su {param_seg} por favor: ')
    return float(param_prim)

def regs_dos(num, numero_parametro):
    while((num.isnumeric() == False) or (' ' in num)):
            num = input(f'Ingrese nuevamente su {numero_parametro} por favor: ')
    return int(num) 

def regs_tres(pram, pram_do):
    while(((hall_curt(pram)) == 0) or ((hall_quint(pram)) > 0) or ('  ' in pram) or (pram.startswith(' '))):
        pram = input(f'Ingrese correctamente su {pram_do} porfavor o no podremos continuar: ')
    return pram

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
    nombre_usuario = input('Ingrese su Nombre: ')
    nombre_usuario = regs_tres(nombre_usuario, 'Nombre')

    apellido_paterno = input('Ingrese su apellido paterno (solo el paterno): ')
    apellido_paterno = regs_tres(apellido_paterno, 'Apellido paterno')

    apellido_materno = input('Ingrese su apellido materno (solo el materno): ')
    apellido_materno = regs_tres(apellido_materno, 'Apellido Materno')

    edad = input('Ingrese su Edad: ')
    edad = regs_dos(edad, 'Edad')

    peso = input('Ingrese su peso: ')
    peso = regs(peso,'Peso')

    estatura = input('Ingrese su estatura: ')
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
        
        Nombre: {nombre_usuario}
        Apellido paterno: {apellido_paterno}
        Apellido materno: {apellido_materno}
        Edad: {edad}
        Peso: {peso}
        Estatura: {estatura}
        Indice de Masa Corporal: {imc}
        Mensaje de recomendación: {message}
        
        ''')
    
    message_seg = input('Le gusto nuestro Servicio: (Y/N): ')
    if(tir_seg(message_seg) > 0 or len(message_seg) == 0):
            while(tir_seg(message_seg) > 0 or len(message_seg) == 0):
                message_seg = input('''\nRespuesta Incorrecta, ingresela de nuevo: (Y/N): ''')
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
    print('Final del Programa')
elif(tir_seg(answer) > 0):
    ley_params(answer)
elif(len(answer) == 0):
    ley_params(answer)