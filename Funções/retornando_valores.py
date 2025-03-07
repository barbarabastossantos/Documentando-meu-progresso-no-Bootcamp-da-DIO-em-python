def calcular_total(numeros): # 01 função
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero): # 02 função
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor , sucessor


print(calcular_total ([10,20,34])) #64
print(retornar_antecessor_e_sucessor (10)) #(9,11)


#                      COMENTANDO O CODIGO

# definimos a função : calcular_total
# essa função recebeu um argumento chamado : numeros (nesse caso vai ser uma lista de numeros)
# lista fica entre colchetes []
# return   é uma palavra reservada , usada para retornar um valor de dentro da função .
# sum()    essa função recebe uma lista de numeros e soma todos os elementos.
# 
# No corpo da segunda função  adicionamos a linha : antecessor recebe numero - 1
# para calcular o antecessor  subtraímos  1  do numero fornecido
# Na proxima linha : sucessor recebe numero + 1
# para calcular o sucessor somamos o numero mais um
# 
# o return vai retornar os dois valores  antecessor e sucessor   da função retornar_antecessor_e_sucessor
# 
# chamamos as funções dando um print  