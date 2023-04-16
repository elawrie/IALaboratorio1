from modelos.fitness import fitness
from modelos.isgoal import isgoal
from modelos.bitflip import bit_flip
from modelos.expandnode import expand_node
from lectura import make_initial
from lectura import make_final
from lectura import print_matrix
import numpy as np

def main():
    # crea un estado inicial
    init_state = make_initial()
    # imprime el estado inicial
    # print_matrix(init_state)

    # separa los matrices 
    print()

    # hace un estado final 
    final_state = make_final()
    # imprime el estado final 
    # print_matrix(final_state)

    # chequea el fitness y si el estado inicial es el "goal"
    print("costo: ", fitness(init_state, final_state))
    print("is goal: ", isgoal(init_state, final_state))

    # prueba la funcion de bit_flip
    # bit_flip(init_state, 0, 0)
    # print_matrix(init_state)
    print()

    # prueba la funcion expand_node
    hijos = []
    hijos = expand_node(init_state)
    
    # imprime todos los hijos posibles del estado inicial 
    # print("are equal: ", isgoal(hijos[0], hijos[2]))
    # print(hijos)

if __name__ == "__main__":
    main()
