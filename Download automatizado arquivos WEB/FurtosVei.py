from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import csv
import time

download_directory = os.path.join(os.getcwd(), 'downloads')
os.makedirs(download_directory, exist_ok=True)

caminho_download = 'C:\\Users\\Lucas\\OneDrive\\Área de Trabalho\\APS\\downloads'
nome_arquivo = 'DadosBO_2020_1(FURTO DE VEÍCULOS).csv'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_directory
})

driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx'
driver.get(url)

furtos_button = driver.find_element(By.ID, "cphBody_btnFurtoVeiculo")
furtos_button.click()

for year in range(1, 4):
    year_name = ['cphBody_lkAno20', 'cphBody_lkAno21', 'cphBody_lkAno22'][year - 1]
    year_button_selector = year_name
    
    year_button = driver.find_element(By.ID, year_button_selector)
    year_button.click()

    for month in range(1, 13):
        month_name = ['cphBody_lkMes1', 'cphBody_lkMes2', 'cphBody_lkMes3', 'cphBody_lkMes4', 'cphBody_lkMes5', 'cphBody_lkMes6', 'cphBody_lkMes7', 'cphBody_lkMes8', 'cphBody_lkMes9', 'cphBody_lkMes10', 'cphBody_lkMes11', 'cphBody_lkMes12'][month - 1]

        month_button_selector = month_name
        
        time.sleep(8)
        month_button = driver.find_element(By.ID, month_button_selector)
        month_button.click()

        exportar_button = driver.find_element(By.ID, "cphBody_ExportarBOLink")
        exportar_button.click()  

print("O arquivo foi baixado com sucesso!!")

caminho_arquivo = os.path.join(caminho_download, nome_arquivo)

if not os.path.isfile(caminho_arquivo):
    print(f'O arquivo {nome_arquivo} não foi encontrado na pasta {caminho_download}. Certifique-se de fornecer o caminho correto.')
    exit()

print("O arquivo foi baixado com sucesso!!")

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
















































