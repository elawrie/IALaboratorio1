import numpy as np
from modelos.fitness import fitness
def isgoal(estado_actual, estado_final):

    if (fitness(estado_actual, estado_final) == 0):

        #Si las matrices coinciden, se entrega TRue
        return True

    else:
        #Si no coinciden, entonces se entrega False
        return False

