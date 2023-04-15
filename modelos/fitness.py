import numpy as np

def fitness(estado_actual, estado_final):

    #returns the numeric value of elements with an equal value in the two matrices
    matches = 0

    rows = 16
    columns = 16

    for i in range(rows):
        for j in range(columns):

            if estado_actual[i][j] == estado_final[i][j]:

                #if the elements match, add one to matches
                matches += 1

    return matches