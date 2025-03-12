ativo1 = True
while ativo1:
    print('\n\n1. Previsões do Gráfico de Velocidade constante;')
    print('2. Gráfico de Velocidade Constante;')
    print('3. Previsão de Pontos de Movimento;')
    print('4. Tempo Gráfico para Colisão;')
    print('5. Problema de velocidade relativa;')
    print('6. Calculadora simples;')
    print('7. IMC (Índice de Massa Corporal);')
    print('8. Gerador de senhas aleatórias;')
    print('9. Valor do dólar em real;')
    print('\n0. Sair.\n\n')
    servico = input('Escolha uma das operações acima: ')
    escolhas = ['1', '2', '3', '4', '5', '6', '7', '8','9', '0']
    
    if servico not in escolhas:
        print('\n\nErro. Escolha uma opção válida')
    elif servico == '0':
        ativo1 = False
    elif servico == '1':
        posRef1 = float(input('Digite a posição de referência 1: \n'))
        temRef1 = float(input('Digite o valor do tempo do 1º ponto de referência: \n'))
        posRef2 = float(input('Digite a posição de referência 2: \n'))
        temRef2 = float(input('Digite o valor do tempo do 2º ponto de referência: \n'))
        temPre = float(input('Digite o valor do tempo para previsão: \n'))
            
        sit1 = (posRef2 - posRef1)/(temRef2 - temRef1)


        posInc = posRef1 - sit1 * temRef1

        posFin1 = posInc + sit1 * temPre
            
        print('Sua velocidade é de {} m/s. \nA posição inicial é {} m. O local para previsão é {} m.\n\n'.format(sit1, posInc, posFin1))
    elif servico == '2':
        lin1pon1 = float(input('Digite o 1º ponto de referência da 1º linha: '))
        lin1tem1 = float(input('Digite o valor do tempo do 1º ponto dessa linha: '))

        lin1pon2 = float(input('Digite o 2º ponto de referência da 1º linha: '))
        lin1tem2 = float(input('Digite o valor do tempo do 2º ponto dessa linha: '))

        lin2pon1 = float(input('Digite o 1º ponto de referência da 2º linha: '))
        lin2tem1 = float(input('Digite o valor do tempo do 1º ponto dessa linha: '))

        lin2pon2 = float(input('Digite o 2º ponto de referência da 2º linha: '))
        lin2tem2 = float(input('Digite o valor do tempo do 2º ponto dessa linha: '))

        lin3pon1 = float(input('Digite o 1º ponto de referência da 3º linha: '))
        lin3tem1 = float(input('Digite o valor do tempo do 1º ponto dessa linha: '))

        lin3pon2 = float(input('Digite o 2º ponto de referência da 3º linha: '))
        lin3tem2 = float(input('Digite o valor do tempo do 2º ponto dessa linha: '))

        lin1vl = (lin1pon2 - lin1pon1)/(lin1tem2 - lin1tem1)
        lin2vl = (lin2pon2 - lin2pon1)/(lin2tem2 - lin2tem1)
        lin3vl = (lin3pon2 - lin3pon1)/(lin3tem2 - lin3tem1)
        print('A velocidade da linha 1 é de {} m/s. \nA velocidade da linha 2 é de {} m/s. \nA velocidade da linha 2 é de {} m/s.\n\n'.format(lin1vl, lin2vl, lin3vl))
    elif servico == '3':
        ponto1 = float(input('Digite a posição do 1º ponto: '))
        ponto1tem = float(input('Digite o valor do tempo do 1º ponto: '))
        ponto2 = float(input('Digite a posição do 2º ponto: '))
        ponto2tem = float(input('Digite o valor do tempo do 2º ponto: '))
        tempPrev = float(input('Digite o tempo para previsão: '))

        velpontos = (ponto2 - ponto1)/(ponto2tem - ponto1tem)

        posInc2 = ponto1 - velpontos * ponto1tem

        posPrevi = posInc2 + velpontos * tempPrev
        print('A velocidade do seu problema é de {} m/s. \nA posição inicial é {} m. \nA posição prevista é de {} m.\n\n'.format(velpontos, posInc2, posPrevi))
    elif servico == '4':
        pacPos = float(input('Digite a posição do pac-man: '))
        pacVel = float(input('Digite a velocidade do pac-man: '))
        fanPos = float(input('Digite a posição do fantasma: '))
        fanVel = float(input('Digite a velocidade do fantasma: '))

        pacsit1 = (fanPos - pacPos)/(fanVel + pacVel)
        pacsit2 = (fanPos - pacPos)/(pacVel + fanVel)
        
        p1 = pacPos + pacVel * pacsit1
        p2 = pacPos + pacVel * pacsit2

        if pacVel < fanVel:
            print('\n\nO tempo para colisão é de {} s.\nO local para colisão é {} mm.'.format(pacsit1, p1))
        else:
            print('\n\nO tempo para colisão é de {} s.\nO local para colisão é {} mm.'.format(pacsit2, p2))
    elif servico == '5':
        b1Tam = float(input('Digite o tamanho do barco 1: '))
        b2Tam = float(input('Digite o tamanho do barco 2: '))

        b1Tem1 = float(input('Digite o tempo que o barco 1 encosta no poste: '))
        b2Tem1 = float(input('Digite o tempo que o barco 2 encosta no poste: '))

        b1Tem2 = float(input('Digite o tempo que o barco 1 sai de trás do poste: '))
        b2Tem2 = float(input('Digite o tempo que o barco 2 sai de trás do poste: '))

        b1vl = b1Tam / (b1Tem2 - b1Tem1)
        b2vl = b1Tam / (b2Tem2 - b2Tem1)

        veloRel1 = b1vl + b2vl
        veloRel2 = b1vl - b2vl

        direcaoOp = str(input('Os barcos se encontram? (s/n)'))
        if direcaoOp.upper == 'S':
            print('\n\nA velocidade do barco 1 é de {} m/s.\nA velocidade do barco 2 é de {} m/s.\nA velocidade relativa é de {} m/s.\n\n'.format(b1vl, b2vl, veloRel2))
        else:
            print('\n\nA velocidade do barco 1 é de {} m/s.\nA velocidade do barco 2 é de {} m/s.\nA velocidade relativa é de {} m/s.\n\n'.format(b1vl, b2vl, veloRel1))
    elif servico == '6':
        ativo2 = True
        while ativo2:
            num1 = float(input('Escolha algum número para a equação: '))
            num2 = float(input('Escolha outro número para equação (proíbido 0): '))
            operacoes = ['1', '2', '3', '4', '5', '6']
            operacao = str(input('Escolha uma das opções abaixo:\n1. Soma;\n2. Subtração;\n3. Multiplicação;\n4. Divisão;\n5. Potenciação;\n6. Radiciação.\n\n'))
            if operacao not in operacoes:
                print('Escolha uma opção válida!')
                ativo1 = False

            sum = num1 + num2
            sub = num1 - num2
            mul = num1 * num2
            div = num1 / num2
            pot = num1 ** num2
            raiz = num1 ** (1/num2)

            if operacao == '1':
                print('A soma entre {} e {} é igual a {}.'.format(num1, num2, sum))
                ativo2 = False
            elif operacao == '2':
                print('A subtração entre {} e {} é igual a {}.'.format(num1, num2, sub))
                ativo2 = False
            elif operacao == '3':
                print('A multiplicação entre {} e {} é igual a {}.'.format(num1, num2, mul))
                ativo2 = False
            elif operacao == '4':
                print('A divisão entre {} e {} é igual a {}.'.format(num1, num2, div))
                ativo2 = False
            elif operacao == '5':
                print('{} elevado à {} é igual a {}.'.format(num1, num2, pot))
                ativo2 = False
            elif operacao == '6':
                print('{} dentro de uma raiz de {} de potencia é igual à {}.'.format(num1, num2, raiz ))
                ativo2 = False
    elif servico == '7':
        
        altura = float(input('Qual sua altura? (m)\n'))
        peso = float(input('Quanto você pesa? (kg)\n'))

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print('Você está: abaixo do peso ideal.')
        elif 18.5 <= imc <= 24.9:
            print('Você está: com peso normal.')
        elif 25 <= imc <= 29.9:
            print('Você está: sobrepeso.')
        elif imc > 30:
            print('Você está: obeso.')
    elif servico == '8':
        import random
        import string

        def gerar_senha():
            # Solicitar o comprimento da senha
            comprimento = int(input("Digite o comprimento da senha: "))

            # Solicitar se deseja incluir números, caracteres especiais e letras maiúsculas
            incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
            incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
            incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

            # Definir os caracteres que podem ser usados
            caracteres = string.ascii_lowercase  # Letras minúsculas sempre

            if incluir_numeros:
                caracteres += string.digits  # Números 0-9
            if incluir_maiusculas:
                caracteres += string.ascii_uppercase  # Letras maiúsculas
            if incluir_especiais:
                caracteres += string.punctuation  # Caracteres especiais como !@#$%

            # Gerar a senha aleatória
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

            # Exibir a senha gerada
            print(f"\nSua senha gerada é: {senha}")

        # Chamar a função
        gerar_senha()
    elif servico == '9':
        