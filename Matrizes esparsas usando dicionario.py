#====================================#
# MATRIZES ESPASAS USANDO DICIONARIO #
#====================================#

# Excelente para representar matrizes com muitos '0'
# menor consumo de memoria

matriz_lista = [[0, 0, 2],
                [0, 4, 0],
                [0, 0, 0]]

matriz_dicionario = {(0, 2):2, (1, 1): 4, (1, 2): 5} # esta dizendo aonde na matriz tera valores diferente de 0. o resto sera 0.

print matriz_dicionario[0, 2]
print matriz_dicionario[1, 1]
print matriz_dicionario[1, 2] #linha e coluna aonde esta o valor diferente de 0

#erro
#print matriz_dicionario[0, 0] #caso eu tente trazer um item que n exista, ele dara erro

# para compensar o erro, usamos o ".get"

print matriz_dicionario.get((0, 0), 0)
print matriz_dicionario.get((1, 1), 1)