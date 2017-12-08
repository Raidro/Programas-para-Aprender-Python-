# coding=utf-8
#===================================#
#       EXPERIMENTO COM LISTAS      #
#===================================#

lista = [1,2,3,'Mateus','Tiago',4,5,6]
print "Lista: ", lista

lista.append('Rodrigo') # so aceita 1 argumento
print "\nAdcionando usando Append: ", lista

lista += [7,8,9]
print "\nAdicionado a lista: ", lista # outra forma de adicionar a lista sem usar o "append"

print "\nPrimeiro Item da lista: ", lista[0]
print "\nQuarto Item da lista: ", lista[4]
print "\nListas de 0 : 5: ", lista[0:6]


lista.remove(4)
print "\nItem Removido: ", lista
print "================================="

