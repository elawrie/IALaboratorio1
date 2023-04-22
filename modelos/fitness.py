import numpy as np

def fitness(estado_actual, estado_final):
    # !!! CREO QUE SEA MEJOR DEFINIR EL ESTADO FINAL AFUERA DE ESTA FUNCION -> ahora esta en lectura.py !!!

    #Retorna la diferencia de bits entra la matríz evaluada, y la de estado objetivo a conseguir.
    cost = 16*16

    rows = 16
    columns = 16

    for i in range(rows):
        for j in range(columns):

            if estado_actual[i][j] == estado_final[i][j]:

                #Si los elementos son iguales, entonces se substrae uno a cost.
                cost -= 1

    return cost