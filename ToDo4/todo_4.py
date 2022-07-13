from functions import input_number, input_text, separator

print('Bem-vindo(a) ao sistema Match! #Contratado.')

input_candidato = input_number('\nQuantos candidatos(as) deseja cadastrar? Digite aqui: ')

separator()

list_names = []

for i in range(input_candidato):
   input_name = input_text('Qual o nome do(a) candidato(a): ') 
   list_names.append(input_name)

list_replace = str(list_names).replace('[','').replace(']','').replace("'",'')

print(f'\nCandidatos Cadastrados: {list_replace}')

separator()

input_vaga = input_number('\nQual a vaga de interesse? \n\n1 - Analista de Dados \n2 - Cientista de Dados \n\nDigite aqui: ')
input_vaga_dict = {1:'Analista de Dados', 2:'Cientista de Dados'}

if input_vaga == 1:
    dict_analista = {'Analista de Dados': ['Python', 'Power BI', 'SQL', 'Boa comunicação']}
    print(f'\nVaga de interesse: {input_vaga_dict[1]}')
elif input_vaga == 2:
    dict_cientista = {'Cientista de Dados': ['Python', 'Banco de dados', 'Machine Learning', 'Resolução de problemas', 'Estatística']}
    print(f'\nVaga de interesse: {input_vaga_dict[2]}')
else:
    print('Entrada inválida')
    
separator()

input_curriculo = input_text('\nInsira o texto com o resumo do currículo: ')

separator()
