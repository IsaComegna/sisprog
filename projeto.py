# -*- coding: utf-8 -*-
import simulador_mvn

def executar(arquivo):#motor de eventos da execucao de programas
    print('oi')

def rotina_end():
    print('Fim')

#Interpretador de comandos
def interpretador(comando, arquivo):
    #motor de eventos de input de comandos
    if (comando == '$DIR'):
        #imprimir so os do id
        file_object = open('programas.txt', 'r+')
        print('Lista de programas disponiveis:')
        for line in file_object:
           print line
    if (comando == '$DEL'):
        print('\nDeletando programa')
        #apagar programa importar os e procurar


    if (comando == '$END'):
        print('Fim do programa')
        rotina_end()
    if (comando == '$RUN'):
        print('O programa sera executado')
        executar(arquivo)

def main():
    print('')
    print('')
    print('-------------------------------------------------------------')
    print('Sistema de desenvolvimento de programas em linguagem simbolica')
    print('-------------------------------------------------------------')
    print('')
    print(' ---Faca seu login---')
    file_object  = open('usuarios.txt', 'r+')
    print('Lista de usuarios ja cadastrados:')
    lines = file_object.readline()
    for line in file_object:
       print line
    print('')
    print('')
    print('Opcoes:')
    print('1 para novo usuario')
    print('2 para usuario em lista de usuarios')
    opcao = int(input() )
    # por id de usuario pra cada novo
    # arquivo: id_nomedoarquivo
    if (opcao==1):
        print('')
        new_user = raw_input('Escolha o nome de seu usuario: ')
        file_object.write(new_user)
        print('Login concluido com sucesso')
    else:
        print('')
        user = raw_input('Nome de usuário: ')
        file_object.write(user)
    file_object.close()
    print('')
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
    if (comando =='$DEL' or comando == '$RUN'):
        arquivo = raw_input('Digite o nome do arquivo: ')
        interpretador(comando, arquivo)
    interpretador(comando, '')

    #ter string com nome da pessoa append nome do arquivo : ja sei o nome do path

main()
