# Percorrendo uma lista aninhada com for
# Como cada  linha e uma lista separada podemos usar dois loops for
# O primeiro for  pega uma linha por vez
# O segundo for pega cada numero dentro da linha 

dados=[
    [1,2,3], # primeira lista , linha 0
    [4,5,6], # segunda lista , linha 1
    [7,8,9]  # terceira lista , linha 2
] # cada lista e chamada de linha


for linha in dados: # percorre cada linha da lista inteira, for pega linha(lista"filha") dentro de dados(a lista "mãe")
    for numero in linha: # percorre cada numero dentro da lista filha
        print(numero, end="") # o end= faz com que os numeros sejam impressos um do lado do outro


        # com o segundo for você consegue imprimir sem virgula e sem colcetes 
        # primeiro for vc pega linha dentro de dados no segundo for vc pega numero dentro de linha
        

print("\n")   
print("==============================\n")

for numero in dados:
    print(numero,end="")

