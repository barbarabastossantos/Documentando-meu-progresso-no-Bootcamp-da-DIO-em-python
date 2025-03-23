# FATIAMENTO

# Permite acessar partes especificas de uma lista : lista[inicio:fim:passo]
# Inicio -> indice inicial(inclusivo)
# Fim -> Indice final( exclusivo, ou seja , não inclui esse indice) sempre indice final -1
# Passo -> Pula elementos da lista

numeros=[10,20,30,40,50,60,70,80,90]
print(numeros[2:6]) # Saida [30,40,50,60]

print(numeros[-5:]) # Começa a contagem de tras pra  frente , fatiamento com indice negativo

print(numeros[1:8:2]) # Saida [20,40,60,80] começa no indice 1 (20) vai ate o 8 mas não inclui ele e pula de 2 em 2

print(numeros[::-1]) # Faz a lista percorrer de tras pra frente , espelhamento 

print(numeros[::]) # Retorna a copia exata  da lista 