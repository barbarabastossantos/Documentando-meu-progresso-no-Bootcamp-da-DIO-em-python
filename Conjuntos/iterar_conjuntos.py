# Para iterar conjunto utilizamos o for e a função enumerate

# USANDO O FOR

nomes={"Barbara","Vanessa","Rodrigo"} #Crio meu conjunto 
for nome in nomes: # uso meu for ele vai percorrer o conjunto nomes e armazenar o valor na variavel nome
    print(nome)



print(30*"=")

# USANDO FUNÇÃO ENUMERATE()

#enumerate serve para sabermos qual indice do objeto dentro do laço

nomes={"Barbara","Vanessa","Rodrigo"} # nosso conjunto
for indice,nome in enumerate(nomes): # nosso for com a função enumerate que retorna dois valores o indice e o objeto
    print(f"{indice}:{nome}")



#          IMPORTANTE : A cada execução o indice vai ser diferente a ordem vai ser diferente  
            # pois os conjuntos não garantem ordem , para manter ordem use lista