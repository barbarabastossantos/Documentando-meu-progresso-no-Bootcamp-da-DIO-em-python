#               DIFERENÇA ENTRE LISTA E TUPLAS

# Uma tupla é parecida com uma lista, mas tem uma diferença muito importante :
# a tupla não pode ser modificada depois de criada.
#  A lista usa colchetes  []  e pode mudar (adicionar e remover itens)
# A tupla usa os parentese () e não pode ser mudado depois de criada
 

#                 QUANDO USAR A TUPLA

# Quando queremos que os dados não sejam alterados 
# Quando precisamos de mais desempenho (tuplas são mais rapidas que listas)
# Quando queremos garantir que a ordem dos valores permaneça fixa

 

#               COMO ACESSAR VALORES DE UMA TUPLA

# Usamos índices igual á lista 
# O primeiro item da tupla tem indice 0, o segundo 1 e assim por diante

numero=(10,20,30,40)

print(numero[0]) #saida 10
print(numero[2]) #saida 
print("=======================")
print("=======================")


#      LISTA :

frutas_lista=["maçã", "banana", "uva"] #criando a lista
frutas_lista[0]="laranja" #alterando a posição 0(trocando maçã por laranja)
print(frutas_lista) #mostra a lista ja modificada
print("=======================")
print("=======================")

#     TUPLA

frutas_tupla=("maçã", "banana", "uva") #criando  a tupla
print(frutas_tupla) #exibindo a tupla se tentar modificar igual fizemos com a lista daria erro 
