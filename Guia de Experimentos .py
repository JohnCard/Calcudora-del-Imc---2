# def regs_tres(pram, pram_do):
#     while((pram.isalpha() == False)):
#             pram = input(f'Ingrese correctamente su {pram_do} porfavor o no podremos continuar: ')
#     return pram

# def regs(param_prim, param_seg,):
#     try:
#         float(param_prim)
#     except:
#         while((str.isnumeric(param_prim) == False) or (('.' not in param_prim) == True)):
#             param_prim = input(f'Ingrese nuevamente su {param_seg} por favor: ')
#     finally:
#         return float(param_prim)
    
# nombre_usuario = input('Ingrese su Nombre: ')
# if((nombre_usuario.isalpha() == False)):
#     nombre_usuario = regs_tres(nombre_usuario, 'Nombre')

# peso = input('Ingrese su peso: ')
# if(('.' not in peso) or (str.isdigit(peso) == False) or (len(peso) == 0)):
#     peso = regs(peso,'Peso')


    
# # Devolviendo todos los datos ingresados por el usuario: 
# print(f'''
# Peso: {peso}
# nombre usuario: {nombre_usuario}
# ''')
import string
from turtle import left


all = '4'
print(all.isalpha())
all2 = 'sa'
if(('s' in all2) or ('d' in all2) or (('4' in all2) and ('5' in all2))):
    print('Hello World')
else:
    print('Bye World')

a = '45'
b = ('12345')
if(a in b):
    print('que onda')
else:
    print('quiuvo')

rg = 'hello'
rt = input('Igresalo ya ¡COÑO!: ')
if(rt):
    print('Eric Cartman')
else:
    print('No existe')
    
def regs():
    nombre = input('Ingrese ya su nombre: ')
    return nombre

print(regs())