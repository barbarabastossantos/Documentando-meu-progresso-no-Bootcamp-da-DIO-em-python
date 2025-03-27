# Os metodos da tuplas são menos dos que os da lista pois   a tupla uma vez criada não pode ser alterada

# ().count -> conta quantas ocorrencias  o item teve dentro da tupla 
# ()len -> retorna o tamanho total da tupla 
#().index -> te mostra qual o indice do item na tupla


cores=("vermelho", "azul", "preto","vermelho","roxo","azul","vermelho","verde")

print(cores)
print(20* "=")
print("A cor vermelha aparece na tupla ", cores.count("vermelho")," vezes.")
print(20* "=")
print("A cor azul aparece na tupla ", cores.count("azul")," vezes.")
print(20* "=")
print("A cor verde aparece na tupla ", cores.count("verde")," vezes.")
print(20* "=")
print("O tamanho total da tupla cores é de " , len(cores), " itens.")
print(20* "=")

nome=("Barbara", "Vitor", "Antonio", "Eliana", "Maria")
print(nome)
print(20* "=")
print("Barbara esta no indice ", nome.index("Barbara"))
print("Maria esta no indice ", nome.index("Maria"))
print("Antonio esta no indice ", nome.index("Antonio"))
print("Eliana esta no indice ", nome.index("Eliana"))
print("Vitor esta no indice ", nome.index("Vitor"))