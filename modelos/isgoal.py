import numpy as np
from modelos.evaluate import evaluate
def isgoal(estado_actual, estado_final):
    if (evaluate(estado_actual, estado_final) == 0):

        #Si las matrices coinciden, se entrega TRue
        return True

    else:
        #Si no coinciden, entonces se entrega False
        return False

