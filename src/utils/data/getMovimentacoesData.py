import pandas as pd


#Carrega dados
def carregaMovimentacao():
    movimentacao = pd.DataFrame(pd.read_csv('./Data/raw/combined_file.csv', encoding='utf8', sep=","))



    movimentacao['Data'] = pd.to_datetime(movimentacao['Ano'].astype(str) + 
                                            movimentacao['Mes'].astype(str), format='%Y%m')
    movimentacao['Data'] = movimentacao['Data'].dt.date



    #Coluna Carga
    movimentacao['Carga'].replace('PRODUTOS DA INDÚSTRIA QUÍMICA', 'PRODUTOS QUÍMICOS', inplace=True)

    #Coluna Terminal
    movimentacao['Terminal'].replace('  ', ' ', inplace=True)

    #Coluna Tipo INstalação
    movimentacao['TipoInstalacao'].replace('', 'PORTO ORGANIZADO', inplace=True)
    movimentacao['TipoInstalacao'].replace(' ', 'PORTO ORGANIZADO', inplace=True)


    # Cria Nova Coluna: Agrupamento por Terminal / Recinto Alfandegado
    movimentacao['TerminalAjustado'] = movimentacao['Terminal']
    movimentacao['TerminalAjustado'].replace('VOPAK (ILHA)', 'VOPAK', inplace=True)
    movimentacao['TerminalAjustado'].replace('VOPAK (ALAMOA)', 'VOPAK', inplace=True)

    movimentacao['TerminalAjustado'].replace('CITROSUCO (SER. PASSAGEM)','CITROSUCO', inplace=True)
    movimentacao['TerminalAjustado'].replace('CUTRALE SABOO', 'CUTRALE', inplace=True)
    movimentacao['TerminalAjustado'].replace('CUTRALE - TPO', 'CUTRALE',inplace=True)

    movimentacao['TerminalAjustado'].replace('AGEO LESTE', 'AGEO', inplace=True)
    movimentacao['TerminalAjustado'].replace('AGEO NORTE - COPAPE','AGEO',  inplace=True)

    movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ALAMOA)', 'GRANEL QUIMICA',inplace=True)
    movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ILHA)', 'GRANEL QUIMICA',  inplace=True)

    movimentacao['TerminalAjustado'].replace('LIBRA 33', 'LIBRA',  inplace=True)
    movimentacao['TerminalAjustado'].replace('LIBRA 35', 'LIBRA',  inplace=True)
    movimentacao['TerminalAjustado'].replace('LIBRA 37', 'LIBRA',  inplace=True)

    movimentacao['TerminalAjustado'].replace('RODRIMAR - ARM VIII', 'RODRIMAR',  inplace=True)

    movimentacao['TerminalAjustado'].replace('SANTOS BRASIL - ', 'SANTOS BRASIL', inplace=True)
    movimentacao['TerminalAjustado'].replace('SANTOS BRASIL (SSZ35.2 Saboó)', 'SANTOS BRASIL', inplace=True)

    movimentacao['TerminalAjustado'].replace('USIMINAS - TPF', 'USIMINAS',  inplace=True)

    #Padronização Berços
    movimentacao['Berco'].replace('ALAMOA IV', 'ALAMOA 4',  inplace=True)
    movimentacao['Berco'].replace('ALAMOA III', 'ALAMOA 3',  inplace=True)
    movimentacao['Berco'].replace('ALAMOA II', 'ALAMOA 2',  inplace=True)
    movimentacao['Berco'].replace('ALAMOA I', 'ALAMOA 1',  inplace=True)

    movimentacao['Berco'].replace('SABOO IV', 'SABOO 4',  inplace=True)
    movimentacao['Berco'].replace('SABOO III', 'SABOO 3',  inplace=True)
    movimentacao['Berco'].replace('SABOO II', 'SABOO 2',  inplace=True)
    movimentacao['Berco'].replace('SABOO I', 'SABOO 1',  inplace=True)

    movimentacao['Berco'].replace('TECON III', 'TECON 3',  inplace=True)
    movimentacao['Berco'].replace('TECON II', 'TECON 2',  inplace=True)
    movimentacao['Berco'].replace('TECON I', 'TECON 1',  inplace=True)

    movimentacao['Berco'].replace('TEV II', 'TEV 2',  inplace=True)
    movimentacao['Berco'].replace('TEV I', 'TEV',  inplace=True)

    movimentacao['Berco'].replace('BTP III', 'BTP 3',  inplace=True)
    movimentacao['Berco'].replace('BTP II', 'BTP 2',  inplace=True)
    movimentacao['Berco'].replace('BTP I', 'BTP 1',  inplace=True)

    movimentacao['Berco'].replace('USIMINAS IV', 'USIMINAS 4',  inplace=True)
    movimentacao['Berco'].replace('USIMINAS III', 'USIMINAS 3',  inplace=True)

    movimentacao['Berco'].replace('ARMAZEM ', 'ARM ',  inplace=True)



    return movimentacao