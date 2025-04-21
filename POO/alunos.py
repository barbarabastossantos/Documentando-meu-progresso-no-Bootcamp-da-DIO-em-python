class Alunos:
    def __init__(self,nome,idade,nota1,nota2):
        self.nome=nome
        self.idade=idade
        self.nota1=nota1
        self.nota2=nota2
        self.media=(nota1+nota2)/2

    def mostrar_boletim(self):
        print(f" Nome do aluno : {self.nome} \n Idade do aluno : {self.idade} \n Primeira nota : {self.nota1} \n Segunda nota : {self.nota2} \n Media do aluno : {self.media} \n")



a1=Alunos("Barbara",30,9,10)
a2=Alunos("Antonio",45,4,6)
a3=Alunos("Mateus",35,6,7)



a1.mostrar_boletim()
a2.mostrar_boletim()
a3.mostrar_boletim()
