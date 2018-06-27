# -*- coding: utf-8 -*-

def montador_passo1(arquivo):
    area = 0
    file = open(arquivo, 'r')
    linha = file.readline() #le uma linha
    pseudo = False
    simbols_df = pd.DataFrame([])
    labels_df = pd.DataFrame([])

    if(linha[0] != ' ')
        if (linha.find(':')!=-1): #existe o simbolo : na linha, entao há rotulo
            #checar se ja ta na tabela de simbolos -> erro
            #incluir na tabela de simbolos
            df['simbolo'] = [linha[:":"]]
            df['valor'] = [linha[":":" "]]
            df['endereco'] = [ci]
            ci = ci + 2
        else:
            ci = ci + 2
            df['simbolo'] = [linha[:":"]]
            df['valor'] = [linha[":":" "]]
            df['endereco'] = [ci]
    else:
        tamanho = linha[].split(2)
        area = area + tamanho
        ci = ci + tamanho
    #fim do arquivo
    montador_passo2(arquivo, area)

def montador_passo2(arquivo, area):
    file = open(arquivo, 'r')
    file2 = open(arquivo_assembly, 'w')
    linha = file.readline() #le uma linha
    #consulta na tabela de instruções se é pseudo
    while (file.readline()):
        instr = linha[:2]
        #motor de eventos
        if (instr == 'JP'): #JP
            ci = ci + 4
            mem [i] = '00'
        elif (instr == 'JN'): #JN
            ci = ci + 4
            mem [i] = '02'
        elif (instr == '+'): #+
            ci = ci + 4
            mem [i] = '04'
        elif (instr == '0*'): #*
            ci = ci + 4
            mem [i] = '06'
        elif (instr == 'LD'): #LD
            ci = ci + 4
            mem [i] = '08'
        elif (instr == 'SC'): #SC
            ci = ci + 4
            mem [i] = '0A'
        elif (instr == 'HM'): #HM
            ci = ci + 4
            mem [i] = '0C'
        elif (instr == 'PD'): #PD
            ci = ci + 4
            mem [i] = '0F'
        elif (instr == 'JZ'): #JZ
            ci = ci + 4
            mem [i] = '01'
        elif (instr == 'LV'): #LV
            ci = ci + 4
            mem [i] = '03'
        elif (instr == '-'): # -
            ci = ci + 4
            mem [i] = '05'
        elif (instr == '/'): # /
            ci = ci + 4
            mem [i] = '07'
        elif (instr=='MM'): # mm
            ci = ci + 4
            mem [i] = '09'
        elif (instr == 'RS'): # RS
            ci = ci + 4
            mem [i] = '0D'
        elif (instr == 'GD'): #GD
            ci = ci + 4
            mem [i] = '0E'
        elif (instr == 'SO'): # SO
            ci = ci + 4
            mem [i] = '0B'
        elif (linha[:1] == 'K'):
            ci = ci + 2
        else:
            ci = ci + 2
    close(file)
    close(file2)
    return arquivo_assembly


def simulador_mvn(arquivo):
    #Inicialização de variáveis
    op = None
    parada = False
    while (not parada):
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
            ci = op + 2
        elif (instr == '0C'): #HM
            #PARAR, QUANDO FOR DADA A PARTIDA continua
            wait = raw_input('')
            ci = op
        elif (instr == '0F'): #PD
            #saida do conteudo do ac
            if (op == 0):
                ci = ac
            elif (op == 1):
                ci = ci + 2
            elif (op == 2):
                print ac
            elif (op == 3):
                print ac
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
        elif (instr == '0D'): # RS
            ci = op
        elif (instr == '0E'): #GD
            ac = raw_input('')
            ci = ci + 2
        elif (instr == '0B'): # SO
            #system call
            exit(1)
        else:
            print('Erro na leitura do arquivo')
