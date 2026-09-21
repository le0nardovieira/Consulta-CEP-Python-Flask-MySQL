# Consulta de CEP com Python, Flask e MySQL

Aplicação web desenvolvida para consulta de endereços a partir de CEPs brasileiros.

O sistema utiliza a API ViaCEP para buscar os dados do endereço, processa a resposta em JSON, exibe as informações em uma interface web e registra cada consulta em um banco de dados MySQL.

## Funcionalidades

- Consulta de CEP
- Validação do CEP informado
- Tratamento de CEP inválido
- Tratamento de CEP inexistente
- Consulta à API ViaCEP
- Manipulação de dados JSON
- Exibição de:
  - CEP
  - Logradouro
  - Bairro
  - Cidade
  - UF
- Registro das consultas no MySQL
- Registro automático de data e hora da consulta
- Abertura do endereço diretamente no Google Maps
- Interface web responsiva

## Tecnologias utilizadas

- Python
- Flask
- MySQL
- HTML
- CSS
- API ViaCEP
- JSON
- Requests
- Google Maps

## Como funciona

O fluxo da aplicação é:

CEP informado pelo usuário  
↓  
Flask recebe o formulário  
↓  
Python valida o CEP  
↓  
API ViaCEP é consultada  
↓  
A API retorna os dados em JSON  
↓  
Python processa os dados  
↓  
A consulta é registrada no MySQL  
↓  
O endereço é exibido na página  
↓  
O usuário pode abrir o local no Google Maps

## Estrutura do projeto

```text
Projeto_CEP_Python_MySQL/
│
├── app.py
├── banco.py
├── database.sql
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css