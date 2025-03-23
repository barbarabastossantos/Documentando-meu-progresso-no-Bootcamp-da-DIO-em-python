# FUNÇÃO ENUMERATE()

# Permite percorrer uma lista e ao mesmo tempo, obter o indice de vada elemento, muito util durante a iteração
# Quando você usa enumerate() ela cria uma sequencia de tuplas . cada tupla contem dois valores 
# O primeiro  valor è o indice do elemento
# O segundo valor é o valor do elemento da lista
# Por baixo dos panos a função enumerate() cria uma  sequancia de tuplas  composta por dois valores para cada elemento:
#  essas tuplas seriam assim  -> (0 , "Ana") , (1, "Carlos"), (2, "Maria")

# nesse exemplo vamos usar a função enumerate() em um conjunto com um laço for

nomes =["Ana", "Carlos", "Maria"]
enumerado=enumerate(nomes) # Aqui vc cria uma variavel enumerador  e armazena o resultado do enumerate() 
for item in enumerado: # O for vai iterar sobre essa variavel 
    print(item)

nomes =["Ana", "Carlos", "Maria"]
for indice,nome in enumerate(nomes): # Aqui já aplica o enumerate() dentro do for tronando o codigo mais conciso
    print(f"Indice {indice} : {nome}")