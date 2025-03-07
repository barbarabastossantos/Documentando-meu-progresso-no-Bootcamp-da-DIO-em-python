def salvar_carro(marca,modelo,ano,placa):
    print(f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")
 
    
#              CHAMANDO A FUNÇÃO 
 
salvar_carro("Fiat", "Palio", 1999, "ABC1234")
#01  Chamndo a função com valores fixos


salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC1234")
#02   Chamando a função com argumentos nomeados
# Isso significa  que ao inves de passar os valores na ordem dos parametros 
# estamos associando explicitamente  cada valor ao nome do parametro

salvar_carro(**{"marca":"Fiat","modelo":"Palio", "ano":1999, "placa":"ABC1234"})
# 03   Chamando a função com dicionario
# Permite passar um dicionario de argumentos oque pode ser util quando os valores vem de uma
# fonte externa , como banco de dados ou api

  
 
