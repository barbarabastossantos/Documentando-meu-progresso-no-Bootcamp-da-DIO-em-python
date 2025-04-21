class Biblioteca:
    def __init__(self,titulo,autor,ano,numero_paginas,nota1,nota2):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        self.numero_paginas=numero_paginas
        self.nota1=nota1
        self.nota2=nota2
        self.media=(nota1+nota2)/2

    def exibir_inf(self):
        print(f"""     Avaliação do Livro
              
              Titulo do livro : {self.titulo}
              Aultor do livro : {self.autor}
              Ano de lançamento : {self.ano}
             Numero de paginas : {self.numero_paginas}
             Primeira avaliação: {self.nota1}
             Segunda avaliação : {self.nota2}
             Media do livro  {self.titulo} é de {self.media}


              """)
        

l1=Biblioteca("Ensaio sobre  a cegueira", "Jose Saramago", 1995, 310, 10, 9)
l2=Biblioteca("Jude o obscuro", "david hass", 1997, 400, 10,10)
l3=Biblioteca("Stoner","hugo fgts",2000, 500, 9,8)

l1.exibir_inf()
l2.exibir_inf()
l3.exibir_inf()