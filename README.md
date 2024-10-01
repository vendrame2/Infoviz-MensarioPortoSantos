

# 📊 Projeto de Visualização de Dados - Mensário Porto de Santos

Este projeto foi desenvolvido como parte da disciplina **MAI5017 – Visualização de Informação**, ministrada pelo prof. Dr. Afonso Paiva, para o curso de Mestrado Profissional MECAI no ICMC/USP, 2º semestre de 2024. O objetivo foi construir um **dashboard interativo** utilizando **Streamlit**, **Plotly Express**, e outras bibliotecas para a análise do **Mensário do Porto de Santos**. O dashboard fornece uma visão abrangente dos dados de movimentação de cargas no Porto de Santos, destacando tendências temporais e análises geoespaciais.

### 🔗 **Links Importantes**
- [Mensário Porto de Santos - Estatísticas Online](https://www.portodesantos.com.br/informacoes-operacionais/estatisticas/estatisticas-online-b-i/)
- [Dashboard Publicado](https://mensarioportosantos-infoviz.streamlit.app/)

---

## 🗂️ Estrutura do Projeto

```
├── data
│   ├── interim            -> Dados intermediários
│   ├── processed          -> Dados finais para modelagem
│   └── raw                -> Fonte de dados originais (IMUTÁVEIS)
│
├── docs                   -> Documentação de código, projeto e metadados
├── Makefile               -> Automação e registro de comandos
├── models                 -> Modelos treinados e escalonadores
├── notebooks              -> Notebooks Jupyter
├── README.md              -> Arquivo de descrição do projeto
├── src                    -> Código principal do projeto
│   ├── init.py            -> Torna `src` um módulo Python
│   └── utils              -> Funções utilitárias
│       ├── data           -> Processamento de dados
│       ├── features       -> Engenharia de features
│       ├── models         -> Treinamento e inferência de modelos
│       ├── evaluation     -> Avaliação de modelos, dados e artefatos
│       └── visualization  -> Visualizações (Plotly, Streamlit)
```

---

## 🖥️ Descrição das Páginas do Dashboard

### 1. 📈 **Evolução das Cargas Movimentadas**
   - **Descrição:** Apresenta a evolução mensal e anual das cargas movimentadas, com comparação à média móvel de 12 meses.
   - **Objetivo:** Identificar tendências de crescimento ou declínio no volume de carga.
   - **Ferramentas:** Gráficos de linha interativos com **Plotly Express**.

### 2. 📊 **Variação da Carga Movimentada YoY%**
   - **Descrição:** Análise da variação percentual ano a ano (YoY%) da movimentação de cargas.
   - **Objetivo:** Identificar picos ou quedas significativas na movimentação.
   - **Ferramentas:** Gráficos de barras e variação percentual.

### 3. 💹 **Variação da Carga Movimentada vs Ano Anterior e Indicadores Macroeconômicos**
   - **Descrição:** Integra a variação das cargas com indicadores macroeconômicos (PIB, taxa de câmbio, inflação).
   - **Objetivo:** Verificar correlações entre a movimentação portuária e a economia nacional.
   - **Ferramentas:** Gráficos combinando séries temporais de movimentação e indicadores econômicos.

### 4. 📦 **Análise de Cargas - Perfil de Carga**
   - **Descrição:** Evolução das cargas movimentadas por perfil (granel, carga geral, etc.) e suas proporções no total movimentado.
   - **Objetivo:** Compreender a distribuição das diferentes categorias de carga ao longo do tempo.
   - **Ferramentas:** Gráficos de pizza e barras empilhadas.

### 5. 🗺️ **Localização Física dos Terminais em Santos**
   - **Descrição:** Mapa interativo com a localização física dos terminais do Porto de Santos.
   - **Objetivo:** Fornecer uma visão geoespacial dos terminais e sua proximidade com infraestruturas logísticas.
   - **Ferramentas:** Mapa geoespacial com **Plotly** e **Mapbox**.

### 6. 🏭 **Análise de Terminais - Visão Geolocalizada de Cargas Movimentadas**
   - **Descrição:** Análise das cargas movimentadas por terminal com foco geoespacial.
   - **Objetivo:** Visualizar a movimentação de carga por terminal específico.
   - **Ferramentas:** Mapas interativos e gráficos de dispersão geoespacial.

### 7. 📦💼 **Análise de Fluxo de Carga por Terminal**
   - **Descrição:** Detalha o fluxo de carga entre terminais, destacando eficiência e padrões de movimentação.
   - **Objetivo:** Analisar os volumes de carga movimentados por cada terminal e seu fluxo.
   - **Ferramentas:** Gráficos de **fluxo** e **Sankey**.

### 8. 📊 **Visualização de Perfis de Carga por Dimensão (Terminal e Carga)**
   - **Descrição:** Análise integrada dos perfis de carga, relacionando-os com os terminais que os movimentam.
   - **Objetivo:** Entender as relações entre os perfis de carga e os terminais que os movimentam.
   - **Ferramentas:** Gráficos de barras empilhadas interativos.

### 9. 🏆 **Análise de Cargas - Top Movimentadores de Carga**
   - **Descrição:** Exibe os principais movimentadores de carga no Porto de Santos, classificando-os pelo volume movimentado.
   - **Objetivo:** Identificar os principais players responsáveis pela movimentação de carga no porto.
   - **Ferramentas:** Gráficos de barras horizontais interativos.

---

## ⚙️ Tecnologias Utilizadas

- **Streamlit**: Criação do dashboard interativo.
- **Plotly Express**: Geração de gráficos interativos.
- **Python**: Processamento de dados e desenvolvimento das funções principais.
- **Pandas**: Manipulação e análise de dados.
- **Mapbox**: Visualização geoespacial dos terminais portuários.

---

## 📂 Estrutura do Código

- **src/data**: Funções para processamento e manipulação de dados.
- **src/features**: Engenharia de features para análises específicas.
- **src/models**: Implementação de modelos para inferência e previsões.
- **src/evaluation**: Funções de avaliação de modelos e qualidade de dados.
- **src/visualization**: Funções para geração de gráficos e dashboards.

---

Esse projeto oferece uma análise visual e interativa dos principais indicadores do Porto de Santos, permitindo insights detalhados sobre a movimentação de cargas, geolocalização de terminais e tendências ao longo do tempo.

--- 

### 📧 **Contato**

Para dúvidas ou colaborações, sinta-se à vontade para entrar em contato com os membros do time:

| Membro da Equipe     | Papel no Projeto                                                                                  |
|----------------------|---------------------------------------------------------------------------------------------------|
| ![👨‍💻](https://emojipedia-us.s3.amazonaws.com/source/skype/289/man-technologist_1f468-200d-1f4bb.png) **Luiz Vendrame**    | Organização do Dataset, Prototipagem Inicial, Visualizações Geolocalizadas        |
| ![🧠](https://emojipedia-us.s3.amazonaws.com/source/skype/289/brain_1f9e0.png) **Denilson Nishida** | Data Storytelling, Insights de Negócio, Visualizações de Dados                    |
| ![👨‍💼](https://emojipedia-us.s3.amazonaws.com/source/skype/289/man-office-worker_1f468-200d-1f4bc.png) **Ricardo Maeshiro** | Data Storytelling para o Porto de Santos, Insights para Visualizações de Dados, Revisão de Informações Geolocalizadas |


Sinta-se à vontade para contatar qualquer membro da equipe para mais informações ou para discutir o projeto!

---
