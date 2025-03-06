def exibir_messagem():
    print("Òla mundo das funções!")

def exibir_messagem2(nome):
    print(f"Seja bem vindo {nome} !")

def exibir_messagem3(nome="Anonimo"):
    print(f"Seja bem vindo {nome} !")


exibir_messagem()
exibir_messagem2(nome = "Barbara")
exibir_messagem3()
exibir_messagem3(nome = "Choppi")


#                          COMENTANDO  O  CODIGO 

# def é uma palavra reservada do python e indica estamos definindo uma função
# oque se segue depois do def , no nosso caso exibir_messagem,  e o nome que damos a nossa função
# os () são obrigatorios  é indicam que essa é uma função 
# dentro deles poderiam estar argumentos(valores que passam para  a função)
# os dois pontos indicam  que agora vem o corpo da função, ou seja , oque  ela vai executar quando for cahamada
# quando dentro do parenteses tem argumento (nome)  essa função espera receber um dado quando for chamada  
# esse dado é chamado de parâmetro

# para executar não basta apenas definir temos que chamar as funções 
# para chamar você escreve o nome da função com os parenteses
#  Lembrando que e se a função  não tiver um valor  padrão para o parâmentro
#  e você não passar um argumento ao chamar o python vai gerar um erro
# valor padrão evita erros quando um argumneto não e passado 
# evita usar valor padão quando queremos obrigar o usuario a colocar valor
# nome = "anonimo" foi um valor padrão
            
