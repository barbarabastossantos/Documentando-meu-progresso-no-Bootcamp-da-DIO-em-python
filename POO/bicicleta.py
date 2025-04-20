class Bicicleta: # nossa classa chamada bicicleta,  classe e como se fosse um molde da bicicleta
    def __init__(self, cor,modelo,ano,valor): #  def __init__ é o metodo especial para inicializar  os atributos do objto
        self.cor= cor # self é referencia ao objeto
        self.modelo=modelo 
        self.ano=ano
        self.valor=valor
        # em outras palavras  self.cor=cor, ou qualquer outro desses , nesse caso cor significa
        # a cor dessa bicicleta(self.cor) vai receber oque a pessoa passou (cor)
        # cor, modelo, ano, valor  são os atributos


    def buzinar(self): # buzinar, parar, correr são metodos
        print("Plim plim plim ...")

    def parar(self): # para nossos metodos passamos o argumento self obrigatoriamente
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm....")

b1=Bicicleta("Vermelha", "Caloi", 2024, 900 ) # b1 e meu objeto instanciado da classe bicicleta
b1.buzinar()
b1.parar()
b1.correr()