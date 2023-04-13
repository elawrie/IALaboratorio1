import numpy as np


def tabu_search(goal_state_matrix):
    tabu_list = []
    mejor_solucion = []
    path = [][]
    solucion_factible = False
    costo_matriz = 0 #Se usa para ver que tan diferente es de la 'goal_state_matrix'.
    i = 0
    j = 0
    k = 0
    '''
    while(solucion_factible == False):
        solucion_inicial = solucion_aleatoria(tabu_list)
        fitness_mejor_solucion = fitness(solucion_inicial)
        tabu_list.append(solucion_inicial)
        
        #Aca se podría definir si la tabu list tiene que ir sacando elementos,
        #o si la dejamos teóricamente infinita de memoria.
        
        costo_matriz = fitness(solucion_inicial)
        path = copy.deepcopy(solucion_inicial)
        
        #Primer while considera el largo del path#
        while( i < 10):
            #Segundo while busca en la vecindad. 16x16= 256#
            while( j < 256):
                buffer = bitFlip(solucion_inicial, j)        
                fitness_buffer = fitness(buffer)
                if(fitness_buffer > fitness_mejor_solucion):
                    fitness_mejor_solucion = fitness_buffer
                    k = j
                solucion_factible = isGoal(buffer)
                if(solucion_factible == True):
                    path = copy.deepcopy(buffer)
                    break;
                j = j + 1
        #Si no se encuentra goal state, entonces en path colocamos la matriz más cercana
        buffer = bitFlip(solucion_inicial, j)
        path = deep.copy(buffer)
        solucion_inicial = buffer # Esta línea  funciona en teoría, pero creo que cambiaré nombres un poco para que sea más semánticamente correcto.
        i = i + 1
        j = 0
        k = 0
        
        
        Return path 
      '''
      
####COMENTARIOS ####
   #No hay implementación  en esta versión para guardar paths fallidos aún. 
   #Solo se guarda el path que logra encontrar la solución
            
        
        
    
    
    


