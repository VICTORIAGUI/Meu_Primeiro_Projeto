def somar (a, b):
    return a + b

def exibir_resultado(a1, b2, c3):
    resultado = c3(a1,b2)
    print(f'O resultado da operação {a1} + {b2} = {resultado}')

exibir_resultado(33, 100, somar)

# Estudar mais sobre funções e parâmetros.
