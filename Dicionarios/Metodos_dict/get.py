#acessar valores

contatos={
    "barbara@gmail.com":{"nome":"Barbara","telefone":"9999999"}
}

# contatos["chave"] -> vai retornar keyError , pois não existe

print(contatos.get("chave"))  # vai retornar none pois esse valor de chave não existe no dicionario
print(contatos.get("chave", {})) # você pode passar um valor defull pra ele retornar 
print(contatos.get("barbara@gmail.com", {}))
