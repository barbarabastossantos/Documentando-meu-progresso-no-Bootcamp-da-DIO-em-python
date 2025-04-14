import datetime

#O timedelta serve para fazer operações com datas, como somar ou subtrair dias, calcular tempo entre duas datas

#Somar dias:

hoje=datetime.date.today()
amanha=hoje+datetime.timedelta(days=1)
ontem= hoje-datetime.timedelta(days=1)

print()
print("Hoje é : ", hoje)
print("Amanhã será : ", amanha)
print("Ontem foi : ", ontem)
print()


# Falta quantos dias para o natal ?

natal=datetime.date(2025,12,25) # dafinir a data do natal
faltam=natal-hoje # fiz a conta  de hoje ate o natal faltam quantos dias ?
print("Faltam ", faltam.days, "dias para o natal") # a variavel faltam que recebeu o resultado eu quero que mostre so os dias ai usei o .days
print()