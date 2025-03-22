# Acesso direto significa acessar um elemento da lista  pelo seu índice.
# Esse índice começa em 0 e termina  no tamanho da lista -1  ex uma lista de 20 numeros começa em 0 e termina em 19 pq 20-1=
  


numeros=[10,20,30,40,50]
print(numeros[0]) # indice 0 é o primeiro elemento o 10
print(numeros[2]) # indice 2 é o terceiro elemneto o 30
print(numeros[4]) # indice 4 é o quinto elemento o 50



# IMPORTANTE: Se tentarmos acessar um indice que não existe ocorrerá um erro.
# Para evitar isso usamos metodo len() ele verifica o tamanho da lista 

indice=3
if indice < len(numeros):
    print(numeros[indice])
else:
    print("Indice fora de alcance!")
