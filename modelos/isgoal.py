import numpy as np
from modelos.fitness import fitness
def isgoal(estado_actual, estado_final):

    if (fitness(estado_actual, estado_final) == 0):

        #If the matrix is the goal matrix, return true
        return True

    else:
        #if not, return false
        return False

