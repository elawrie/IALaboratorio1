import numpy as np

#Genera un estado inicial aleatorio.
def make_initial():
    np.random.seed()
    initial_state = np.random.randint(2, size=(16, 16))
    return initial_state

#Genera un estado final aleatorio.
def make_final():
    np.random.seed(124)
    final_state = np.random.randint(2, size=(16, 16))
    return final_state

#Función que imprime una matríz
def print_matrix(state):
  for row in state:
    print(row)