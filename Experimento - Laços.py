#=======================================#
#           EXPERIMENTO: LACO           #
#=======================================#


print (range(10))
for i in range(10):
    print (i)

dicionario = {'item1': 'valor1', 'item2': 'valor2', 'item3': 'valor3'}

for i in dicionario:
    print (i)

#========================================================
a = 0
while a < 10:
    print (a)
    a+=1

#=======================================================

dicionario = {"intem1": 1, "item2": 2, "item3": 3}

print(dicionario)

for index in dicionario:
  print("dicionario[{}] = {}".format(index, dicionario[index]))

#=========================================================


dicionario = {"item1": 1, "item": 2, "item3": 3}

print(dicionario)

string = "{"
for index in dicionario:
  string += "'{}': {}".format(index, dicionario[index])
  print("dicionario[{}] = {}".format(index, dicionario[index]))
string += "}"

print(string)

#=========================================================


dicionario = {'item1': 'valor1', 'item2': 'valor2', 'item3': 'valor3'}
for i in dicionario:
    print (i)