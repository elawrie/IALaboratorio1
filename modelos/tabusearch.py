import numpy as np
import copy
from modelos.fitness import fitness
from modelos.bitflip import bit_flip
from modelos.isgoal import isgoal
from lectura import make_initial

def tabu_search(initial_state, goal_state_matrix):
    tabu_list = []
    mejor_solucion = []
    path = []
    paths_desechados = []
    solucion_factible = False
    costo_matriz = 0 #Se usa para ver que tan diferente es de la 'goal_state_matrix'.
    i = 0
    j = 0
    profundidad_del_path = 0
    total_de_paths_generados = 1
    solucion_inicial = initial_state
    mejor_solucion = initial_state
    fitness_mejor_solucion = fitness(mejor_solucion, goal_state_matrix)
    tabu_list.append(mejor_solucion) #Se agrega primer intento a la tabu list


    #busca hasta que llega a la solucion final
    while(profundidad_del_path < 126):
        if(profundidad_del_path == 125):
            print("Path desechado. Se genera nueva solución inicial")
            paths_desechados.append(path)
            path = [] #Se limpiar path para crear otro completamente nuevo.
            soy_una_solucion_inicial_tabu = True #Tengo que ver si se puede instanciar en if. Carlos 
            #Se comprueba que nueva instancia del path, no se encuentre en la tabu list.
            if(soy_una_solucion_inicial_tabu == True):
                mejor_solucion = make_initial()
                soy_una_solucion_inicial_tabu = False
                y = 0 #Corrige problema al pasar x como print(tabu_list[x]). Casting Error. 
                for x in tabu_list:
                    #Begin debugging#
                    print(" ---------------------------------")
                    print("|     Elemento Tabu_list " + str(y+1) + "        |")
                    print(" ---------------------------------")
                    print(tabu_list[y]) 
                    #End debugging#
                    if(isgoal(tabu_list[y], mejor_solucion) == True):
                        print("Se ha encontrado una solución generada que es tabú")
                        soy_una_solucion_inicial_tabu = True
                    y +=1 #Solución temporal. Estoy seguro que se puede hacer de otra manera. Carlos
                    ### HAY QUE HACER TESTING A LA TABU LIST. SE DEBE INSTANCIAR UNA MATRIZ IGUAL
                if(soy_una_solucion_inicial_tabu == False):
                    path.append(mejor_solucion)
               



            tabu_list.append(copy.deepcopy(mejor_solucion)) #Se agrega nueva instancia a la tabu list
            fitness_mejor_solucion = fitness(mejor_solucion, goal_state_matrix)
            total_de_paths_generados += 1
            print(fitness_mejor_solucion)
            profundidad_del_path = 0
                
        #usado para salir del loop de busqueda de los vecinos
        exit_vecinos = False

        #print("loop starts")
        #print("the initial state has a fitness of {}".format(fitness_mejor_solucion))
        i=0
        j=0


        #que es el costo_matriz
        #costo_matriz = fitness(solucion_inicial)

        
        #Primer while considera el largo del path#
        #este innecesario?

            #buscando todos los vecinos

        #these two loops will be exited as soon as a state with a better fitness is found.
        #not all neighbouring states will be searched because the difference in fitness between
        #two neighbouring states cannot be higher than 1, if one element is changed at a time

        while( j < 16 and not exit_vecinos):

            while(i < 16 and not exit_vecinos):

                buffer = bit_flip(copy.deepcopy(mejor_solucion),i, j)
                fitness_buffer = fitness(buffer,goal_state_matrix)



                if(fitness_buffer < fitness_mejor_solucion):
                    #print ("old: {} .... new: {}" .format(fitness_mejor_solucion,fitness_buffer))
                    fitness_mejor_solucion = fitness_buffer
                    mejor_solucion = buffer
                    path.append(mejor_solucion)
                    #printing to see if it decreases over iterations

                    solucion_factible = isgoal(buffer,goal_state_matrix)
                    if (solucion_factible == True):
                        #terminó la busqueda
                        print("The search is finished!!")
                        print("Total paths generados: " + str(total_de_paths_generados))
                        print("Profunidad del path exitoso: " + str(profundidad_del_path) + " estados") 
                        return path, paths_desechados
                    else:
                        #print(("Found a neighbouring state with the fitness of {}".format(fitness_buffer)))
                        #print(mejor_solucion)
                        #print("---------------------------")

                        #encontramos un vecino con mejor fitness, empezando el loop otra vez
                        exit_vecinos = True


                i += 1
            i = 0
            j = j + 1

            #añadiendo la mejor de los vecinos al path

        #the path doesn't work perfectly yet, needs to be fixed
        #path.append(copy.deepcopy(mejor_solucion))
        #print("the mejor_solucion is {}".format(fitness_mejor_solucion))
        profundidad_del_path += 1 

    return path
      