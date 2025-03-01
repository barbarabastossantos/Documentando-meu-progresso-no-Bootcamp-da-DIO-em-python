conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso ! ")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial! ")
    else:
        print("Saldo insuficiente ! ")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso! ")
    else:
        print("Saldo insuficiente! ")
else:
    print ("Sistema não reconhece seu tipo de conta, entre em contato com seu gerente.")


#     COMENTÁRIOS  SOBRE O CÓDIGO ( para futuras consultas)

# 01. Coloque lá nos tipos de conta os operadores lógicos boleanos True e False para podermos brincar com o codigo
# hora testamos a conta normal hora a conta universitaria

# 02. Atribui valores as variaveis 

# 03. Dei inicio a nossa estrutura condicional aninhada if/elif/else (se, senao se , senao)

# 04. Perceba que temos  situações : 

#       Primeira o if da conta  normal,  se saldo for maior ou igual ao saque  dois pontos para sinalizar abertura de bloco
# se for verdade executa esse bloco e printa na tela a messagem  caso contrario pulamos para proxima condição

#        Segunda situação o elif senao se o saque  for menor ou igual saldo adicionado ao cheque especial dois pontos inicia o segundo bloco de aninhamento
#  for verdadeiro executa o print da messagem caso não for pulamos para nosa ultima situação nesse caso do primeiro aninhamento 
# 
#         Terceira situação e ultima nesse caso temos o else o senao,  o else não precisa de teste logico pois ele e a unica opção possivel uma vez que as demias não passou no teste ai so pode ser ele.
# 
# terminamos nosso primeira estrutura aninhada condicional a conta universitaria nao tem  a condicional elif pois nesse caso não tem o cheque especial
#            
