from modelos.evaluate import evaluate
from modelos.isgoal import isgoal
from modelos.bitflip import bit_flip
from modelos.expandnode import expand_node
from lectura import make_initial
from lectura import make_final
from modelos.tabusearch import tabu_search
from lectura import print_matrix
import numpy as np

def main():
    #Crear un estado inicial
    init_state = make_initial()
    print("Estado inicial:")
    print_matrix(init_state)

    print()

    #Crear un estado final 
    final_state = make_final()
    print("Estado final:")
    print_matrix(final_state)

    print()

    #Chequear el fitness y si el estado inicial es el "goal"
    print("Costo: ", evaluate(init_state, final_state))
    print("Es el estado objetivo? ", isgoal(init_state, final_state))

    #Realizar la búsqueda
    path = []
    paths_desechados = []
    path,paths_desechados = tabu_search(init_state,final_state)
    print("Path generado: ")
    y = 0 #Corrige problema al pasar x como print(tabu_list[x]). Casting Error. 
    for x in path:
        print(" ---------------------------------")
        print("|   Estado path número " + str(y+1) + "        |")
        print(" ---------------------------------")
        print_matrix(path[y])
        y += 1


    #Los paths desechados para ver con el tema de debugging
    # #Se imprimen paths fracasados
    # y = 0
    # for x in paths_desechados:
    #     #Comienza debugging#
    #     print(" ---------------------------------")
    #     print("|   path fallido número " + str(y+1) + "        |")
    #     print(" ---------------------------------")
    #     for path in paths_desechados[y]:
    #         print_matrix(path)
    #     y += 1
    #     #Termina debugging#

    print("Terminado")

if __name__ == "__main__":
    main()