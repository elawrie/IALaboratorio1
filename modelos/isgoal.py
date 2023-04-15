import numpy as np
def isgoal(estado_actual, estado_final):

    if (np.all(estado_actual, estado_final)):

        #If the two matrices are equal, return true
        return 1

    else:
        #if not, return false
        return 0

