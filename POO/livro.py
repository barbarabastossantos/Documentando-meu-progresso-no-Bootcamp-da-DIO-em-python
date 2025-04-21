class Livro:
    def __init__(self,titulo,autor,ano_publicado):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicado=ano_publicado

    def exibir(self):
        print(f"Titulo do livro:  {self.titulo} \n Autor : {self.autor} \n Ano de publicação : {self.ano_publicado} \n ")

    
l1=Livro("Revolução dos Bichos", "George Orwell",1945)
l2=Livro("Meu Mundo","Roberta Alves",2000)
l3=Livro("Deus Presente","Paulo Junior",1900)

l1.exibir()
l2.exibir()
l3.exibir()
        