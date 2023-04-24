from modelos.bitflip import bit_flip
import copy

def expand_node(matrix):
    hijos = []
    #Recorrer filas
    for i in range(16):
        #Recorrer columnas 
        for j in range(16):
            #Agrega cada hijo posible encontrado con el cambio de una celda usando la función bit_flip
            matrix_copy = copy.deepcopy(matrix)
            hijos.append(bit_flip(matrix_copy, i, j))
    
    #Retorna una lista de todos los hijos posibles del estado actual
    return hijos