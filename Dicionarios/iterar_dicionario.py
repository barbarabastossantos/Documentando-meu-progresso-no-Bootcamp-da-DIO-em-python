# a forma mais comum de percorrer os dados de um dicionariio é ultilizando o comando for

contatos={
    "barbara@gmail.com " :{"nome":"Barbara","telefone":"99999"},
    "antonio@gmail.com " :{"nome":"Antonio","telefone":"88888"},
    "eliana@gmail.com " :{"nome":"Eliana","telefone":"77777"},
}


for chave,valor in contatos.items():
    print(chave,valor)

# esse for vai percorrer chave, valor de conatos intem a item e vai imprimir na tela o resultado
# .items() e um metodo 