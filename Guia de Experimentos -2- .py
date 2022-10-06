import string
rb = 'ZXCVBMASDFGHJKLÑQWERTUIOP¨¨+*~[]^``/|¬°!"#$%&()=-_;:,zxcvbmasdfghjklñqwertuiop 1234567890.'
def leer_params(pirm, let):
    ty = 0
    for hj in pirm:
        if(let.find(hj) >= 0):
            ty += 1
    return ty

def tir_seg(ull_seg):
    return leer_params(ull_seg,rb)
    
nom = input('Ingresa el dato: ')
if(nom == 'y'):
    while(nom == 'y' or tir_seg(nom) > 0 or len(nom) == 0):
        if(nom == 'y'):
            print('Tecla "y"')
            nom = input('Ingresa el dato otravez: ')
        elif(tir_seg(nom) > 0 or len(nom) == 0):
            print('Sintaxis mala')
            nom = input('Ingresa el dato otra vez: ')
    else:
        print('El gran Final')    
elif(nom == 'n'):
    print('El gran Final')
elif(tir_seg(nom) > 0 or len(nom) == 0):
    while(tir_seg(nom) > 0 or len(nom) == 0 or nom == 'y'):
        if(nom == 'y'):
            print('Tecla "y"')
            nom = input('Ingresa el dato otravez: ')
        elif(tir_seg(nom) > 0 or len(nom) == 0):
            print('Sintaxis mala')
            nom = input('Ingresa el dato otra vez: ')
    else:
        print('El gran Final')
        
print(string.ascii_lowercase)