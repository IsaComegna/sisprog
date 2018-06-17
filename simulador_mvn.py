# -*- coding: utf-8 -*-

def montador_passo1(arquivo):
    area = 0
    file = open(arquivo, 'r')
    linha = file.readline() #le uma linha
    #checa se tem rotulo (procurar por :)
    if (rotulo):
        #checar se ja ta na tabela de simbolos -> erro
        #incluir na tabela de simbolos

    #consulta na tabela de instruções se é pseudo
    if (pseudo):
        tratamento_pseudo()
    else:
        determinar_binario()
        tamanho = determinar_tamanho()
        area = area + tamanho
        ci = ci + tamanho

    #fim do arquivo
    montador_passo2(arquivo, area)

def montador_passo2(arquivo, area):
    file = open(arquivo, 'r')
    linha = file.readline() #le uma linha
    #consulta na tabela de instruções se é pseudo
    if (pseudo):
        tratamento_pseudo()
    else:
        determinar_binario()
        #processa operandos !!!
        monta_e_gera_binario()
        tamanho = determinar_tamanho()
        ci = ci + tamanho
        reserva_area(area)









def carrega_loader():
    print('Carregando loader na memoria')


def carrega_programa():
    print('Carregando programa na memoria')
    return 0


def simulador_mvn(arquivo):

    #Inicialização de variáveis
    mem = ['0000']*4096  #a memória possui 3 bits com código hexadecimal
    ac = 0 #inicia em 0
    cont = 0 #contador para verificar se todos os eventos foram simulados
    simular = True #habilita simulação a começar
    reg_end_mem = 0 #registrador de endereçamento da memória
    reg_dados_mem = 0 #registrador de dados da memória
    acabou = False
    op = None

    ci = carrega_programa(arquivo)
    file = open(arquivo, 'r')
    linha = file.readline()
    instr = linha[:2]

    #motor de eventos
    if (instr == '00'): #JP
        ci = op
    elif (instr == '02'): #JN
        if (ac<0):
            ci = op
        else:
            ci = ci + 2
    elif (instr == '04'): #+
        ac = ac + mem[op]
        ci = ci + 2
    elif (instr == '06'): #*
        ac = ac * mem[op]
        ci = ci + 2
    elif (instr == '08'): #LD
        ac = mem[op]
        ci = ci + 2
    elif (instr == '0A'): #SC
        #???????
        ci = op + 2
    elif (instr == '0C'): #HM
        #PARAR, QUANDO FOR DADA A PARTIDA continua
        wait = raw_input('')
        ci = op
    elif (instr == '0E'): #PD
        #saida do conteudo do ac
        print('AC =')
        print(ac)
        ci = ci + 2
    elif (instr == '01'): #JZ
        if (ac == 0):
            ci = op
        else:
            ci = ci + 2
    elif (instr == '03'): #LV
        ac = op
        ci = ci + 2
    elif (instr == '05'): # -
        ac = ac - mem[op]
        ci = ci + 2
    elif (instr == '07'): # /
        ac = ac / mem[op]
        ci = ci + 2
    elif (instr=='09'): # mm
        mem[op] = ac
        ci = ci + 2
    elif (instr == '0B'): # RS
        ci = op
    elif (instr == '0D'): #GD
        ac = raw_input('')
        ci = ci + 2
    elif (instr == '0F'): # SO
        #system call
        ci = ci + 2
    else:
        print('Erro na leitura do arquivo')
