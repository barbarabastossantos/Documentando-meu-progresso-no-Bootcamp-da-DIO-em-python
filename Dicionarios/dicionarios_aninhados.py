# dicionarios aninhados , dicionario dentro de dicionario desde que a chave seja imutavel

contatos={
    "barbara@gmail.com " :{"nome":"Barbara","telefone":"99999"},
    "antonio@gmail.com " :{"nome":"Antonio","telefone":"88888"},
    "eliana@gmail.com " :{"nome":"Eliana","telefone":"77777"},
}

telefone=contatos["barbara@gmail.com "]["telefone"]
# o primeiro colchetes tem a chave do meu dicionario 
# o segundo colchetes tem o valor que quero acessar

print(telefone)