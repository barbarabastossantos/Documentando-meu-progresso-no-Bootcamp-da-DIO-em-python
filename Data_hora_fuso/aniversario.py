import datetime

dia= datetime.datetime.now()
print(dia)

formatada=dia.strftime("%d/%m/%Y, %H:%M:%S")
print(formatada)

formt_2=datetime.datetime.strptime(formatada, "%d/%m/%Y, %H:%M:%S")
print(formt_2)

aniversario=datetime.datetime(2026,4,16)
print(aniversario)

comemorar=dia-aniversario
print("Falta ", comemorar.days ," dias para você comemorar seu aniversario de novo Bárbara")

