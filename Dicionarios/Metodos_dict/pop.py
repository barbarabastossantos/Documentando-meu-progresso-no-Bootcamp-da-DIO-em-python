# remove um chave do dicionario e retorna valor


contatos={
    "barabara@gmail.com":{"nome":"Barbara", "idade":30}
}

resultado=contatos.pop("barabara@gmail.com","não encontrada")

print(resultado)
print("======\n")
resultado=contatos.pop("barabara@gmail.com","não encontrada")
print(resultado)