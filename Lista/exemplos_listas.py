# Exemplo de listas 

frutas=["laranja","uva", "banana"] # A maior parte dos codigos apresenta a lista desse jeito.
print(frutas)

frutas=[] #              lista vazia , muito util para :

#           01. ARMAZENAR ELEMENTOS DINAMICAMENTE -> pode começar com uma lista vazia  e vai adicionando 
# elementos conforme necessario

lista=[] # iniciamos com a lista vazia 
lista.append(10) #adicionamos a lista o metodo .append() que sempre adiciona elemento no final
lista.append(20)
print(lista)

#No meu código do banco, por exemplo ao inves de armazenar os depósitos e saques como uma string,
#  seria mais prático se eu tivesse usado uma lista vazia. Isso porque a lista permite guardar diferentes 
# tipos de dados (números, strings, floats) e facilita a manipulação depois.

#Como eu usei  uma string vazia (extrato = ""), 
# toda vez que eu adicionei  um novo valor, precisei concatenar (+=), o que foi 
#  mais trabalhoso.

#Já com uma lista vazia (extrato = []), eu poderia simplesmente adicionar os valores com .append(),
#  sem precisar ficar formatando tudo.

#No final para exibir o extrato como texto, bastaria juntar os itens da lista com "\n".join(extrato)
# Alista ajuda a otimizar o codigo

#               02. REPRESENTAR AUSENCIA DE  VALORES -> uma lista pode indicar que não ha dados disponiveis 

registros=[]
if not registros: # if condicional se not  significa não os dois pontos executa,
    # esse comando seria " se não haver registro faça"
    #esse comando vai executar o print  pq a lista continua vazia 
    print("Nenhum registro encontrado.")


#              03. ITERAÇÕES E LOOPS -> usada para acumular resultados resultados de um loop 

numeros_pares=[] #primeiro criamos a lista vazia  para armazenar os numeros pares
for i in range(10):# range(10) gera os numeros de 0 a 9 . O for percorre esses numeros um por um  e guarda o valor em i
    if i %2 ==0: # if verifica se os numeros que estão guardados em i são pares,
  # essa verificaçao e feita atraves do operador modulo % ele retorna o resto da divisão. Para ser par o resto tem que sr igual a 0
        numeros_pares.append(i) # os numeros dentro de i que for par vai ser adicionado atraves do metodo append() na variavel numeros_pares
print(numeros_pares)

 

letras=list("python") # usando o construtor list ele vai trazer cada letra ( argumento iteravel)      
print(letras)