import os
from datetime import date
import shutil
import schedule
import time

# lê horario do sistema e converte formato string 
def timeSystem():
    '''
    Retorna DIA/MÊS/ANO DO SISTEMA
    '''
    return str(date.today())

#verifica se o arquivo de configuração existe, caso negativo o cria na pasta selecionada
def searchfileConfig():
    '''
    Verifica se o arquivo de configuração do sistema existe, caso negativo o mesmo é criado. 
    '''
    #indica a pasta em que o script esta sendo executado
    dir_path = os.getcwd() 
    #lista todos os arquivos do diretório
    files_array = os.listdir(dir_path) 
    #verifica se o arquivo de configuração o script existe no diretório de execução
    if 'configcopy.txt' in files_array:
       print('Arquivo de configuracao encontrado') 
    else:
        newFile = False
        while(1):
            try:
                new_file = open('configcopy.txt','a')
                new_file.close()
                newFile = True
            except:
                print('O arquivo de configuracao não pode ser criado')
            if newFile:
                print('Arquivo de configuracao encontrado')
                break


def testConfig():
    '''
    Verifica se o arquivo de configuração possui ao menos duas linhas de valores, caso negativo requisita os endereços dos diretorios do usuário
    '''
    arquivo = open('configcopy.txt','r')
    lista = arquivo.readlines()
    arquivo.close()
    if len(lista) == 3:
        print('Arquivos de configuração verificados')
    else:
        addOrigin = (input('INSIRA O ENDEREÇO DE ORIGEM DA PASTA DO PROJETO: '))
        addDestiny = (input('INSIRA O ENDEREÇO DA PASTA DE DESTINO DO PROJETO: '))
        timeBackup = (input('INFORME A HORA DE BACKUP (FORMATO 00:00 ATÉ 23:59): '))
        addOrigin = addOrigin + '\n'
        addDestiny = addDestiny + '\n'
        #addOrigin = addOrigin.replace("\\", '\\\\') + '\n'
        #addDestiny = addDestiny.replace("\\", '\\\\') + '\n'
        arquivo = open('configcopy.txt','w')
        arquivo.write(addOrigin)
        arquivo.write(addDestiny)
        arquivo.write(timeBackup)
        arquivo.close()
       
def copyFiles():
    arquivo = open('configcopy.txt','r')
    address = arquivo.readlines()
    for i in range(2):
        address[i] = address[i].replace("\n","")
    destination = shutil.copytree(address[0], address[1]+"matrix2_"+timeSystem())
    print(destination)

def versionamento():
    #Armazena data do sistema
    date_today = timeSystem()
    print(date_today)
    #Verifica se o arquivo de configuração existe, caso negativo o cria
    searchfileConfig()
    #Verifica se as configurações existem, caso contrario cria-se as configurações
    testConfig()
    #efetua a cópia do diretório de origem para o diretório de destino
    copyFiles()

def retTimeBackup():
    arquivo = open('configcopy.txt','r')
    _array = arquivo.readlines()
    return _array[2]
#############################################################################################

#schedule.cada.tempo.fazer
schedule.every().day.at(retTimeBackup()).do(versionamento)

while 1:
    schedule.run_pending()
    time.sleep(60)