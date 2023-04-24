import numpy as np
import copy
from modelos.evaluate import evaluate
from modelos.bitflip import bit_flip
from modelos.isgoal import isgoal
from lectura import make_initial
from modelos.expandnode import expand_node

def tabu_search(initial_state, goal_state_matrix):
    tabu_list = []
    mejor_solucion = []
    path = []
    paths_desechados = []
    solucion_factible = False
    costo_matriz = 0 #Se usa para ver que tan diferente es un estado de la 'goal_state_matrix'.
    i = 0
    j = 0
    profundidad_del_path = 0
    total_de_paths_generados = 1
    solucion_inicial = initial_state
    mejor_solucion = initial_state
    fitness_mejor_solucion = evaluate(mejor_solucion, goal_state_matrix)
    tabu_list.append(mejor_solucion) #Se agrega primer intento a la tabu list


    #Busca hasta que llega a una solucion final. Profunidad máxima de 125 Estados concatenados del original.
    while(profundidad_del_path < 126):
        #Si se han realizado 125 Estados desde un path inicial. Se instancia otro nuevo.
        if(profundidad_del_path == 125):
            print("Path desechado. Se genera nueva solución inicial")
            paths_desechados.append(path)
            path = [] #Se borra contenido de 'path' para crear otro completamente nuevo.
            soy_una_solucion_inicial_tabu = True 
            #Se comprueba que nueva instancia de 'path', no se encuentre en la tabu list.
            if(soy_una_solucion_inicial_tabu == True):
                mejor_solucion = make_initial()
                soy_una_solucion_inicial_tabu = False
                y = 0 #Corrige problema al pasar x como print(tabu_list[x]). Casting Error. 
                for x in tabu_list:
                    #Begin debugging
                    print(" ---------------------------------")
                    print("|     Elemento Tabu_list " + str(y+1) + "        |")
                    print(" ---------------------------------")
                    print(tabu_list[y]) 
                    #End debugging#
                    if(isgoal(tabu_list[y], mejor_solucion) == True):
                        print("Se ha encontrado una solución generada que es tabú")
                        soy_una_solucion_inicial_tabu = True
                    y +=1 #Solución temporal. Estoy seguro que se puede hacer de otra manera. Carlos
                if(soy_una_solucion_inicial_tabu == False):
                    path.append(mejor_solucion)
               
            #Se ajustan variables para que nueva iteración funcione correctamente
            tabu_list.append(copy.deepcopy(mejor_solucion)) #Se agrega nueva Estado inicial a la tabu list
            fitness_mejor_solucion = evaluate(mejor_solucion, goal_state_matrix)
            total_de_paths_generados += 1
            print(fitness_mejor_solucion)
            profundidad_del_path = 0
                
        #Se ajustan variables a usarse en bucle while anidado
        exit_vecinos = False
        i=0
        j=0

        '''
        Estos dos ciclos while seran terminados tan pronto como se encuentre un vecino de 'mejor_solucion'
        que poseea mejor fitness que la matriz contenida en la variable mencionada.  De esta forma no se busca 
        en toda la vecindad, ya que solo es posible encontrar soluciones mejores con diferencia de 1 en el fitness.
        En palabras simples: Las soluciones mejores solo pueden ser de un bit mejor con este método de exploración.
        '''

        #Llamar expand_node
        all_neighbors = expand_node(mejor_solucion)

        #Recorrer todos los vecinos para comparar y buscar el vecino mejor 
        for neighbor in all_neighbors:
            if (exit_vecinos == False):
                fitness_buffer = evaluate(neighbor,goal_state_matrix)
                #Si se encuentra un vecino mejor
                if(fitness_buffer < fitness_mejor_solucion):
                    fitness_mejor_solucion = fitness_buffer
                    mejor_solucion = neighbor
                    path.append(mejor_solucion)
                    solucion_factible = isgoal(neighbor,goal_state_matrix)
                    if (solucion_factible == True):
                        #Terminó la busqueda
                        print("Busqueda finalizada!!")
                        print("Total paths generados: " + str(total_de_paths_generados))
                        print("Profunidad del path exitoso: " + str(profundidad_del_path) + " estados") 
                        #Se envía listas a main.py para su posterior impresión
                        return path, paths_desechados
                    else:
                        #Si se encuentra un vecino con mejor fitness, empezamos el loop general otra vez
                        #cambiando el valor de 'exit_vecinos'
                        exit_vecinos = True
            else:
                break

        #Se actualiza registro de la profundiad del path actual buscado
        profundidad_del_path += 1 