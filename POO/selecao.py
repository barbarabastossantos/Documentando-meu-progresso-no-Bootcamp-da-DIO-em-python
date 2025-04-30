print("""     
            
                        PROGRAMA DE ESTÁGIO 
      
      A Bastos LTD busca atraves de seus programas de estagio promover  a 
    educação e oportunidades para os estudantes que, satisfazendo nossos criterios ,
    ocuparão vagas de estagiarios dentro de nossas empresas.
      

""")

nome=input("Olá! Por gentileza informe seu nome : " )

curso=input(f""" 
            
             Preciso saber {nome} se você faz algum curso superior?
            
    Digite apenas  a numeração correspondente a sua resposta :

     [1] Para SIM
     [2] Para NÃO

""")

if curso == "1":
    periodo=input(f"\n Legal {nome}  , em qual periodo do curso você esta ? \n Digite apenas o numero : ")
    if periodo >= "3":
        prova=float(input(f"\n {nome}  você fez uma avaliação valendo 100 , qual foi sua nota nessa prova : "))
        if prova >= 70 :
            print(f""" 

                          {nome} PARABENS! 
                      Você correspondeu ao perfil de candidato
                      do nosso programa de estagio aqui na 
                       Bastos LTD . Se prepare para proxima etapa !
                              BOA SORTE....


""")
        else:
            print(f"Infelizmente {nome} você não corresponde ao perfil de canditado  para a vaga que buscamos... \n ")
    else:
        print(f"Infelizmente {nome} você não corresponde ao perfil de canditado para a vaga que buscamos... \n ")        
else:
    print(f"Infelizmente {nome} você não corresponde ao perfil de canditado para vaga  a que buscamos... \n")          