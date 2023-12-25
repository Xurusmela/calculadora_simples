import calculadora

# Implementação da calculadora simples

while True:

# Apresentação
    print('\n\t\t\t -- Calculadora Simples --')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

    # Ler a opção de escolha do usuário
    op = int(input('\n\tOpção: '))
    if op == 1:
        print('\nSoma\n')
         # Entrada
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))

        # Processamento
        total = calculadora.soma(v1, v2)
        print(f'A soma desses números será {total}')

    elif op == 2:
        print('\nSubtração\n')

        # Entrada
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))
        total = calculadora.sub(v1, v2)
        print(f'A subtração desses números será {total}')

    elif op == 3:
        print('\nMultiplicação\n')

        # Entrada
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))
        total = calculadora.mult(v1, v2)
        print(f'A Multiplicação desses números será {total}')

    elif op == 4:
        print('\nDivisão\n')

        # Entrada
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))

        if v1 == 0 and v2 == 0:
            print('Não é possível dividir por 0')
        else:
            total = calculadora.div(v1, v2)
            print(f'A Divisão desses números será {total}')

    elif op == 5:
        print('Até mais')
        break
    else:
        print(f'Opçao {op} inválida\n')
