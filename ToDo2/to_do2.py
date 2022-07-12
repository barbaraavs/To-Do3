check = 0

while check == 0:
    print('\nCALCULADORA DE TAMANHO DE AMOSTRA\n')

    print('---------------------------------------------------------------------------------------------------')

    populacao = input('\nDigite o tamanho da população: ')

    while not populacao.isdigit():
        populacao = input('\nEntrada inválida. Digite o tamanho da população: ')

    populacao = int(populacao)
        
    grau_Confianca = input('Digite o grau de confiança da amostra: 80% = 80 || 85% = 85 || 90% = 90 || 95% = 95 || 99% = 99 || Digite aqui: ')

    while not grau_Confianca.isdigit() or int(grau_Confianca) not in [80, 85, 90, 95, 99]:
        grau_Confianca = input('\nEntrada inválida. Digite o grau de confiança da amostra: \n80% = 80\n85% = 85\n90% = 90\n95% = 95\n99% = 99\nDigite aqui: ')

    grau_Confianca = int(grau_Confianca)

    if grau_Confianca > 79:
        if grau_Confianca == 80:
            escore_z = 1.28
        elif grau_Confianca == 85:
            escore_z = 1.44
        elif grau_Confianca == 90:
            escore_z = 1.65
        elif grau_Confianca == 95:
            escore_z = 1.96
        elif grau_Confianca == 99:
            escore_z  = 2.58
    else:
        print('\nNão há amostra suficiente para o grau de confiança informado.\n')
        
    margem_Erro = input('Digite a margem de erro da amostra (digite um número inteiro, entre 1 e 100. Exemplo: 10 equivale a 10%): ')

    while not margem_Erro.isdigit():
        margem_Erro = input('\nEntrada inválida. Digite a margem de erro da amostra: ')
        
    margem_Erro = int(margem_Erro)

    desvio_Padrao = (50 / 100)

    escore_Quadrado = (escore_z ** 2)
    erro_Quadrado = ((margem_Erro / 100) ** 2)
    erro_Populacao = round(float(erro_Quadrado * populacao),2)

    parte_Um = round(float((escore_Quadrado * desvio_Padrao * (1 - desvio_Padrao)) / erro_Quadrado),2)
    parte_Dois = round(float(1 + ((escore_Quadrado * desvio_Padrao * (1 - desvio_Padrao)) / erro_Populacao)),2)
    parte_Tres = int(parte_Um /parte_Dois)

    print('\n---------------------------------------------------------------------------------------------------\n')
    print(f'Dados para cálculo\n')

    print(f'- Tamanho da população: {populacao}')
    print(f'- Grau de confiança: {grau_Confianca}%')
    print(f'- Escore z: {escore_z}')
    print(f'- Margem de erro: {margem_Erro}%')
    print(f'- Desvio Padrão pré-determinado: 50%')

    print('\n---------------------------------------------------------------------------------------------------\n')
    print(f'- Tamanho da amostra: {parte_Tres}')
    print('\n---------------------------------------------------------------------------------------------------\n')

    check1 = input(f'Deseja realizar outro cálculo?\n1 - Sim\n2 - Não\nDigite: ')

    while not check1.isdigit():
        check1 = input('\nEntrada inválida. Digite 1 - Sim || 2 - Não\nDigite: ')

    check1 = int(check1)
    
    if check1 == 1:
        check = 0
    else:
        check = 1
        print('\nPrograma finalizado.\n')      
    