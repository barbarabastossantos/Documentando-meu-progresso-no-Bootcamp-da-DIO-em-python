def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def dividir(a,b):
    return a/b

def multiplicar(a,b):
    return a*b

def expressao(a,b):
    return a*2-3+b/2

def exibir_resultado(a,b,funcao):
    resultado=funcao(a,b)
    print(f" O resultado da operação é {resultado}")

exibir_resultado(10,5,expressao)
exibir_resultado(10,5,somar)
exibir_resultado(10,5,subtrair)
exibir_resultado(10,5,dividir)
exibir_resultado(10,5,multiplicar)