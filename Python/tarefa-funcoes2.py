# Escreva uma função que, dado um número nota representando nota nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def imprime_nota(nota):
    if nota >= 9:
        print(f'A sua nota é A!')
    elif nota >= 7:
        print(f'Sua nota é B!')
    elif nota >= 5:
        print(f'Sua nota é C!')
    elif nota >= 3:
        print(f'Sua nota é D!')
    elif nota >= 2:
        print(f'Sua nota é E!')
    elif nota ==0:
        print(f'Sua nota é F!')


imprime_nota(9)
imprime_nota(7)
imprime_nota(5.8)
imprime_nota(4)
imprime_nota(3)
imprime_nota(2)
imprime_nota(0)