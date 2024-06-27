import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import time
import locale





locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Sources do projeto
from src.utils.data import getMovimentacoesData as movimenta
from src.utils.data import getTerminaisData as terminais
from src.utils.data import getBercosData as bercos
from src.utils.data import getPanoramaData as carregaDadosTerminaisPanorama

st.set_page_config(
    page_title="Port of Santos Container  Visualization",
    page_icon="🏂",
    layout="wide"
    )

import menu as menu
menu.menu()
    
#Movimentação
movimentacao = movimenta.carregaMovimentacao()



terminaisSantos = terminais.carregaTerminais()

movimentacaoGeo = pd.merge(movimentacao, terminaisSantos,on='Terminal', how='left' )
#def colunasMovimentaGeo():
    #   Colunas
    #   Ano
    #   Mes
    #   Berco
    #   TipoInstalacao
    #   Terminal           
    #   PerfilCarga  
    #   TipoOperacao    
    #   Navegacao      
    #   SentidoCarga  ...    
    #   Unidades        
    #   Data
    #   TerminalAjustado   
    #   Latitude  
    #   Longitude    
    #   Local         
    #   Tipo  
    #   Tamanho 
    #   TerminalUni
   #print(movimentacaoGeo)


deParaBercos = bercos.carregaDeParaBercosMovimentacaoPDZ()
#st.dataframe(deParaBercos)

#Identificação dos berços
dfPoligono, dfBercosPDZ = bercos.carregaBercosPDZDataFrame()


deParaBercosDadosPDZ = pd.merge(deParaBercos, dfBercosPDZ,left_on="BercoPDZ", right_on="Berco", how='outer' )

deParaBercosDadosPDZ = deParaBercosDadosPDZ.dropna(subset=['BercoMovimentacao'])
deParaBercosDadosPDZ = deParaBercosDadosPDZ.drop(columns=deParaBercosDadosPDZ.columns[[4, 
                                                                                       deParaBercosDadosPDZ.columns.get_loc('Berco'),
                                                                                       deParaBercosDadosPDZ.columns.get_loc('Descricao')
                                                                                       ]])


movimentacaoBercos = pd.merge(movimentacaoGeo, deParaBercosDadosPDZ,left_on="Berco", right_on="BercoMovimentacao", how='left')

movimentacaoBercos = movimentacaoBercos.drop(columns=movimentacaoBercos.columns[[
                                                                                movimentacaoBercos.columns.get_loc('TerminalUni'),
                                                                                movimentacaoBercos.columns.get_loc('BercoMovimentacao'),
                                                                                movimentacaoBercos.columns.get_loc('BercoPDZ'),
                                                                                movimentacaoBercos.columns.get_loc('Carga_y'),
                                                                                movimentacaoBercos.columns.get_loc('Cais')
                                                                                ]])


tab1, tab2 = st.tabs(["EDA", "Dados"])
with tab1:

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        #st.header("Perfl da Carga")
        #perfilCarga_list = list(movimentacao["PerfilCarga"].unique())[::-1]
        #selected_perfilCarga = st.multiselect('Selecione o Tipo da Carga', perfilCarga_list,default="CARGA CONTEINERIZADA") 
        pass
    with col2:
        st.header("Periodicidade")
        periodicidade = st.radio('Selecione a Periodicidade', ["mesAno","Ano"])
        
    with col3:
        st.header("Agrupamento")
        selected_group = st.selectbox('Selecione o Tipo de Agrupamento', 
                                    [
                                        #"Terminal","Carga","TipoInstalacao","PerfilCarga","TipoOperacao","GrupoBerco"
                                        'Berco', 'TipoInstalacao', 'PerfilCarga', 'TipoOperacao', 'Navegacao', 'SentidoCarga', 'Carga', 
                                        'Terminal', 'Local', 'Tipo',  "Região Berco"
                                     ])
        
        
        if selected_group == "Terminal": 
                selected_group = "TerminalAjustado" 
                
        elif selected_group == "Carga":
                selected_group = "Carga_x"
                
        elif selected_group == "Região Berco":
                selected_group = "GrupoBerco"
        else:
            selected_group = selected_group

            
    with col4:
        st.header("Selecionar Maiores")
        ligarmaiores = st.toggle("Selecionar apenas os maiores")
        qtd = st.slider("Quantidade de TOPs", 3, 10, 1)
    


    movimentacaoBercos['DataN'] = pd.to_datetime(movimentacaoBercos['Data'], format='%d%b%Y.%f')

    movimentacaoBercos["mesAno"] = pd.to_datetime(movimentacaoBercos['Data'], format='%b/%Y.%f')


    #movimentoQ = movimentacaoGeo[((movimentacaoGeo["PerfilCarga"].isin(selected_perfilCarga)) & 
    #                            (movimentacaoGeo["TipoInstalacao"].isin(selected_tipoInst)))].groupby(
    #                                                                                        [selected_group,'mesAno',"Latitude","Longitude"]
    #                                                                                        ).agg({'Toneladas':"sum"}).sort_values(by=["mesAno",selected_group], ascending=True).reset_index()



    movimentoQ = movimentacaoBercos.groupby(
                                        [periodicidade,selected_group]
                                        ).agg({'Toneladas':"sum"}).sort_values(by=[periodicidade,selected_group], ascending=True).reset_index()
    
    dsReserva = movimentacaoBercos.copy()
    #st.dataframe(movimentoQ)
    if ligarmaiores:
         
        def top_n_tipos_carga_por_ano(df, n, selected_group, periodicidade):
            # Inicializa um DataFrame vazio para armazenar os resultados
            resultados = pd.DataFrame(columns=[periodicidade, selected_group, 'Toneladas'])

            # Itera sobre cada ano único no DataFrame
            for ano in df[periodicidade].unique():
                
                # Filtra os dados para o ano específico
                df_ano = df[df[periodicidade] == ano]
                
                # Agrupa por TipoCarga e soma as Toneladas
                cargas_grouped = df_ano.groupby(selected_group)['Toneladas'].sum().reset_index()
                
                # Seleciona os top N tipos de carga para o ano atual
                top_cargas_ano = cargas_grouped.nlargest(n, 'Toneladas')
                
                top_cargas_ano[periodicidade] = ano

                # Adiciona os resultados ao DataFrame final
                resultados = pd.concat([resultados, top_cargas_ano])
                
            return resultados

        # Obter os top N tipos de carga para cada ano
        movimentoQ = top_n_tipos_carga_por_ano(movimentoQ, qtd, selected_group,periodicidade)
        #st.dataframe(movimentoQ)


    


    if periodicidade == "Ano":
            


            #movimentoQ['Percentual'] = movimentoQ['Toneladas'].pct_change() * 100
            movimentoQ['Toneladas_M'] = (movimentoQ['Toneladas'] / 1000000).round(2)

            fig = px.bar(movimentoQ, x=periodicidade, y="Toneladas_M", color=selected_group, #text=(movimentoQ['Toneladas']/1000000).round(2),
                         labels={'Toneladas':'Toneladas em Milhões'})
            
            fig.update_traces(
                #texttemplate='%{y:.2f} M',
                #texttemplate='%{y} M \n(%{customdata:.2f} %)',
                texttemplate='%{y} M',
                textposition='auto',
                #customdata=movimentoQ['Toneladas_M'].fillna(0).tolist()  # Usando fillna para tratar o primeiro valor sem percentual
            )
            
            fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(count=3, label="3y", step="year", stepmode="backward"),
                    dict(count=5, label="5y", step="year", stepmode="backward"),
                    dict(count=10, label="10y", step="year", stepmode="backward"),
                    dict(step="all")
                    ])
                )   
            )
            

            
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            evento = st.plotly_chart(fig, key="iris", on_select="rerun")
            #evento.selection

            def process_selection(selection, campo):
                # Verifica se há pelo menos dois itens no mesmo legendGroup
                groups = {}
                
                for item in selection['points']:
                    #legend_group = item.get('customdata', {}).get('legendgroup', None)
                    legend_group = item.get('legendgroup', None)
                    if legend_group:
                        if legend_group not in groups:
                            groups[legend_group] = []
                        groups[legend_group].append(item)

                # Se nenhum grupo tem mais de um item
                for group, items in groups.items():
                    if len(items) < 2:
                        st.error(f"É necessário pelo menos mais um item no grupo '{group}'.")
                        return

                # Seleciona o item com menor e maior valor de x
                min_x_item = None
                max_x_item = None
                for group, items in groups.items():
                    items_sorted_by_x = sorted(items, key=lambda item: item[campo])
                    if min_x_item is None or items_sorted_by_x[0][campo] < min_x_item[campo]:
                        min_x_item = items_sorted_by_x[0]
                    if max_x_item is None or items_sorted_by_x[-1][campo] > max_x_item[campo]:
                        max_x_item = items_sorted_by_x[-1]

                return min_x_item, max_x_item, legend_group
              



            # Verifica e processa a seleção
            if 'selection' in evento:
                if len(evento.selection['points'])<2:
                    pass
                else:
                    min_x_item, max_x_item, legend_group = process_selection(evento.selection,"label")
                    print(min_x_item)
                    print(max_x_item)
                    if min_x_item and max_x_item:
                        # Criando o novo container com duas colunas
                        col1, col2 = st.columns([2, 1])

                        # Gráfico de linhas entre o menor e maior valor de x
                        
                        filtered_df = dsReserva[
                                                (dsReserva[periodicidade] >= min_x_item['label']) & 
                                                (dsReserva[periodicidade] <= max_x_item['label']) &
                                                (dsReserva[selected_group] == legend_group)
                                                ].groupby(
                                                            ["mesAno","Ano"]
                                                            ).agg({'Toneladas':"sum"}).sort_values(by=["mesAno"], ascending=True).reset_index()
                        
                        filtered_df['Toneladas_M'] = (filtered_df['Toneladas'] / 1000000).round(2)
                        print(filtered_df)
                        fig_lines = px.line(filtered_df, x="mesAno", y='Toneladas_M',text="Toneladas_M", width=1000,height=400 )
                        fig_lines.update_traces(textposition="top center", 
                                            
                                                marker=dict(line=dict(color='gray', width=1)))
                        col1.plotly_chart(fig_lines, use_container_width=True)

                        # Gráfico indicador com volume de toneladas e índice de crescimento/retração
                        import plotly.graph_objects as go
                        fig_indicator = go.Figure()

                        

                        toneladasMax = filtered_df.loc[filtered_df['Ano'] == max_x_item["label"], 'Toneladas_M'].sum()
                        toneladasMin = filtered_df.loc[filtered_df['Ano'] == min_x_item["label"], 'Toneladas_M'].sum()                                  

                        #crescimento =  (1-(toneladasMax/toneladasMin))*100
                        crescimento = ((toneladasMax - toneladasMin) / toneladasMin     )*100
                        st.write(crescimento)
                        # Criando o componente de indicador com Graph Objects
                        fig_indicator = go.Figure(go.Indicator(
                            mode='number+delta',
                            value=toneladasMax,
                            delta={'reference': toneladasMin, 'relative': True},
                            title='Crescimento em  Tons',
                            domain={'row': 0, 'column': 1},
                            number={'suffix': 'M'}
                        ))

                        # Configurando layout do indicador
                        fig_indicator.update_layout(
                            grid={'rows': 1, 'columns': 2, 'pattern': "independent"},
                            template={'data': {'indicator': [{'title': {'text': "Toneladas"}}]}}
                        )
                        col2.plotly_chart(fig_indicator, use_container_width=True)  
                        
            
            



    else:
        fig = px.bar(movimentoQ, x=periodicidade, y="Toneladas", color=selected_group)
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=3, label="3m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)





   
   


with tab2:
    st.dataframe(movimentacaoBercos)


