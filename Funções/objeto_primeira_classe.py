def somar(a,b): # primeira função somar(a+b) recebe dois numeros
    return a+b # e retorna a soma deles  return a+b nessa função usamos o retunr pq somar precisa devolver um valor para quem chamou

def exibir_resultado(a,b,funcao): # essa segunda função recebe dois numeros e uma função como parametro
    resultado=funcao(a,b) # não usamos retunr pq não queremos calcular queremos armazenar o resultado de outra função
    #essa  função ñ precisa devolver nada pra quem chamou ela apenas chama outra função e exibe o resultado
    print(f" O resultado de {a} + {b} é {resultado}")

exibir_resultado(10,10, somar) # executa a função passando 10, 10 como valores e a função somar para fazzer o calculo