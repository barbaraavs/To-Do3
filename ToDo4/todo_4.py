import re
from encodings import utf_8
from functions import input_number, input_text, separator

print('Bem-vindo(a) ao sistema Match! #Contratado.')

list_candidato = []

input_candidato = input_number('\nQuantos candidatos(as) deseja cadastrar? Digite aqui: ')

for i in range(1, input_candidato + 1, 1):   
    list_number = i
    list_candidato.append(list_number)

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
    
    list_analista = []
    
    for i in range(input_candidato):
        str_analista = 'Analista de Dados/ '
        str_analista = str_analista * input_candidato
        str_analista = re.sub(r"([a-z])([A-Z])", r"\1 \2", str_analista)
        str_analista = str_analista.split('/ ')
        str_analista.pop()
        list_analista = str_analista
        print(list_analista)
    
    dict_analista = {'Analista de Dados': ['Python', 'Power BI', 'SQL', 'Boa comunicação']}
    print(f'\nVaga de interesse: {input_vaga_dict[1]}')
elif input_vaga == 2:
    list_cientista = ['Cientista de Dados']
    dict_cientista = {'Cientista de Dados': ['Python', 'Banco de dados', 'Machine Learning', 'Resolução de problemas', 'Estatística']}
    print(f'\nVaga de interesse: {input_vaga_dict[2]}')
else:
    print('Entrada inválida')
    
separator()

input_curriculo = input_number('\nCurrículo: o que deseja fazer? \n\n1 - Inserir texto para análise \n2 - Ler arquivo de texto (.txt) \n\nDigite aqui: ')

separator()

list_input_curriculo_text = []

if input_curriculo == 1:
    
    for i in range(input_candidato):
        input_curriculo_text = input('Insira o currículo do candidado: ') 
        list_input_curriculo_text.append(input_curriculo_text)
        
    breakpoint()
    
elif input_curriculo == 2:
    print('\nORIENTAÇÕES: \n\n- Arquivo no formato .txt; \n- Nome do arquivo: curriculo.txt')
    separator()
    arq_txt = open("C:\\Users\\barba\\OneDrive\\Área de Trabalho\\Arquivos\\Resilia\\data_analytics\\ToDo-Resilia\\ToDo4\\curriculo.txt", encoding='utf-8')
    print(arq_txt.read())
    breakpoint()
    if input_vaga == 1:
        list_0 = list(zip(list_candidato, list_names, list_analista, list_input_curriculo_text))
        
        print(list_0)