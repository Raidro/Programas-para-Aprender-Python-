#===================================#
#            DICIONARIOS            #
#===================================#

# sao o tipo de variavel que permite que sejam usados outros tipos de dados como indice
# diferente das listas que apenas aceitam numeros
# Manipulando um dicionario usando as funcoes len e keys
# len retorna o tamanho do dicionario
# keys retorna todas as chaves do dicionario


dicionario = {}
dicionario['item'] = 'conteudo' # temos um indice e uma string
dicionario[0] = 'outro conteudo' # novamente temos, um indice e uma string
dicionario['item'] = 'conteudo modificado'
print  len(dicionario)
print  dicionario.keys()
print  dicionario
#======================================#
