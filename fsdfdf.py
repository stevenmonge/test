'''
Entradas: una matriz cuadrada
Salidasdebo crear una funcion que me intercambie los elementos de las diagonales
se intercambian los elementos de las diagonales
Restricciones: (se omite la validacion de restricciones
'''
 
def invertirDiagonales(matriz):
    if(type(matriz) != list):
        print("Solo debe ingresar matriz")
    else:
        recorreColumnasFC(matriz,len(matriz),0)

def recorrerFilasFC(matriz,cantidadFilas,contaFilas):
    if(contaFilas >= cantidadFilas):
        return 0
    else:
        recorrerColumnasFC(matriz,len(matriz[contaFilas]),0,contaFilas)
        return recorrerFilasFC(matriz,cantidadFilas, contaFilas +1)

def recorreColumnasFC(matriz, cantidadColumnas,contaColumnas, posicionFilas):
    if(contaColumnas >= cantidadColumnas):
        return 0
    else:
        return recorreColumnasFC(matriz,cantidadColumnas,contaColumnas +1, posicionFilas)
 
'''
tengo esto

pero no me sirve
debe ser funcion iterativa
'''

# escriba bien el enunciado.
