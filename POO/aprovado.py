class Portugues:
    def __init__(self,nota1,nota2):
        print(""" 
                  Finalizando o semestre 
              A media  minima para ser APROVADO  é de 6.
              Media inferior a 6 o aluno será REPROVADO. 
                  A direção dejesa a todos sucesso! 
              
                      VERIFICANDO...
              

""")
        self.media_portugues=(nota1 + nota2)/2

    def resultado_portugues(self):
     if self.media_portugues >= 6:
        print(f"Provado em português! Media {self.media_portugues} \n")
     else:
        print(f"Reprovado em português! Media {self.media_portugues}\n")

class Matematica:
   def __init__(self,nota1,nota2):
      self.media_matematica=(nota1+nota2)/2

   def resultado_matematica(self):
      if self.media_matematica >= 6:
         print(f"Aprovada em Matematica! Media {self.media_matematica} \n")
      else:
         print(f"Reprovada em matematica! Media {self.media_matematica}\n")
      
        

class Aluno(Portugues,Matematica):
   def __init__(self,n1_port,n2_port,n1_mat,n2_mat):
      Portugues.__init__(self,n1_port,n2_port) # o nome da classe .__init__ e como se fosse o super
      Matematica.__init__(self,n1_mat,n2_mat) # o super so funciona em herança simples pq ela  pega uma e ignora a outra 

  # def resultado_geral(self):
   #  media_geral= (self.media_portugues+ self.media_matematica)/2
  #   print(f"Media geral : {media_geral}")
  


aluno1=Aluno(7,8,5,6)
aluno1.resultado_portugues()
aluno1.resultado_matematica()
#aluno1.resultado_geral()