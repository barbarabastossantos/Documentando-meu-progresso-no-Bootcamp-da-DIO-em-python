# Com o indice negativo podemos acessar os elementos da lista de tras para frente
# O indice -1 representa o ultimo elemento o -2 o penultimo e assim por diante

frutas=["maçã", "melancia", "abacaxi", "pitaiá"]
print(frutas[-1]) # ultimo elemento "pitaiá"
print(frutas[-2]) # penultimo elemento "abacaxi"
print(frutas[-4]) # primeiro elemento " maçã"

# Se o indice ultrapassar  o tamanho da lista , um erro ocorre

#print(frutas[-5]) # vai gerar um erro

indice=-5
if indice > len(frutas): # Aqui verificamos se esse indice esta na lista
    print(indice)
else:
    print("Fora do alcance do indice")