nome = "baRbarA"

print(nome.title())
#title coloca a primeira letra em maiuscula e o resto minuscula

print(nome.upper())
#upper tudo maiusculo

print(nome.lower())
#lower tudo minusculo

print(nome.center(15,"="))
print(nome.center(15))
#center centraliza a string, center tem dois argumentos 
#primeiro indica quantos espaços eu quero o segundo e opcional
#segundo mostra o caractr que vc deseja por a esquerda e direita

print("." .join(nome))
#usado para junção o join vai passar iten a iten e colocar o caracter que vc deseja
#o join e muito ultil em listas 

nome2 = "    Antonio    "

print(nome2)
print(nome2.strip())
#strip elimina todos os espaços em branco

print(nome2.lstrip())
#elimina os espaços da esquerda

print(nome2.rstrip())
#elimina os espaços da direita