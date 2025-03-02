opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n : "))

    if opcao == 1:
        print(" Sacando .....")
    elif opcao == 2:
        print("Exibindo o Extrato ....")
else:
    print("Obrigada por usar nossos serviços.")


    ## Estrutura de repetição "while" em Python
# -----------------------------------------
# O "while" é um laço de repetição (loop) que continua executando um bloco de código 
# enquanto a condição especificada for verdadeira. Ele é útil quando não sabemos 
# exatamente quantas vezes precisamos repetir uma ação, diferente do "for", 
# que geralmente é usado quando sabemos a quantidade de repetições.
# -----------------------------------------

# Inicializamos a variável "opcao" com -1.
# Por que -1? Porque precisamos de um valor inicial que não seja 0,
# já que o laço while só para quando opcao == 0.
#opcao = -1  


# Criamos um loop "while" que continuará rodando enquanto "opcao" for diferente de 0.
# O operador "!=" significa "diferente de".
#while opcao != 0:  
    # Exibe um menu de opções para o usuário escolher.
    # O "\n" é uma quebra de linha, que ajuda a deixar a exibição mais organizada.
   # print("\n1 - Sacar\n2 - Extrato\n0 - Sair")  
    
    # Pedimos ao usuário que escolha uma opção digitando um número.
    # O input() sempre retorna um texto (string), então usamos "int()" para converter para número inteiro.
    # Se o usuário digitar um valor que não seja um número, o programa vai gerar um erro.
   # opcao = int(input("Escolha uma opção: "))  
    
    # Estrutura condicional para verificar a escolha do usuário.
    
    # Se a opção escolhida for 1...
    #if opcao == 1:  
        # Exibe a mensagem "Sacando..."
   #     print("Sacando...")  
    
    # Se a opção escolhida for 2...
   # elif opcao == 2:  
        # Exibe a mensagem "Exibindo extrato..."
    #    print("Exibindo extrato...")  
    
    # Se a opção for diferente de 1 e 2...
   # else:  
        # Mensagem de despedida caso o usuário escolha sair (0) ou digite outra coisa.
    #    print("Obrigado por usar nosso serviço.")  
        
# Fim do programa. Quando o usuário digitar 0, o while será encerrado e o programa termina.