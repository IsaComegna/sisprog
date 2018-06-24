# -*- coding: utf-8 -*-
import simulador_mvn
import pandas as pd
from tabulate import tabulate
import numpy as np

def executar(arquivo):#motor de eventos da execucao de programas
    print('oi')

def rotina_end():
    print('Fim')

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
        executar(arquivo)


def lista_comandos(user):
    print('')
    print('')
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
