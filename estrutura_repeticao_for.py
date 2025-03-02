#           TABUADA DO 5


for numero in range(1, 11):  
    print(f"5 x {numero} = {5 * numero}")



#          COMENTANDO CODIGO   (Para futuras consultas )

# O for e equivalente ao "para" do portugol  no  visualg  " para  ... ate ... faca "
# o for e usado quando sabemos previamente o numero de vezes que o codigo vai ser executado
# o ranger e uma funcao bult-in do python, ela é usada para produzir uma sequencia de numeros inteiros 
# a partir de um inicio(inclusivo) para um fim (exclusivo)
# no caso do nosso codigo :
# range(1, 11) → Gera os números de 1 a 10 o 11 e ultimo iten e excluido -1 , o primeiro item 
# aparece no caso 1 e o ulimo e menos 1 no caso 11 nao conto para no 10
# numero é a variável de controle, que muda a cada repetição a variavel de controle vai alterando 
# o valor automaticamente dentro do loop for
# sem variavel de controle , incremneto +1 e o  decremento -1 nosso codigo entra no loop infinito
# multiplicamos 5 * numero e mostramos o resultado

# podemos fazer assim tambem esse codigo :

for numero in range(0,51,5):
    print(numero, end=" ")


# o zero indica o start o inicil
#  o 51 o stop o fim (pq queremos que pare no 50)
#  5 e o step queremos que os passos sejam feitos de cinco em cinco
# nesse caso vai imprimir um do lado do outro com espaço entre eles  por causa do end recebe espaço vazio 
# caso nao colocarmos, ficar so numero vai aparecer um embaixo do outro

          

# outro caso para se usar  o for :
#  quando queremos percorrer um objeto iteravel → pode ser  lido elemento por elemento


texto = input("Informe um texto : ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra)

else:
    print( )


# oque vem antes do in nesse caso letra  e o nome que damos para cada item enquanto
# percorremos o texto que e nossa variavel de controle
# oque vem depois do in e onde ela vai procurar no nosso caso texto
# .upper() serve para toranar o texto de minusculo para maiusculo
