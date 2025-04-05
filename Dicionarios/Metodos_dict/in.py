# para saber se algo existe dentro de outra coisa

contatos={
    "barbara@gmail.com " :{"nome":"Barbara","telefone":"99999"},
    "antonio@gmail.com " :{"nome":"Antonio","telefone":"88888"},
    "eliana@gmail.com " :{"nome":"Eliana","telefone":"77777"},
}

resultado="barbara@gmail.com"in contatos
print(resultado)
resultado="nome"in contatos["antonio@gmail.com "]
print(resultado)
resultado="telefone" in contatos["barbara@gmail.com "]
print(resultado)
resultado="guilherme@gmail.com" in contatos
print(resultado)