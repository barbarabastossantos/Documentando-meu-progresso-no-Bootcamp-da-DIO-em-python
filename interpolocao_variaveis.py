nome = "Barbara"
idade = 30
profissao = "Programadora"
sexo = "Feminino"
cidade = "Barra do Choça"
telefone = 779999999


print(f" Me chamo {nome} tenho {idade} anos de idade . \n Traballho como {profissao} sou do sexo {sexo}. \n moro em {cidade} e meu numero de telefone é {telefone}")

#Em python temos três formas de interpolar variaveis em strigs :
# Primeira é usando o sinal %
# Segunda é ultizando  o9 metodo format
# Terceira é utilizando f-string
# f-string é a mais usada  as outras duas estão em desuso


PI = 3.14159

print(f" Valor de PI : {PI:.2f}")
# Passamos um argumento o valor do pi vai ter duas casas decimais 

print(f"Valor de PI : {PI:10.2f}")
# Agora passamos dois argumentos , vai ter dez espaços e duas casas decimais 