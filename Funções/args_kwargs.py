#00 IMPORTANDO O ZEN OF PYTHON
import this
# o this e um modulo do python que contem o zen of python


#01 PARTE DEFINIÇÃO DE FUNÇÃO

def exibir_poema(data_extenso,*args,**kwargs):
# def define uma função, ou sreja , um bloco de codigo reutilizavel.
# exibir_poema esse é o nome da função é o identificador que usamos para chamar-lo depois.
# (data_extenso,*args,**kwargs): , esses são os parametros da função
# data_extenso é um parametro obrigatorio pq ele é um argumento posicional,isso significa que ele ñ tem 
# um valor padrão definido na função.Se a função for chamada sem esse argumento o python ñ sabera oque colocar e dara erro.
# para tornar-lo opcional precisamos definir um valor padrão como 'data_extenso="sem titulo"'
# *args o * indica que esse parametro pode receber  varios valores posicionais.
# **kwargs o ** indica que esse parametro pode receber varios pares chave=valor(como um dicionario)

#02 PARTE CRIAÇÃO DO TEXTO A PARTIR DOS ARGUMENTOS POSICIONAIS (*args) 

  texto="\n".join(args)
# a variavel texto armazena a junçãode todos os valores e args , formando um unico  bloco de texto.
# o metodo .join(args) junta os elementos de args
# o que define  a separação entre eles e \n
# \n (quebra de linha) garante que cada item de args  fique em uma linha separada  no resultado final.

#03 PARTE FORMATANDO OS METADADOS(informações extras)

  meta_dados="\n".join([f"{chave.title()} : {valor}" for chave, valor in kwargs.items()])
# essa linha pega todas as informações  extras passasdas via kwargs(como autor e ano) e as formata para exibir
# a variavel meta_dados armazena os dados extras (autor e ano)
# "\"n".join([...]) junta os metadados em  um bloco de texto separando cada um com uma quebra de linha 
# "{chave.title()} : {valor}" formata a chave para começar com a letra maiuscula e adiciona valor
# for chave, valor in kwargs.items() percorre todos os pares chave_valor do dicionario **
 
#04 PARTE MONTANDO A MESSAGEM FINAL
  messagem = f"{data_extenso}\n\n {texto}\n\n{meta_dados}"
#{data_extenso} inseri o titulo ou data no topo
#\n\n adiciona duas quebras de linhas para separar o titulo do poema 
# {meta_dados}" inseri as informações extras 
  print(messagem)
#exibe o valor que a variavel messagem recebeu que acabamos de vê

zen_poema=this.s.split("\n")
# o .s é um atributo do modulo this 
# o this.s contem o texto do zen 
# .split("\n") e um metodo para dividir a string em varias linhas 

#06 PARTE CHAMANDO A FUNÇÃO 
exibir_poema("Zen of Python", *zen_poema, autor="Tim Peters", ano=1999)
#"Zen of Python" vai para data_extenso
# *zen_poema vai para args
#autor="Tim Peters", ano=1999 vão para kwargs