import numpy as np

# generar un estado inicial
def make_initial():
    # Set a random seed for reproducibility
    np.random.seed(123)
    # Generate a 16x16 matrix of random values between 0 and 1
    initial_state = np.random.randint(2, size=(16, 16))
    return initial_state

def make_final():
    # Set a random seed for reproducibility
    np.random.seed(124)

    # Generate a 16x16 matrix of random values between 0 and 1
    final_state = np.random.randint(2, size=(16, 16))
    return final_state

# function that print a given matrix
def print_matrix(state):
  for row in state:
    print(row)