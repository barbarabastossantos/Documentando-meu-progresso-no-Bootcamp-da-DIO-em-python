saldo = 2000
saque = 300

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque! ")

#         COMENTARIO DO CÓDIGO

# A variavel status recebe o teste logico da condicional if/else
# if se saldo for maior ou igual ao sauque retorna para a varivel staus a string sucesso se nao else retorna string falha 
#dentro do print coloquei o f de format para colocar a variavel status que vai mostrar na tela o valor verdadeiro que ela recebeu seja do if ou do else