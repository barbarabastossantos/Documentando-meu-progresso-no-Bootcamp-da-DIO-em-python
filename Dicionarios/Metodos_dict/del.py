# outra forma de remover

contatos={
    "barbara@gmail.com " :{"nome":"Barbara","telefone":"99999"},
    "antonio@gmail.com " :{"nome":"Antonio","telefone":"88888"},
    "eliana@gmail.com " :{"nome":"Eliana","telefone":"77777"},
}

print(contatos)

del contatos["antonio@gmail.com "]["telefone"]
print(contatos)
del contatos["barbara@gmail.com "]
print(contatos)