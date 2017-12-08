# coding=utf-8
#===================================#
#       MANIPULANDO LISTAS          #
#===================================#


# Criando uma lista


Lista = [1, 2, 3, 4, 'teste']
print Lista
#==================================

# Usando o Append para adicionar novos itens a lista


Lista2 = [1,2,3,4, 'Mateus']
print "\nAntes: ", Lista2
Lista2.append('Rodrigo')
print "Depois: \n", Lista2
#==================================


# Coletando itens de uma lista
# O primeiro indice é ' 0 '

Lista3 = [1,2,3,4, 'Satiro']
print Lista3[0]
print Lista3[1]
print Lista3[-1]
#===================================

# Removendo itens de uma lista

Lista4 = [1,2,3,4, 'Mateus']
print "\nAntes da Remoção: ", Lista4
Lista4.remove('Mateus')
print "Depois da remoçao \n", Lista4
#===================================

# Pegando um pedaço da lista

Lista5 = [1,2,3,4,5,6]
print Lista5[1:]
print Lista5[1:4]
print Lista5[:5]
print Lista5[0:3]
#===================================

# Para somar uma lista com outra usa o operador ' + '
# Para ordenar uma lista usa a função ' sorted '

L1 = [1,2,3,4]
L2 = [5,6,7,8]

print "\n"
#print "As listas somadas: %s" L1 + L2
print "Soma das listas: ", L1 + L2
L3 = [3,2,5,7,8,1,4]
print "Lista Ordenada: ",sorted(L3)