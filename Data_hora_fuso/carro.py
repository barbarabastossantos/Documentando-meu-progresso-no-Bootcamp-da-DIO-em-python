import  datetime


tipo_carro="p" # pode ser p,m,g

tempo_p= 30 
tempo_m= 45
tempo_g= 60

# quando formos por dentro da condicional  não podemos por tempo_p pq o python não vai entender
# ele precisa saber 30 oque? minutos? segundos? dias?
# o timedelta() espera :
# datetime.timedelta(minutes=)
# datetime.timedelta(hours=)
# datetime.timedelta(days=)
# o timedelta() não aceita uma data como argumneto, ele quer saber quanto tempo você quer adicionar
#  datetime.timedelta(minutes= tempo_p) no caso tempo_p vale 30 
# logo o python entende dessa forma -> datetime.timedelta(minutes=30)

chegada=datetime.datetime.now()

if tipo_carro == "p":
   retirada= chegada+datetime.timedelta(minutes=tempo_p) 
   print("Horario de chegada : ", chegada)
   print("Horario de retirada : ", retirada)
elif tipo_carro == "m":
    retirada= chegada+datetime.timedelta(minutes=tempo_m)
    print("Horario de chegada : ", chegada)
    print(" Horario de retirada : ",retirada)
else:
    retirada= chegada+datetime.timedelta(minutes=tempo_g)
    print("Horario de chegada : ", chegada)
    print("Horario de retirada e : ", retirada)