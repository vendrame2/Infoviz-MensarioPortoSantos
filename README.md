# Infoviz-MensarioPortoSantos
Trabalho para a matéria de Visualização da Informação (MECAI/USP São Carlos) com o objetivo de criar uma nova visualização das informações do Mensário par ao Porto de Santos


Organização de Projeto
.
├── data
│   ├── interim -> Dados intermediários
│   ├── processed -> Dados finais para modelagem
│   └── raw -> Fonte de dados iniciais e IMUTÁVEIS
│
├── docs -> Documentações de código, projeto, metadados e afins
│
├── Makefile -> Makefiles para automação e registro de comandos manuais
│
├── models -> Arquivos de modelos treinados, escalonadores e afins
│
├── notebooks -> Jupyter notebooks. │
├── README.md
│
└── src -> Armazena .py de estágios DVC e código base
│
├── __init__.py -> Torna src um módulo python
│
└── utils -> Armazena código base
│
├── data -> Funções/classes para processamento de dados
│
├── features -> Funções/classes para engenharia de features
│
├── models -> Funções/classes para treinamento e inferência de modelos
│
├── evaluation -> Funções/classes para avaliação de modelos, dados, artefatos, etc.
│
└── visualization -> Funções/classes para visualização