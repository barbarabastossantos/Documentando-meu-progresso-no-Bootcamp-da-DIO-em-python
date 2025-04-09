import datetime

d=datetime.datetime(2023,4,8,21,2)
print("Hoje é " , d)
#criamos uma data

d=d+datetime.timedelta(weeks=1)
# vai adicionar em d mais uma semana
print("Daqui uma semana será " ,d)