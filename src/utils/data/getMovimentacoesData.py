import pandas as pd
import numpy as np


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

    #Coluna TipoOperacao
    movimentacao['TipoOperacao'].replace(' ', 'OUTROS', inplace=True)

   #Coluna Tipo INstalação
    #movimentacao['TipoInstalacao'].replace('', 'PORTO ORGANIZADO')
    #movimentacao['TipoInstalacao'].replace(' ', 'PORTO ORGANIZADO')

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'SANTOS BRASIL - ')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'BRASIL TERMINAL ')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TECONDI - TUP')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'CAIS PÚBLICO - C')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'ADM - CPB')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TEAÇU 2 - CPB')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TEAÇU 3 - CPB')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TEAÇU 1 - CPB')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TERM. MARIT. GUA')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TERMINAL DE GRAO')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'MOINHO SANTISTA ')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "PORTO ORGANIZADO").fillna("PORTO ORGANIZADO")




    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'EMBRAPORT - TPF')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'USIMINAS - TPF')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'ULTRAFÉRTIL - TP')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'COREX - CPB')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TERM. DOW - TPO')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'CUTRALE - TPO')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'CARGILL - TUP')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")

    mask = (movimentacao['Ano'] == 2023) & (movimentacao['Terminal'] == 'TERM. DOW - TPO')
    movimentacao.loc[mask, 'TipoInstalacao'] = movimentacao.loc[mask, 'TipoInstalacao'].replace(" ", "FORA DO PORTO ORGANIZADO").fillna("FORA DO PORTO ORGANIZADO")





    # Cria Nova Coluna: Agrupamento por Terminal / Recinto Alfandegado
    movimentacao['TerminalAjustado'] = movimentacao['Terminal']
    movimentacao['TerminalAjustado'].replace('VOPAK (ILHA)', 'VOPAK', inplace=True)
    movimentacao['TerminalAjustado'].replace('VOPAK (ALAMOA)', 'VOPAK', inplace=True)

    movimentacao['TerminalAjustado'].replace('CITROSUCO (SER. PASSAGEM)','CITROSUCO', inplace=True)
    movimentacao['TerminalAjustado'].replace('CITROSUCO ARM XL','CITROSUCO', inplace=True)

    movimentacao['TerminalAjustado'].replace('CAIS PÚBLICO - C','CAIS PÚBLICO', inplace=True)
    
    movimentacao['TerminalAjustado'].replace('CUTRALE SABOO', 'CUTRALE', inplace=True)
    movimentacao['TerminalAjustado'].replace('CUTRALE - TPO', 'CUTRALE', inplace=True)

    movimentacao['TerminalAjustado'].replace('AGEO LESTE', 'AGEO', inplace=True)
    movimentacao['TerminalAjustado'].replace('AGEO NORTE - COPAPE','AGEO', inplace=True)

    movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ALAMOA)', 'GRANEL QUIMICA', inplace=True)
    movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ILHA)', 'GRANEL QUIMICA', inplace=True)

    movimentacao['TerminalAjustado'].replace('LIBRA 33', 'LIBRA', inplace=True)
    movimentacao['TerminalAjustado'].replace('LIBRA 35', 'LIBRA', inplace=True)
    movimentacao['TerminalAjustado'].replace('LIBRA 37', 'LIBRA', inplace=True)

    movimentacao['TerminalAjustado'].replace('RODRIMAR - ARM VIII', 'RODRIMAR', inplace=True)

    movimentacao['TerminalAjustado'].replace('BRASIL TERMINAL ', 'BTP', inplace=True)

    movimentacao['TerminalAjustado'].replace('BRACELL (ARM 15)', 'BRACELL', inplace=True)

    movimentacao['TerminalAjustado'].replace('BUNGE (PACIFICO) - PAQUETÁ', 'BUNGE', inplace=True)
    movimentacao['TerminalAjustado'].replace('BUNGE (SANTISTA) - MACUCO', 'BUNGE', inplace=True)

    movimentacao['TerminalAjustado'].replace('SUZANO (VCP - ARM 13/14/15)', 'SUZANO (ARM 32)', inplace=True)
    
    movimentacao['TerminalAjustado'].replace('SANTOS BRASIL - ', 'SANTOS BRASIL', inplace=True)
    movimentacao['TerminalAjustado'].replace('SANTOS BRASIL (SSZ35.2 Saboó)', 'SANTOS BRASIL', inplace=True)

    movimentacao['TerminalAjustado'].replace('USIMINAS - TPF', 'USIMINAS', inplace=True)
    movimentacao['TerminalAjustado'].replace('TERM. MARIT. GUA', 'TERMAG', inplace=True)
    movimentacao['TerminalAjustado'].replace('TERMINAL DE GRAO', 'TGG', inplace=True)

    movimentacao['TerminalAjustado'].replace('MOINHO SANTISTA ', 'MOINHO SANTISTA', inplace=True)
    movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].replace('TERM. DOW - TPO', 'DOW')
    
    movimentacao['TerminalAjustado'].replace('TEAÇU 3 - CPB', 'CPB', inplace=True)
    movimentacao['TerminalAjustado'].replace('TEAÇU 2 - CPB', 'CPB', inplace=True)
    movimentacao['TerminalAjustado'].replace('TEAÇU 1 - CPB', 'CPB', inplace=True)

    movimentacao.loc[movimentacao['Berco'] == 'ARM 19', 'TerminalAjustado'] = movimentacao.loc[movimentacao['Berco'] == 'ARM 19', 'TerminalAjustado'].fillna('OUTROS')
    movimentacao.loc[movimentacao['Berco'] == 'TIPLAM', 'TerminalAjustado'] = movimentacao.loc[movimentacao['Berco'] == 'TIPLAM I', 'TerminalAjustado'].fillna('TIPLAM')
    movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].replace('', np.nan).fillna('OUTROS')

    #Padronização Berços
    movimentacao['Berco'].replace('ALAMOA IV', 'ALAMOA 4', inplace=True)
    movimentacao['Berco'].replace('ALAMOA III', 'ALAMOA 3', inplace=True)
    movimentacao['Berco'].replace('ALAMOA II', 'ALAMOA 2', inplace=True)
    movimentacao['Berco'].replace('ALAMOA I', 'ALAMOA 1', inplace=True)

    movimentacao['Berco'].replace('SABOO IV', 'SABOO 4', inplace=True)
    movimentacao['Berco'].replace('SABOO III', 'SABOO 3', inplace=True)
    movimentacao['Berco'].replace('SABOO II', 'SABOO 2', inplace=True)
    movimentacao['Berco'].replace('SABOO I', 'SABOO 1', inplace=True)

    movimentacao['Berco'].replace('TECON III', 'TECON 3', inplace=True)
    movimentacao['Berco'].replace('TECON II', 'TECON 2', inplace=True)
    movimentacao['Berco'].replace('TECON I', 'TECON 1', inplace=True)

    movimentacao['Berco'].replace('TEV II', 'TEV 2', inplace=True)
    movimentacao['Berco'].replace('TEV I', 'TEV', inplace=True)

    movimentacao['Berco'].replace('BTP III', 'BTP 3', inplace=True)
    movimentacao['Berco'].replace('BTP II', 'BTP 2', inplace=True)
    movimentacao['Berco'].replace('BTP I', 'BTP 1', inplace=True)

    movimentacao['Berco'].replace('USIMINAS IV', 'USIMINAS 4', inplace=True)
    movimentacao['Berco'].replace('USIMINAS III', 'USIMINAS 3', inplace=True)

    movimentacao['Berco'].replace('ARMAZEM ', 'ARM ', inplace=True)
    
    movimentacao['Berco'].replace('TERM. DOW', 'DOW', inplace=True)
    
    movimentacao['Berco'].replace('ARMAZEM 35.1', 'ARM 35.1', inplace=True)
    



 

    return movimentacao