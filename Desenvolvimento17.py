def cabecario(msg):
    print('=-' * 30)
    print('{:.^60}'.format(msg))
    print('=-' * 30)

def calculadora():
      while True:
            try:
                operador = int(input('\033[4;34m SELECIONE A OPÇÃO: \033[m\n[1] para soma\n[2] para subtração\n[3] para multiplicação\n[4] para divisão\n[0] para Sair do Programa\n>>>> '))
                if operador == 0:
                    print('\033[1;31mSAINDO DO PROGRAMA. \033[m\n')
                    break
                elif operador >= 5:
                    print('\033[1;31mOPÇÃO INVÁLIDA \033[m\n')
                    continue
                elif operador == 1:
                    num1 = float(input('Informe o primeiro número: '))
                    num2 = float(input('Informe o segundo número: '))
                    res = num1 + num2
                    print('\033[7;30;42m {} + {} = {:.1f} \033[m\n'.format(num1, num2, res))
                elif operador == 2:
                    num1 = float(input('Informe o primeiro número: '))
                    num2 = float(input('Informe o segundo número: '))
                    res = num1 - num2
                    print('\033[7;30;42m {} - {} = {:.1f} \033[m\n'.format(num1, num2, res))
                elif operador == 3:
                    num1 = float(input('Informe o primeiro número: '))
                    num2 = float(input('Informe o segundo número: '))
                    res = num1 * num2
                    print('\033[7;30;42m {} x {} = {:.1f} \033[m\n'.format(num1, num2, res))
                elif operador == 4:
                    num1 = float(input('Informe o primeiro número: '))
                    num2 = float(input('Informe o segundo número: '))
                    res = num1 / num2
                    print('\033[7;30;42m {} / {} = {:.1f} \033[m\n'.format(num1, num2, res))
            except:
                print('\033[1;31mOPÇÃO INVÁLIDA \033[m\n')

cabecario('DESENVOLVIMENTO 17')
calculadora()
