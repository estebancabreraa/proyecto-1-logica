#Universidad Del Valle De Guatemala
#Andrea Elias -17048
#Randy Venegas -18341
#Esteban Cabrera -17781
#Programa que utiliza el algoritmo de warshall, que se utiliza para encontrar el cierre transitivo
#de un grafo por medio de las matrices de adyacencia 

#argumento matriz de adyacencua
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
#
def Floyd_Warshall(adyMat):

#inicializa el numero de los vertices
    vertices = len(adyMat)

    #matriz de respaldo
    matriz2 = adyMat

    #Ciclo donde los caminos sin direcion son seteados a cero
    for vert1 in range(vertices):
        for vert2 in range(vertices):
            if matriz2[vert1][vert2] == 0:
                matriz2[vert1][vert2] = float('INF')

    # Ciclo para determinar los caminos mas cortos

    for k in range(vertices):
        #i representa el primer vertice
        for i in range(vertices):
            # j es el segundo vertice
            for j in range(vertices):
                matriz2[i][j] = min(matriz2[i][j], (matriz2[i][k] + matriz2[k][j]))

    return matriz2
#Matriz de relacion de la cual se desea obtener el cierre transitivo, aqui puede ingresar la matriz deseada.
MatrizOriginal = [[0, 1, 1, 0],
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




