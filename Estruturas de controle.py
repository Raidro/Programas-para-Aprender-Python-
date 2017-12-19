# coding=utf-8
#===================================#
#     EXTRUTURAS DE CONTROLE        #
#===================================#


# condicionais mais basicas em python: if, elif, else

a = 3
if a == 1:
  print 'A é igual a 1'
elif a == 2:
  print 'A é igual a 2'
else:
  print 'A não é nem 1 nem 2'

# Escopo
# Uma variavel declarada dentro de um bloco(escopo) não pode ser usada em outro bloco

a = 1
b = 2

if a == 1:
    c = 3
    #aqui eu consigo acessar a variavel a,b e c
    print a,b,c

elif a == 2:
    d = 4
    # aqui eu consigo acessar a variavel a,b e d
    print a,b,d
else:
    e=5
    # aqui eu consigo acessar a variavel a,b e e
    print a,b,e





