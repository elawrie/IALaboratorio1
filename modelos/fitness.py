import numpy as np

def fitness(estado_actual, estado_final):
    # !!! CREO QUE SEA MEJOR DEFINIR EL ESTADO FINAL AFUERA DE ESTA FUNCION -> ahora esta en lectura.py !!!
    # # Set a random seed for reproducibility
    # np.random.seed(124)

    # # Generate a 16x16 matrix of random values between 0 and 1
    # estado_final = np.random.randint(2, size=(16, 16))

    #returns the cost of the state, i.e. the number of differing elements in the two matrices
    cost = 16*16

    rows = 16
    columns = 16

    for i in range(rows):
        for j in range(columns):

            if estado_actual[i][j] == estado_final[i][j]:

                #if the elements match, subtract one from cost
                cost -= 1

    return cost