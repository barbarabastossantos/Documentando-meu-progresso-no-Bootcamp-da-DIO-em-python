# Dicionarios tem CHAVE-VALOR 
# As chaves são imutaveis o valor pode ser tanto mutavel quanto imutavel


pessoa={"nome":"Barbara", "idade":28} 
#pessoa-> dicionario
#nome-> chave : Barbara -> valor
#idade -> chave : 28 -> valor



# Outra forma de criar um dicionario é usando o construtor  dict()

pessoa=dict(nome="Barbara",idade=28)
#pessoa-> dicionario
#nome-> chave vai receber Barbara -> valor 
#idade -> chave vai receber  28 -> valor
#troca os dois pontos  , pelo sinal de igual
# no lugar de {} usamos a palavra reservada dict()


#  Outra forma é quando você ja tem um dicionario criado e quer adicionar mais um item

pessoa["telefone"]="8888-1234"

print(pessoa)