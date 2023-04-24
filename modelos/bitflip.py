def bit_flip(matrix, i, j):
    #Cambia el bit a 1 si el valor es 0
    if (matrix[i, j] == 0):
        matrix[i, j] = 1
    #Cambia el bit a 0 si el valor es 1
    else:
        matrix[i, j] = 0
    #Retorna la matríz con un bit de diferencia 
    return matrix