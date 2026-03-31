# Validador e Gerador de CPF

Este projeto consiste em uma ferramenta de linha de comando (CLI) desenvolvida em Python para a validação e geração de números de CPF (Cadastro de Pessoas Físicas). O programa utiliza o algoritmo oficial de cálculos de dígitos verificadores para garantir a autenticidade matemática dos números processados.

## Funcionalidades

* **Gerar CPF Válido:** O sistema gera 9 dígitos aleatórios e calcula sequencialmente o primeiro e o segundo dígito verificador, entregando um CPF completo e formatado (000.000.000-00).
* **Validar CPF:** O usuário insere um CPF e o sistema realiza o cálculo dos pesos para conferir se os dígitos verificadores informados são matematicamente consistentes com a base do número.
* **Menu Interativo:** Uma interface simples no terminal que permite ao usuário escolher entre as funções de geração ou validação de forma contínua.

## Como o Algoritmo Funciona

A validação de um CPF baseia-se no algoritmo do **Módulo 11**. Para cada dígito verificador, é realizada uma soma ponderada dos dígitos anteriores por uma sequência decrescente de pesos (começando em 10 para o primeiro dígito e 11 para o segundo). O resto da divisão dessa soma por 11 determina o dígito final.



## Pré-requisitos

* Python 3.x instalado.
* Biblioteca nativa `random` (já inclusa no Python).

## Como Executar

1. Salve o código em um arquivo chamado `main.py`.
2. Abra o terminal na pasta do arquivo.
3. Execute o comando:
   ```bash
   python main.py
