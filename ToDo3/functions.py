from turtle import end_fill

def separator():
    
    print('\n---------------------------------------------------------------------------------------------------------')
    

def inputs_cand(input_msg):
    
    digit = False
    valor = 0
    while True:
        message = str(input(input_msg))
        if message.isnumeric():
            valor = int(message)
            digit = True
        else:
            print('\nDigite um valor de entrada válido, entre 0 e 10: ')
        if digit:
            break
    return valor

def input_notas():
    input_one = inputs_cand('\nDigite a nota mínima do candidato para a etapa de entrevistas. Digite aqui: ')
    print(f'Resultado do candidato na etapa de entrevista: {input_one}')
    
    input_two = inputs_cand('\nDigite a nota mínima do candidato para a etapa do teste teórico. Digite aqui: ')
    print(f'Resultado do candidato na etapa do teste teórico: {input_two}')
    
    input_three = inputs_cand('\nDigite a nota mínima do candidato para a etapa do teste prático. Digite aqui: ')
    print(f'Resultado do candidato na etapa do teste prático: {input_three}')
    
    input_four = inputs_cand('\nDigite a nota mínima do candidato para a etapa de avaliação de soft skills. Digite aqui: ')
    print(f'Resultado do candidato na etapa de avaliação de soft skills: {input_four}')
            
    new_list = [input_one, input_two, input_three, input_four]
    print(f'\nNotas de corte: e{new_list[0]}_t{new_list[1]}_p{new_list[2]}_s{new_list[3]}')
    
    return new_list


def input_notas_new():
    input_one_2 = inputs_cand('\nDigite a nota do candidato para a etapa de entrevistas. Digite aqui: ')
    print(f'Resultado do candidato na etapa de entrevista: {input_one_2}')
            
    input_two_2 = inputs_cand('\nDigite a nota do candidato para a etapa do teste teórico. Digite aqui: ')
    print(f'Resultado do candidato na etapa do teste teórico: {input_two_2}')
    
    input_three_2 = inputs_cand('\nDigite a nota do candidato para a etapa do teste prático. Digite aqui: ')
    print(f'Resultado do candidato na etapa do teste prático: {input_three_2}')
    
    input_four_2 = inputs_cand('\nDigite a nota do candidato para a etapa de avaliação de soft skills. Digite aqui: ')
    print(f'Resultado do candidato na etapa de avaliação de soft skills: {input_four_2}')
    
    new_list = [input_one_2, input_two_2, input_three_2, input_four_2]
    print(f'\nNotas do candidato: e{new_list[0]}_t{new_list[1]}_p{new_list[2]}_s{new_list[3]}')
    
    return new_list

def input_continue():
    
    check = inputs_cand('\nDeseja realizar outra operação? \n\n1 - Sim \n2 - Não \n\nDigite aqui: ')
            
    if check == 1:
        check = 0
    elif check == 2: 
        print('\nPrograma encerrado.\n')
        exit()
    
    return check