#Universidad Del Valle De Guatemala
#Andrea Elias -17048
#Randy Venegas -18341
#Esteban Cabrera -17781
#Programa que utiliza el algoritmo de warshall, que se utiliza para encontrar el cierre transitivo
#de un grafo por medio de las matrices de adyacencia 

#argumento matris de adyacencua
def Warshall(adjMatriz):
    # Asigna el numero de vertices tomandolo del numero de columnas y filas de la matriz.
    #Numero de vertices corresponde al numero de valores de la relacion dada por ejemplo R ={1,2,3,4} 4 vertices.
    Vertices = len(adjMatriz)

    #Crea una nueva matriz para poder operar sobre ella.
    laMatriz = adjMatriz

    # Ciclo for para acceder o alterar cada ruta, para hacer el cierre trnasitivo en laMatriz

    
    for g in range(Vertices):
        # 'h' corresponde primer vertice 
        for h in range(Vertices):
            # 'j' corresponde a el segundo vertice 
            for j in range(Vertices):
                
                laMatriz[h][j] = laMatriz[h][j] or (laMatriz[h][g] & laMatriz[g][j])

    
    return laMatriz


#Matriz de relacion de la cual se desea obtener el cierre transitivo, aqui puede ingresar la matriz deseada.
MatrizOriginal = [[0, 0, 1, 0],
                  [1, 0, 0, 1],
                  [0, 0, 1, 0],
                  [0, 1, 0, 1]
                  ]
#cada bloque de numeros representa una fila.
print("Matriz dada:")
print(MatrizOriginal[0])
print(MatrizOriginal[1])
print(MatrizOriginal[2])
print(MatrizOriginal[3])

print("Cierre transitivo")
Warshall(MatrizOriginal)

print(MatrizOriginal[0])
print(MatrizOriginal[1])
print(MatrizOriginal[2])
print(MatrizOriginal[3])



