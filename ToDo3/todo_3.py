from functions import separator, inputs_cand, input_notas, input_notas_new, input_continue

notas_candidatos = [[5,10,8,8], [10,7,7,8], [8,5,4,9], [2,2,2,1], [10,10,8,9]]

check = 0

while check == 0:     
    input_start = inputs_cand('\nBem-vindo(a)! Deseja verificar a compatibilidade de um candidato já cadastrado (1 a 5) ou verificar outro? \n\n1 - Candidato já cadastrado \n2 - Cadastrar notas de candidato \n3 - Encerrar programa \n\nDigite aqui: ')
    
    separator()
    
    print(f'\nVocê selecionou a opção {input_start}.') 
    
    separator()

    if input_start == 1:
        
        input_nota = input_notas()
        
        separator()
        
        input_validated = inputs_cand('Deseja verificar quais candidatos passam no teste de compatibilidade? \n\n1 - Sim \n2 - Não \n\nDigite aqui: ')
        
        if input_validated == 1:
            
            separator()
            for i in notas_candidatos:
                if(i[0] >= input_nota[0]) and (i[1] >= input_nota[1]) and (i[2] >= input_nota[2]) and (i[3] >= input_nota[3]):
                    index_candidato = notas_candidatos.index(i)
                    print(f'Candidato {index_candidato + 1}: Aprovado. Notas do candidato: e{notas_candidatos[index_candidato][0]}_t{notas_candidatos[index_candidato][1]}_p{notas_candidatos[index_candidato][2]}_s{notas_candidatos[index_candidato][3]}')
                
            separator()
            input_continue()
            
        else:
            separator()
            print('\nPrograma encerrado.\n')
            break
            
    elif input_start == 2:
        
        input_new_notas = input_notas_new()
        
        notas_candidatos.append(input_new_notas)
        separator()
        new_notas = inputs_cand(f'\nNotas do candidado incluídas com sucesso. Deseja avaliar o desempenho? \n\n1 - Sim \n2 - Não \n\nDigite aqui: ')
        
        if new_notas == 1:
            
            input_nota = input_notas()
            
            separator()
            
            for i in notas_candidatos:
                if (i[0] >= input_new_notas[0]) and (i[1] >= input_new_notas[1]) and (i[2] >= input_new_notas[2]) and (i[3] >= input_new_notas[3]):
                    index_candidato = notas_candidatos.index(i)
                    print(f'Candidato {index_candidato + 1}: Aprovado. Notas do candidato: e{notas_candidatos[index_candidato][0]}_t{notas_candidatos[index_candidato][1]}_p{notas_candidatos[index_candidato][2]}_s{notas_candidatos[index_candidato][3]}')
            
            separator()
            input_continue()

        else:
            separator()
            print('\nPrograma encerrado.\n')
            check = 1  
        
    elif input_start == 3:
        separator()
        print('\nPrograma encerrado.\n')
        check = 1