# PROJETO: BACKUP VERSIONAMENTO DE PROJETO
___
## RESUMO
+ O programa tem como função efetuar um backup de um diretorio inteiro para um segundo diretório, podendo até mesmo este diretório não estar fisicamente no pc mais sim na rede.
___
## ARQUIVO DE CONFIGURAÇÃO 
+ O programa é constituido de dois arquivos sendo um deles um arquivo em formato .txt tendo a função de configuração;

### CONFIGURAÇÃO
+ O arquivo de configuração do programa deve conter 3 linhas de texto:
    linha_1| __contém o endereço diretório de origem contendo os arquvis para backup__
    :---|:---
    __linha_2__| __contém o endereço do diretorio de destino__
    __linha_3__| __contem o horario em que o backup ocorrerá__ 

+ Observação o valor do horario de backup pode sobrer um atraso de até 60 segundos, decisão tomada para não consumir em excesso o processamento do computador
___
## Correções 
- [ ] Alterar o nome fixo que é criado na pasta de destino