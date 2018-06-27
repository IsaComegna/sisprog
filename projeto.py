# -*- coding: utf-8 -*-
import simulador_mvn
import pandas as pd
from tabulate import tabulate
import numpy as np

global mem
ci = 0
ac = 0 #inicia em 0


def executar(arquivo):#motor de eventos da execucao de programas
    arquivo_assembly = montador_passo1(arquivo)
    simulador_mvn(arquivo_assembly)

def carrega_loader():
    file = open("loader.txt", 'r')
    arroba = file.readline() #le linha de @
    inic = file.readline() #le uma linha
    linha = file.readline() #le uma linha
    i = 0
    linha = file.readline() #le uma linha
    while (linha != "DADO"):
        if (linha[2:4] == "COUNT"):
            mem[i] = 31
        elif (linha[2:4] == "DADO"):
            mem[i] = 15
        else:
            mem[i] = linha[:2]
            mem[i+1] = linha[2:4]
        linha = file.readline() #le uma linha
    linha = file.readline() #le uma linha
    while (linha != "EXEC"):
        if (linha[2:4] == "COUNT"):
            mem[i] = 31
        elif (linha[2:4] == "EXEC"):
            mem[i] = 36
        else:
            mem[i] = linha[:2]
            mem[i+1] = linha[2:4]
        linha = file.readline() #le uma linha
    linha = file.readline() #le uma linha
    while (linha != "CEM"):
        if (linha[2:4] == "INIC"):
            mem[i] = 0
        else:
            mem[i] = linha[:2]
            mem[i+1] = linha[2:4]
        linha = file.readline() #le uma linha

#Interpretador de comandos
def interpretador(comando, user):
    #motor de eventos de input de comandos

    if (comando =='$DEL' or comando == '$RUN'):
        arquivo = raw_input('Digite o nome do arquivo: ')

    if (comando == '$DIR'):
        comandos_df = pd.read_csv('arquivos.csv')
        user_archives = comandos_df.loc[comandos_df['usuario']==user]
        print(tabulate(user_archives, headers='keys', tablefmt='psql'))
        lista_comandos(user)

    if (comando == '$DEL'):
        print('\nDeletando programa')
        comandos_df = pd.read_csv('arquivos.csv')
        user_files = comandos_df.loc[comandos_df['usuario']==user]
        comandos_df.loc[user_files.loc[comandos_df['arquivo']==arquivo].index.values]=0
        comandos_df.to_csv('arquivos.csv', index=False)
        lista_comandos(user)

    if (comando == '$END'):
        print('Fim do programa')
        main()
    if (comando == '$RUN'):
        print('O programa sera executado')
        lista_comandos(user)
        carrega_loader()
        executar(arquivo)


def lista_comandos(user):
    print('')
    print('Lista de comandos disponiveis')
    print('$DIR: informa os seus programas disponiveis')
    print('$DEL: remove do sistema um programa do usuario')
    print('$RUN: inicia a execucao de um dos programas')
    print('$END: encerra a operacao do SO e reporta informacoes coletadas')
    print('')
    print('')
    comando = raw_input('Digite seu comando: ')
    while(comando != '$DIR' and comando!='$DEL' and comando!='$RUN' and comando!='$END'):
        print('Comando nao encontrado. \n')
        comando = raw_input('Digite seu comando: ')
    interpretador(comando, user)


def main():
    print('')
    print('')
    print('-------------------------------------------------------------')
    print('Sistema de desenvolvimento de programas em linguagem simbolica')
    print('-------------------------------------------------------------')
    print('')
    print(' ---Faca seu login---')
    print('Lista de usuarios ja cadastrados:')
    users_df = pd.read_csv('usuarios.csv')
    print(tabulate(users_df, headers='keys', tablefmt='psql'))

    print('')
    print('')
    print('Opcoes:')
    print('1 para novo usuario')
    print('2 para usuario em lista de usuarios')
    opcao = int(input())

    if (opcao==1):
        print('')
        print('Escolha o nome de usuario:')

    else:
        print('')
        print('Nome de usuário:')
    user = raw_input('') #variavel do nome do usuario
    if (opcao==1):
        users_df.loc[users_df.index.size] = [user]
        users_df.to_csv('usuarios.csv', index=False)
    print('Login concluido com sucesso')
    lista_comandos(user)

main()
