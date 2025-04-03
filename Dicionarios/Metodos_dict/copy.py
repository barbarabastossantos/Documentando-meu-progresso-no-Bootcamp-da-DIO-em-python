#copia o dicionario

contatos={
    "barbara@gmail.com":{"nome":"Barbara","telefone":"9999999"}
}

copia=contatos.copy()
copia["barbara@gmail.com"]={"nome":"Babi"}
print(contatos["barbara@gmail.com"])
print(copia["barbara@gmail.com"])
copia2=contatos.copy()
print(copia2)