# Sistema de Consulta de Informações de Motoristas

Sistema em Python para consulta e exibição de informações de motoristas a partir de uma planilha Excel.

## Funcionalidades

- Lista todos os motoristas disponíveis na planilha
- Exibe informações detalhadas do motorista selecionado
- Interface interativa via console
- Validação de dados e tratamento de erros
- Opção de realizar múltiplas consultas em uma sessão

## Requisitos

- Python 3.x
- pandas
- openpyxl

## Instalação

1. Clone o repositório
2. Instale os pacotes necessários:
```bash
pip install pandas openpyxl
```

## Como Usar
Existem duas formas de executar o aplicativo:

1. Usando o arquivo batch:
   -Dê um duplo clique em executar_programa.bat
2. Usando Python diretamente:
```bash
python leitor_planilha.py
 ```

## Estrutura de Arquivos
script-multas/
│
├── leitor_planilha.py     # Script Python principal
├── executar_programa.bat  # Arquivo batch para execução fácil
└── README.md             # Documentação

## Formato dos Dados
A planilha Excel deve conter as seguintes colunas:

- Coluna B: Nomes dos Motoristas
- Coluna C: Nome Completo
- Colunas O,N,M,P: Endereço e CEP
- Coluna J: Email
- Colunas E,F,G: Informações de RG/UF
- Coluna H: CPF
- Coluna I: CNH
## Tratamento de Erros
O sistema inclui tratamento para:

- Entrada inválida do usuário
- Dados ausentes na planilha
- Erros de arquivo não encontrado
- Formato de dados inválido
## Como Contribuir
Para contribuir com este projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua funcionalidade
3. Faça commit das suas alterações
4. Faça push para a branch
5. Crie um Pull Request
## Licença
Este projeto está licenciado sob a Licença MIT.