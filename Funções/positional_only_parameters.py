#               CODIGO

# Essa função chamada criar_carro(),vai receber varias informações sobre o carro
# modelo, ano, placa, marca, motor e combustivel
# Mas o detalhe importante aqui é o "/" no meio dos parametros
# esse simbolo faz com que alguns parametros só possam ser passados por posição e não por nome
# isso é chamado de "positional-only parameters"(parametros apenas posicionais)


def criar_carro(modelo,ano,placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio",1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina") #valido

#criar_carro(modelo="Palio",ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina") #invalido



#           COMENTANDO O CODIGO

#def criar_carro(..) cria uma função chamada criar_carro
# modelo,ano,placa, são os três primeiros paramentros da função
# /: esse simbolo barra divide os parametros em dois grupos :
# Antes da barra -> modelo,ano,placa que são posicionais
# Depois da barra -> marca, motor, combustivelque podem ser passados por nome ou por posição


#             CHAMANDO A FUNÇÃO

# exemplo valido : 

# "Palio" foi passado na posição de modelo (correto)
# 1999 foi passado na posição de ano (correto)
# "ABC-1234" foi passado na posição de placa ( correto)
# marca="fiat", motor"1.0", combustivel="gasolina" esses passamos por nome e como esses parametros 
# estão depois da barra isso e permitido

# Positional Only significa que certos parametros so podem ser passados por posição
# a barra e o que define isso no python. 
# Tudo que vem antes da barra deve ser passado sem nome, apenas na ordem correta

