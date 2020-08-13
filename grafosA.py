#Universidad Del Valle De Guatemala
#Andrea Elias -17048
#Randy Venegas -18341
#Esteban Cabrera -17781

#Programa que da el cierre transitivo, creando una matriz booleana de alcance, en este se ahorra espacio comparado con la implementacion del algoritmo de Warshall .


#librerias
from collections import defaultdict 


#clase que contiene todas las funciones
class Grafo: 
  
  #inicializacion de los vertices, estos dependiendo del numero de elementos del conjunto.
    def __init__(self, vertices): 
        self.vertices = vertices 
        
   #Funcion para la impresion de la matriz
  
    def mostrarMatriz(self, matrizTC): 
        fila = ""  
        for i in range(self.vertices): 
            for j in range(self.vertices): 
                fila = fila + str(matrizTC[i][j]) 
            print (fila) 
            fila = ""
            
            #Funcion de cierre transitivo
      
    def cierre_transitivo(self, grafo): 
        
        matrizTC =[i[:] for i in grafo] 
        
      
        for k in range(self.vertices): 
          #Recorre los vertices uno por uno 
            for i in range(self.vertices): 
                for j in range(self.vertices): 
             #Si el vertice k se encuentra en camino entre i a j, verificar que el valor es 1
                    matrizTC[i][j] = matrizTC[i][j] or (matrizTC[i][k] and matrizTC[k][j]) 
  
        self.mostrarMatriz(matrizTC) 
          
g = Grafo(4) 
  #Grafo del que se desea obtener el cierre transitivo, aqui puede colocar los valores que desee.
grafo = [[1, 1, 0, 1], 
         [0, 1, 1, 0], 
         [0, 0, 1, 1], 
         [0, 0, 0, 1]] 
  
g.cierre_transitivo(grafo) 
