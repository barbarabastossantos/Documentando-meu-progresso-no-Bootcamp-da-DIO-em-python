#strftime e strptime

# SRTFTIME() OU STRING FORMAT TIME
# serve para transformar uma data/tempo(datetime) em uma string

# STRPTIME() OU STRING PARSE TIME
# serve para transformar uma string com data em um objeto  datetime

from datetime import datetime
#  importamos a classe  datetime para usarmos os metodos .now(),.strftime(), .srtptime()

agora=datetime.now()
print()
print("Data atual (datetime) : ", agora)
#criamos uma variavel chamada agora que vai receber  o metodo datetime.now() que retorna a data atual

formatada= agora.strftime("%d/%m/%Y  %H:%M:%S")
print()
print("Data formatada com o metodo strftime() : ", formatada)
print()

data_string = "16/04/2025 10:23:45"
data_obj = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
print("String convertida para datetime com o metodo strptime() : ", data_obj)
print()