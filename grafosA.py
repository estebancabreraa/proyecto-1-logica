from collections import defaultdict 

class Grafo: 
  
    def __init__(self, vertices): 
        self.vertices = vertices 
  
    def mostrarMatriz(self, matrizTC): 
        fila = ""  
        for i in range(self.vertices): 
            for j in range(self.vertices): 
                fila = fila + str(matrizTC[i][j]) 
            print (fila) 
            fila = ""
      
    def clausura_transitiva(self, grafo): 
        
        matrizTC =[i[:] for i in grafo] 
        
        for k in range(self.vertices): 
            for i in range(self.vertices): 
                for j in range(self.vertices): 
                    matrizTC[i][j] = matrizTC[i][j] or (matrizTC[i][k] and matrizTC[k][j]) 
  
        self.mostrarMatriz(matrizTC) 
          
g = Grafo(4) 
  
grafo = [[1, 1, 0, 1], 
         [0, 1, 1, 0], 
         [0, 0, 1, 1], 
         [0, 0, 0, 1]] 
  
g.clausura_transitiva(grafo) 
