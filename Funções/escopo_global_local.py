salario = 2000 # criamos uma variavel GLOBAL pois ela foi definida fora de qualquer função na raiz do programa

#criando função...

def salario_bonus(bonus):
    global salario # usando a palavra reservada gobal estamos dizendo que queremos usar a variavel salario que esta fora da função no nosso escopo global
    salario += bonus # pegamos o valor da variavel gobal salario e somamos com o valor recebiido pelo parametro bonus, essa e a forma abreviada de salario=salario+bonus
    return salario  # a função vai retornar o novo valor do salario 

salario_com_bonus=salario_bonus(500) # chamamos a função e passamos o bonus de 500
print(salario_com_bonus) # mostramos o novo salario com bonus