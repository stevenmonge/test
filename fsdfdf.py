'''
Entradas: una matriz cuadrada
Salidasdebo crear una funcion que me intercambie los elementos de las diagonales
se intercambian los elementos de las diagonales
Restricciones: (se omite la validacion de restricciones
'''
## ESTE MEJOR NO PORQUE ESTO ES RECURSIVO! 
##def invertirDiagonales(matriz):
##    if(type(matriz) != list):
##        print("Solo debe ingresar matriz")
##    else:
##        recorreColumnasFC(matriz,len(matriz),0)
##
##def recorrerFilasFC(matriz,cantidadFilas,contaFilas):
##    if(contaFilas >= cantidadFilas):
##        return 0
##    else:
##        recorrerColumnasFC(matriz,len(matriz[contaFilas]),0,contaFilas)
##        return recorrerFilasFC(matriz,cantidadFilas, contaFilas +1)
##
##def recorreColumnasFC(matriz, cantidadColumnas,contaColumnas, posicionFilas):
##    if(contaColumnas >= cantidadColumnas):
##        return 0
##    else:
##        return recorreColumnasFC(matriz,cantidadColumnas,contaColumnas +1, posicionFilas)
## 

'''
debe crear una funcion INTERACTIVA!!!! que  permita cambiar los elementos de las diagonales
ejemplo         
asi entra[[1,2,3],[4,5,6],[7,8,9]]
asi sale[[3,2,1],[4,5,6],[9,8,7]]
'''
# SOLUCION: AL SER INTERACTIVA SE APLICA WHILE o FOR DE LA SIGUIENTE MANERA.
def invertirDiagonales(matriz):
 
    if(type(matriz) != list):
        print("Solo debe ingresar matriz")
    else:
        posicionFila = 0
        
        while(posicionFila < len(matriz)):
            if(posicionFila == 0 or posicionFila == len(matriz)-1):        # preguntamos si esta en la primer fila O ULTIMA, ya que las diagonales estan solo en la primer fila y la ultima
                
                elementoPosicionZero = matriz[posicionFila][0]             # Guardamos el primer elemento antes de cambiarlo
                elementoPosicionUltima  = matriz[posicionFila][len(matriz)-1]  # guardamos el ultimo antes de cambiarlo

                # intercambiamos los elementos:
                matriz[posicionFila][0] = elementoPosicionUltima
                matriz[posicionFila][len(matriz)-1] = elementoPosicionZero
            posicionFila += 1
     
    print("la invertida es: ")      # no se imprime pero se retorna: 
    return matriz
                
                
 
