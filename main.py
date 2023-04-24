from modelos.fitness import fitness
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

    #Crear un estado final 
    final_state = make_final()

    #Chequear el fitness y si el estado inicial es el "goal"
    print("Costo: ", fitness(init_state, final_state))
    print("Es el estado objetivo? ", isgoal(init_state, final_state))

    #Realizar la búsqueda
    path = []
    paths_desechados = []
    path,paths_desechados = tabu_search(init_state,final_state)
    print("Path generado: ")
    y = 0 #Corrige problema al pasar x como print(tabu_list[x]). Casting Error. 
    for x in path:
        #Begin debugging#
        print(" ---------------------------------")
        print("|   Estado path número " + str(y+1) + "        |")
        print(" ---------------------------------")
        print_matrix(path[y])
        y += 1
        #End debugging#

    #Se imprimen paths fracasados
    y = 0
    for x in paths_desechados:
        #Begin debugging#
        print(" ---------------------------------")
        print("|   path fallido número " + str(y+1) + "        |")
        print(" ---------------------------------")
        for path in paths_desechados[y]:
            print_matrix(path)
        y += 1
        #End debugging#

    print("Terminado")

if __name__ == "__main__":
    main()