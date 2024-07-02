import pandas as pd
import numpy as np

import locale



#Carrega dados
def carregaMovimentacao():
    movimentacao = pd.DataFrame(pd.read_csv('./Data/raw/combined_file.csv', encoding='utf8', sep=","))
    movimentacao = ajustaMovimmentacao(movimentacao)
    return movimentacao



def ajustaTexto(df, coluna, txtAnterior, txtAtualizado):
        df[coluna] = df[coluna].apply(lambda x: txtAtualizado if x == txtAnterior else x)    



def ajustaMovimmentacao(movimentacao):
    movimentacao["Toneladas"] = movimentacao["Toneladas"].round(2)

    

    movimentacao['Data'] = pd.to_datetime(movimentacao['Ano'].astype(str) + 
                                            movimentacao['Mes'].astype(str), format='%Y%m')
    movimentacao['Data'] = movimentacao['Data'].dt.date



    #Coluna Carga
    #movimentacao['Carga'].replace('PRODUTOS DA INDÚSTRIA QUÍMICA', 'PRODUTOS QUÍMICOS', inplace=True)
    ajustaTexto(movimentacao, 'Carga','PRODUTOS DA INDÚSTRIA QUÍMICA', 'PRODUTOS QUÍMICOS')

    

    #Coluna Terminal
    #movimentacao['Terminal'].replace('  ', ' ', inplace=True)
    ajustaTexto(movimentacao, 'Terminal', '  ', ' ')


    #Coluna TipoOperacao
    #movimentacao['TipoOperacao'].replace(' ', 'OUTROS', inplace=True)
    ajustaTexto(movimentacao, 'TipoOperacao', ' ', 'OUTROS')


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

    
    #movimentacao['TerminalAjustado'].replace('DEICMAR', 'BANDEIRANTES-DEICMAR', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'BANDEIRANTES-DEICMAR' if x == 'DEICMAR' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'DEICMAR', 'BANDEIRANTES-DEICMAR')

    #movimentacao['TerminalAjustado'].replace('VOPAK (ILHA)', 'VOPAK', inplace=True)
    #movimentacao['TerminalAjustado'].replace('VOPAK (ALAMOA)', 'VOPAK', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'VOPAK' if x == 'VOPAK (ILHA)' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'VOPAK' if x == 'VOPAK (ALAMOA)' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'VOPAK (ILHA)', 'VOPAK')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'VOPAK (ALAMOA)', 'VOPAK')

    #movimentacao['TerminalAjustado'].replace('CITROSUCO (SER. PASSAGEM)','CITROSUCO', inplace=True)
    #movimentacao['TerminalAjustado'].replace('CITROSUCO ARM XL','CITROSUCO', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CITROSUCO' if x == 'CITROSUCO (SER. PASSAGEM)' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CITROSUCO' if x == 'CITROSUCO ARM XL' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'CITROSUCO (SER. PASSAGEM)','CITROSUCO')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'CITROSUCO ARM XL','CITROSUCO')

    #movimentacao['TerminalAjustado'].replace('CAIS PÚBLICO - C','CAIS PÚBLICO', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CAIS PÚBLICO' if x == 'CAIS PÚBLICO - C' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'CAIS PÚBLICO - C','CAIS PÚBLICO')
    
    #movimentacao['TerminalAjustado'].replace('CUTRALE SABOO', 'CUTRALE', inplace=True)
    #movimentacao['TerminalAjustado'].replace('CUTRALE - TPO', 'CUTRALE', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CUTRALE' if x == 'CUTRALE SABOO' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CUTRALE' if x == 'CUTRALE - TPO' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado','CUTRALE SABOO', 'CUTRALE')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'CUTRALE - TPO', 'CUTRALE')

    #movimentacao['TerminalAjustado'].replace('AGEO LESTE', 'AGEO', inplace=True)
    #movimentacao['TerminalAjustado'].replace('AGEO NORTE - COPAPE','AGEO', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'AGEO' if x == 'AGEO LESTE' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'AGEO' if x == 'AGEO NORTE - COPAPE' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'AGEO LESTE', 'AGEO')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'AGEO NORTE - COPAPE', 'AGEO')

    #movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ALAMOA)', 'GRANEL QUIMICA', inplace=True)
    #movimentacao['TerminalAjustado'].replace('GRANEL QUIMICA (ILHA)', 'GRANEL QUIMICA', inplace=True)
    #acao['TerminalAjustado'].apply(lambda x: 'GRANEL QUIMICA' if x == 'GRANEL QUIMICA (ALAMOA)' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'GRANEL QUIMICA' if x == 'GRANEL QUIMICA (ILHA)' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'GRANEL QUIMICA (ALAMOA)', 'GRANEL QUIMICA')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'GRANEL QUIMICA (ILHA)', 'GRANEL QUIMICA')

    #movimentacao['TerminalAjustado'].replace('LIBRA 33', 'LIBRA', inplace=True)
    #movimentacao['TerminalAjustado'].replace('LIBRA 35', 'LIBRA', inplace=True)
    #movimentacao['TerminalAjustado'].replace('LIBRA 37', 'LIBRA', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'LIBRA' if x == 'LIBRA 33' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'LIBRA' if x == 'LIBRA 35' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'LIBRA' if x == 'LIBRA 37' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'LIBRA 33', 'LIBRA')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'LIBRA 35', 'LIBRA')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'LIBRA 37', 'LIBRA')


    #movimentacao['TerminalAjustado'].replace('RODRIMAR - ARM VIII', 'RODRIMAR', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'RODRIMAR' if x == 'RODRIMAR - ARM VIII' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'RODRIMAR - ARM VIII', 'RODRIMAR')

    #movimentacao['TerminalAjustado'].replace('BRASIL TERMINAL ', 'BTP', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'BTP' if x == 'BRASIL TERMINAL ' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'BRASIL TERMINAL ', 'BTP')

    #movimentacao['TerminalAjustado'].replace('BRACELL (ARM 15)', 'BRACELL', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'BRACELL' if x == 'BRACELL (ARM 15)' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'BRACELL (ARM 15)', 'BRACELL')

    #movimentacao['TerminalAjustado'].replace('BUNGE (PACIFICO) - PAQUETÁ', 'BUNGE', inplace=True)
    #movimentacao['TerminalAjustado'].replace('BUNGE (SANTISTA) - MACUCO', 'BUNGE', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'BUNGE' if x == 'BUNGE (PACIFICO) - PAQUETÁ' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'BUNGE' if x == 'BUNGE (SANTISTA) - MACUCO' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'BUNGE (PACIFICO) - PAQUETÁ', 'BUNGE')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'BUNGE (SANTISTA) - MACUCO', 'BUNGE')


    #movimentacao['TerminalAjustado'].replace('SUZANO (VCP - ARM 13/14/15)', 'SUZANO (ARM 32)', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'SUZANO (ARM 32)' if x == 'SUZANO (VCP - ARM 13/14/15)' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'SUZANO (VCP - ARM 13/14/15)', 'SUZANO (ARM 32)')
    
    #movimentacao['TerminalAjustado'].replace('SUZANO (VCP - ARM 13/14/15)', 'SUZANO (ARM 32)', inplace=True)
    #movimentacao['TerminalAjustado'].replace('SANTOS BRASIL (SSZ35.2 Saboó)', 'SANTOS BRASIL', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'SANTOS BRASIL' if x == 'SANTOS BRASIL - ' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'SANTOS BRASIL' if x == 'SANTOS BRASIL (SSZ35.2 Saboó)' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'SUZANO (VCP - ARM 13/14/15)', 'SUZANO (ARM 32)')
    ajustaTexto(movimentacao, 'TerminalAjustado','SANTOS BRASIL (SSZ35.2 Saboó)', 'SANTOS BRASIL')


    #movimentacao['TerminalAjustado'].replace('USIMINAS - TPF', 'USIMINAS', inplace=True)
    #movimentacao['TerminalAjustado'].replace('TERM. MARIT. GUA', 'TERMAG', inplace=True)
    #movimentacao['TerminalAjustado'].replace('TERMINAL DE GRAO', 'TGG', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'USIMINAS' if x == 'USIMINAS - TPF' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'TERMAG' if x == 'TERM. MARIT. GUA' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'TGG' if x == 'TERMINAL DE GRAO' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'USIMINAS - TPF', 'USIMINAS')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'TERM. MARIT. GUA', 'TERMAG')
    ajustaTexto(movimentacao, 'TerminalAjustado','TERMINAL DE GRAO', 'TGG')

    #movimentacao['TerminalAjustado'].replace('MOINHO SANTISTA ', 'MOINHO SANTISTA', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].replace('TERM. DOW - TPO', 'DOW')
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'MOINHO SANTISTA' if x == 'MOINHO SANTISTA ' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'DOW' if x == 'TERM. DOW - TPO' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado','MOINHO SANTISTA ', 'MOINHO SANTISTA')
    ajustaTexto(movimentacao, 'TerminalAjustado','TERM. DOW - TPO', 'DOW')

    #movimentacao['TerminalAjustado'].replace('TEAÇU 3 - CPB', 'CPB', inplace=True)
    #movimentacao['TerminalAjustado'].replace('TEAÇU 2 - CPB', 'CPB', inplace=True)
    #movimentacao['TerminalAjustado'].replace('TEAÇU 1 - CPB', 'CPB', inplace=True)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CPB' if x == 'TEAÇU 3 - CPB' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CPB' if x == 'TEAÇU 2 - CPB' else x)
    #movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].apply(lambda x: 'CPB' if x == 'TEAÇU 1 - CPB' else x)
    ajustaTexto(movimentacao, 'TerminalAjustado', 'TEAÇU 3 - CPB', 'CPB')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'TEAÇU 2 - CPB', 'CPB')
    ajustaTexto(movimentacao, 'TerminalAjustado', 'TEAÇU 1 - CPB', 'CPB')

    #movimentacao.loc[movimentacao['Berco'] == 'ARM 19', 'TerminalAjustado'] = movimentacao.loc[movimentacao['Berco'] == 'ARM 19', 'TerminalAjustado'].fillna('OUTROS')
    #movimentacao.loc[movimentacao['Berco'] == 'TIPLAM', 'TerminalAjustado'] = movimentacao.loc[movimentacao['Berco'] == 'TIPLAM I', 'TerminalAjustado'].fillna('TIPLAM')
    movimentacao['TerminalAjustado'] = movimentacao.apply(
                                            lambda row: 'OUTROS' if row['Berco'] == 'ARM 19' and pd.isnull(row['TerminalAjustado']) else row['TerminalAjustado'], axis=1
                                                        )
    movimentacao['TerminalAjustado'] = movimentacao.apply(
                                            lambda row: 'TIPLAM' if row['Berco'] == 'TIPLAM I' and pd.isnull(row['TerminalAjustado']) else row['TerminalAjustado'], axis=1
                                                        )

    movimentacao['TerminalAjustado'] = movimentacao['TerminalAjustado'].replace('', np.nan).fillna('OUTROS')

    #Padronização Berços
    #movimentacao['Berco'].replace('ALAMOA IV', 'ALAMOA 4', inplace=True)
    #movimentacao['Berco'].replace('ALAMOA III', 'ALAMOA 3', inplace=True)
    #movimentacao['Berco'].replace('ALAMOA II', 'ALAMOA 2', inplace=True)
    #movimentacao['Berco'].replace('ALAMOA I', 'ALAMOA 1', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'ALAMOA 4' if x == 'ALAMOA IV' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'ALAMOA 3' if x == 'ALAMOA III' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'ALAMOA 2' if x == 'ALAMOA II' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'ALAMOA 1' if x == 'ALAMOA I' else x)
    ajustaTexto(movimentacao, 'Berco', 'ALAMOA IV', 'ALAMOA 4')
    ajustaTexto(movimentacao, 'Berco', 'ALAMOA III', 'ALAMOA 3')
    ajustaTexto(movimentacao, 'Berco', 'ALAMOA II', 'ALAMOA 2')
    ajustaTexto(movimentacao, 'Berco', 'ALAMOA I', 'ALAMOA 1')

    #movimentacao['Berco'].replace('SABOO IV', 'SABOO 4', inplace=True)
    #movimentacao['Berco'].replace('SABOO III', 'SABOO 3', inplace=True)
    #movimentacao['Berco'].replace('SABOO II', 'SABOO 2', inplace=True)
    #movimentacao['Berco'].replace('SABOO I', 'SABOO 1', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'SABOO 4' if x == 'SABOO IV' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'SABOO 3' if x == 'SABOO III' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'SABOO 2' if x == 'SABOO II' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'SABOO 1' if x == 'SABOO I' else x)
    ajustaTexto(movimentacao, 'Berco', 'SABOO IV', 'SABOO 4')
    ajustaTexto(movimentacao, 'Berco', 'SABOO III', 'SABOO 3')
    ajustaTexto(movimentacao, 'Berco', 'SABOO II', 'SABOO 2')
    ajustaTexto(movimentacao, 'Berco', 'SABOO I', 'SABOO 1')

    #movimentacao['Berco'].replace('TECON III', 'TECON 3', inplace=True)
    #movimentacao['Berco'].replace('TECON II', 'TECON 2', inplace=True)
    #movimentacao['Berco'].replace('TECON I', 'TECON 1', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'TECON 3' if x == 'TECON III' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'TECON 2' if x == 'TECON II' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'TECON 1' if x == 'TECON I' else x)
    ajustaTexto(movimentacao, 'Berco', 'TECON III', 'TECON 3')
    ajustaTexto(movimentacao, 'Berco', 'TECON II', 'TECON 2')
    ajustaTexto(movimentacao, 'Berco', 'TECON I', 'TECON 1')


    #movimentacao['Berco'].replace('TEV II', 'TEV 2', inplace=True)
    #movimentacao['Berco'].replace('TEV I', 'TEV', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'TEV 2' if x == 'TEV II' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'TEV' if x == 'TEV I' else x)
    ajustaTexto(movimentacao, 'Berco', 'TEV II', 'TEV 2')
    ajustaTexto(movimentacao, 'Berco', 'TEV I', 'TEV')

    #movimentacao['Berco'].replace('BTP III', 'BTP 3', inplace=True)
    #movimentacao['Berco'].replace('BTP II', 'BTP 2', inplace=True)
    #movimentacao['Berco'].replace('BTP I', 'BTP 1', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'BTP 3' if x == 'BTP III' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'BTP 2' if x == 'BTP II' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: 'BTP 1' if x == 'BTP I' else x)
    ajustaTexto(movimentacao, 'Berco', 'BTP III', 'BTP 3')
    ajustaTexto(movimentacao, 'Berco', 'BTP II', 'BTP 2')
    ajustaTexto(movimentacao, 'Berco', 'BTP I', 'BTP 1')

    #movimentacao['Berco'].replace('USIMINAS IV', 'USIMINAS 4', inplace=True)
    #movimentacao['Berco'].replace('USIMINAS III', 'USIMINAS 3', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: '' if x == '' else x)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: '' if x == '' else x)
    ajustaTexto(movimentacao, 'Berco', 'USIMINAS IV', 'USIMINAS 4')
    ajustaTexto(movimentacao, 'Berco', 'USIMINAS III', 'USIMINAS 3')

    #movimentacao['Berco'].replace('ARMAZEM ', 'ARM ', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: '' if x == '' else x)
    ajustaTexto(movimentacao, 'Berco', 'ARMAZEM ', 'ARM ')
    
    #movimentacao['Berco'].replace('TERM. DOW', 'DOW', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: '' if x == '' else x)
    ajustaTexto(movimentacao, 'Berco', 'TERM. DOW', 'DOW')
    
    #movimentacao['Berco'].replace('ARMAZEM 35.1', 'ARM 35.1', inplace=True)
    #movimentacao['Berco'] = movimentacao['Berco'].apply(lambda x: '' if x == '' else x)
    ajustaTexto(movimentacao, 'Berco', 'ARMAZEM 35.1', 'ARM 35.1')
    



 

    return movimentacao