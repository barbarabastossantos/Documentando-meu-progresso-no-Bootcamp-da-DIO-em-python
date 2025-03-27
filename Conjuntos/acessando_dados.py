#conjuntos em python não suportam indexação e nem fatiamento, para isso basta converter o conjunto para lista

numeros={1,2,3,4,5,2,4} # nosso conjunto
numeros=list(numeros) # transforma o conjunto em lista usando o contrutor list
print("Na posição 0 esta o numero " ,numeros[0])
print("Na posição -1 esta o numero ",numeros[-1])
print("Na posição -4 esta o numero ",numeros[-4])
print("Na posição 1 esta o numero ",numeros[1])
print("Na posição 2 esta o numero ",numeros[2])
      