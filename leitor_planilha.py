import pandas as pd
import os

def ler_planilha():
    while True:
        try:
            # Lê a planilha Excel
            df = pd.read_excel('ANULA PLANILHA ANULA MULTA.xlsx')
            
            # Obtém todos os nomes da coluna B e remove os NaN
            nomes = df.iloc[:, 1].tolist()
            nomes_filtrados = [(i, nome) for i, nome in enumerate(nomes) if pd.notna(nome) and str(nome).strip()]
            
            # Mostra os nomes disponíveis
            print("\nNomes disponíveis:")
            for i, nome in nomes_filtrados:
                print(f"{i + 1} - {nome.strip()}")
            
            while True:
                try:
                    # Solicita escolha do usuário
                    escolha = int(input("\nEscolha o número correspondente ao nome desejado: ")) - 1
                    
                    # Verifica se a escolha é válida
                    if escolha < 0 or escolha >= len(nomes):
                        print("Número inválido. Por favor, escolha um número da lista.")
                        continue
                        
                    if pd.isna(nomes[escolha]):
                        print("Opção inválida. Por favor, escolha um nome válido da lista.")
                        continue
                        
                    break
                except ValueError:
                    print("Por favor, digite um número válido.")
            
            # Obtém a linha correspondente à escolha
            linha = df.iloc[escolha]
            
            # Formata e exibe as informações
            print("\n=== Informações do Cliente ===")
            print(f"NOME COMPLETO: {linha.iloc[2] if pd.notna(linha.iloc[2]) else 'Não informado'}")
            print(f"ENDEREÇO COM CEP: {', '.join(str(linha.iloc[i]) for i in [14,15,17,13,12] if pd.notna(linha.iloc[i]))}")
            print(f"WHATSAPP: {""}")
            print(f"EMAIL: {linha.iloc[9] if pd.notna(linha.iloc[9]) else 'Não informado'}")
            print(f"RG / UF: {' '.join(str(linha.iloc[i]) for i in [4,5,6] if pd.notna(linha.iloc[i]))}")
            print(f"CPF: {linha.iloc[7] if pd.notna(linha.iloc[7]) else 'Não informado'}")
            print(f"CNH: {linha.iloc[8] if pd.notna(linha.iloc[8]) else 'Não informado'}")
            
            # Pergunta se deseja fazer nova consulta
            print("\n===================================")
            nova_consulta = input("Deseja fazer nova consulta? (S/N): ").strip().upper()
            if nova_consulta != 'S':
                break
            os.system('cls')
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Verifique se o arquivo 'ANULA PLANILHA ANULA MULTA.xlsx' está na mesma pasta do script.")
            break

if __name__ == "__main__":
    ler_planilha()