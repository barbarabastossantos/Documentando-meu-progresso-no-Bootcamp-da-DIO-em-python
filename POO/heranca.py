# classe mãe- Pessoa

class Pessoa:
    def __init__(self,nome,cpf,nascimento):
        self.nome=nome
        self.cpf=cpf
        self.nascimento=nascimento

# filha 1 - Aluno

class Aluno(Pessoa):
    def __init__(self,nome,cpf,nascimento,matricula):
        super().__init__(nome,cpf,nascimento)
        self.matricula=matricula

# filha 2 - Professor

class Professor(Pessoa):
    def __init__(self, nome, cpf, nascimento,salario):
        super().__init__(nome, cpf, nascimento)
        self.salario=salario

# filha 3 - Cordenador

class Cordenador(Pessoa):
    def __init__(self, nome, cpf, nascimento,setor):
        super().__init__(nome, cpf, nascimento)
        self.setor=setor



# A classe mãe Pessoa guarda as informações  comuns a todos 
# As classes filhas só precisam dizer  o que é diferente nelas

filha1=Aluno("Barbara","99999999","16/04/1995","555555555")
print(f" Veio da classe mãe o nome : {filha1.nome} \n Veio da classe filha 1 a matricula : {filha1.matricula} \n")

filha2=Professor("Antonio","7777777","16/05/1980",800000)
print(f" Veio da classe mãe o cpf : {filha2.cpf} \n Veio da classe filho 2 o salario : {filha2.salario:.2f} \n")

filha3=Cordenador("Eliana","55555555","30/03/1959", "Escolar")
print(f" Veio da classe mãe o data de nascimento : {filha3.nascimento} \n Veio da classe filha 3 a setor : {filha3.setor}")