
#         uso do  break


while True: # Criei um loop infinite while True propositalmente para poder usar o break
# o loop infinito não para sozinho 
    numero = int(input(" Informe um numero : "))

    if numero == 10: # aqui verificamos se o numero digitado e igual a 10 
# o operador de comparação "=="  verifica se os dois valores são iguais 
        break # o comando break faz o loop para imediatamente
# se o usuario digitar 10 o programa para de rodar
print(numero) 



#        uso do continue


for numero in range(100):  # O loop "for" percorre os números de 0 a 99 (100 números no total).
    
    if numero % 2 == 0:  
        # Aqui verificamos se o número atual é PAR.
        # O operador "%" (módulo) retorna o resto da divisão.
        # Se "numero % 2" for igual a 0, significa que o número é divisível por 2, ou seja, é um número PAR.
        
        continue  
        # O "continue" faz o loop IGNORAR tudo o que vem depois dele e passar para a próxima repetição.
        # Ou seja, se o número for par, ele NÃO será impresso e o programa segue para o próximo número.
    
    print(numero)  
    # Essa linha só será executada se o número NÃO for par (ou seja, se for ímpar).
    # Portanto, o programa imprimirá apenas os números ímpares de 0 a 99.


