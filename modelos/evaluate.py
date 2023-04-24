import numpy as np

def evaluate(estado_actual, estado_final):

    #Retorna la diferencia de bits entra la matríz evaluada, y la de estado objetivo a conseguir.
    cost = 16*16

    #Largo de los filas y columnas
    rows = 16
    columns = 16

    for i in range(rows):
        for j in range(columns):

            if estado_actual[i][j] == estado_final[i][j]:

                #Si los elementos son iguales, entonces se substrae uno a cost.
                cost -= 1

    return cost