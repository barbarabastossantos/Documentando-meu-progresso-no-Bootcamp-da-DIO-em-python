# os dados são acessados e modificados atraves das chaves

dados={"nome":"Barbara","idade":30,"telefone":"999999"}

# aqui estou acessando os valores 
print(20*"=")
print("Acessando os valores do dicionario : \n")
print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

# aqui estou acessando e subescrevendo os valores, mudando os valores

dados["nome"]="Vitoria"
dados["idade"]=18
dados["telefone"]="88888"
print(20*"=")
print("Modificando os valores do meu dicionario : \n")

print(dados)
print(20*"=")