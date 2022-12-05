# Funções são blocos de códigos que executam funcionalidades especificas. Normalmente são utilizadas para evitar que determinada parte do seu código seja escrito varias vezes 
# Sintaxe da função:

def nome(parametro):
    print(f'{parametro}')

nome('Valor')       

# Exemplo real, com nomes e valores
def pda(nome):
    print(f'Nome:{nome}')


pda('Erickson')
pda('Renan')
pda('Daniel')

# Outro exemplo 
def vic(anos):
    print(f"anos:{anos}")

vic('15')
vic('20')
vic('25')

# Quando a função não tiver valor (for vazia), vai imprimir o valor que tiver pré-estabelecido (valor deflo).

def idade(idade = 20):
    print(f'A idade é {idade}')

idade()   

# Quando a função não tiver NENHUM VALOR 

def cep(cep = ''):
    print(f'O seu cep é {cep}')

cep('')

# Valores Padrão com mais de um valor  
def flor(flor='Rosa', cor='Vermelha'):
    print(f'A cor da {flor} é {cor}')

flor('Orquídea', 'Azul')
flor('Cravo', 'Brano')

# Exercício: Escreva uma 

def imprime_menor(a, b):
    if a <b:
        print(a)
    elif a > b:
        print(b)
    else:
            print('Os números são iguais.')

imprime_menor(0,5)
imprime_menor(10,3)
imprime_menor(42, 42)