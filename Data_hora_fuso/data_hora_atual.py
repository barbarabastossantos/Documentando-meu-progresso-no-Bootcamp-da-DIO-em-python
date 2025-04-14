import datetime

#criar data e hora:

data_hora=datetime.datetime(2025,4,20,20,40,3)
print("\n", data_hora, "\n")

# pegar data e hora atual :

agora=datetime.datetime.now()
print("Agora são :", agora, "\n")

#acessando partes da data e hora:

print("Estamos no ano : ", agora.year)
print("No mês : ", agora.month)
print("No dia :", agora.day)
print("As horas : ", agora.hour)
print("Os minutos: ", agora.minute)
print("Os segundos : ", agora.second)
print()