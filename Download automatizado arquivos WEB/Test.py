import csv
import os

pasta = 'C:\\Users\\Lucas\\OneDrive\\Área de Trabalho\\APS\\downloads'
nome_arquivo = 'DadosBO_2020_1(FURTO DE VEÍCULOS).csv'

caminho_arquivo = os.path.join(pasta, nome_arquivo)

if not os.path.isfile(caminho_arquivo):
    print(f'O arquivo {nome_arquivo} não foi encontrado na pasta {pasta}. Certifique-se de fornecer o caminho correto.')
    exit()

anos = []
dados = []

with open(caminho_arquivo, mode='r', encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=';')
    
    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
    
        if '/' in linha[1]:
            ano_str = linha[1].split('/')[1]
            anos.append(int(ano_str))
        else:
            anos.append(0)
            
        dados.append(list(map(str, linha[1:])))

novo_nome_arquivo = 'dados_mensais.csv'

with open(novo_nome_arquivo, mode='w', newline='', encoding='utf-8') as novo_arquivo_csv:
    escritor_csv = csv.writer(novo_arquivo_csv)
    
    escritor_csv.writerow(cabecalho)
    
    for i, ano in enumerate(anos):
        linha = [ano, *dados[i]]
        escritor_csv.writerow(linha)

print(f'O novo arquivo {novo_nome_arquivo} foi criado com sucesso.')