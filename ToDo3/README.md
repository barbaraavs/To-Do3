# **#TODO3: DEU MATCH 👊🏻**
Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade de um candidato com uma vaga de acordo com seu resultado nas etapas do processo seletivo. Para isso foi criado um teste que devolve uma string no seguinte formato: **eX_tX_pX_sX** (sendo que cada X é substituído pela avaliação da pessoa em uma das etapas do processo - entrevista, teste teórico, teste prático e avaliação de soft skills).  
  
Temos a seguinte lista de candidatos como exemplo e os resultados:  

- **Candidato 1**: e5_t10_p8_s8  
- **Candidato 2**: e10_t7_p7_s8  
- **Candidato 3**: e8_t5_p4_s9  
- **Candidato 4**: e2_t2_p2_s1  
- **Candidato 5**: e10_t10_p8_s9

## Objetivo

Criar com Python uma lista para armazenar esses resultados (e outros resultados que quiser no mesmo formato, o código precisa funcionar para qualquer lista que seja inserida nesse formato) e depois uma função que busca o candidato de acordo com os critérios digitados pelo usuário. O usuário vai informar qual a nota mínima de e, t, p e s que ele deseja buscar, nossa aplicação deve listar quem são os candidatos disponíveis com nota maior ou igual a essas informadas pelo usuário.

## Exemplo:

Ao buscar por alguém com resultados **'4,4,8,8'**, por exemplo, vamos receber que os candidatos **1** e **5** atendem a esse critério, foram bem no teste prático e apresentaram um ótimo nível de soft skills!

## Autora 👩🏻

Engenheira de Energia formada pela Universidade Positivo e estudante de *Data Analytics* na Resilia Educação.