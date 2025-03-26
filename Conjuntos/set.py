# set elimina itens duplicados em um iteravel

numeros=[1,2,3,4,5,3,4,2,1,7,7,8,5,4,3,9,5,2,3,1] #lista

print(set(numeros)) # aqui printamos a a lista sem os numeros duplicados com uso do set()
print("Ao total temos " ,len(numeros) , "itens") # aqui usamos vemos o tamanho da lista total com o len()
print(numeros) # aqui printamos a lista original 

print("==========================")
# da pra usar com com strings

nome="barbara"

print(nome)
print(set(nome))
print(len(nome))


print("=======================================")

carros=("palio","gol","celta","palio","gol") #tupla

print(set(carros))
print(len(carros))
print(carros)