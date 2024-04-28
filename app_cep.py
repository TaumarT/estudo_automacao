from selenium import webdriver
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys
import pyautogui as auto
from selenium.webdriver.common.by import By
import xlsxwriter 
from openpyxl import load_workbook
abrir_navegador = webdriver.Chrome()

arquivo="C:\\Users\\taian\\Documents\\automacao\\PesquisaEndereco_1.xlsx"
planilhaCriada = load_workbook(arquivo)
# planilha = planilhaCriada.add_worksheet()

sheet_selecionada = planilhaCriada['Dados']

sheet_cep = planilhaCriada['CEP']

meuNavegador = opcoes_selenium_aula.Chrome()
meuNavegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
auto.sleep(2)


# print(endereco_rua)
# print(endereco_bairro)
# print(endereco_cidade_uf)
# print(endereco_cep)

for linha in range(2,len(sheet_cep['A'])+1):

    cep_pesquisa = sheet_cep['A%s'%linha].value
    meuNavegador.find_element(By.NAME,'endereco').send_keys(cep_pesquisa)
    auto.sleep(2)
    meuNavegador.find_element(By.NAME,'btn_pesquisar').click()
    auto.sleep(2)
    endereco_rua = meuNavegador.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    endereco_bairro = meuNavegador.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    endereco_cidade_uf = meuNavegador.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
    endereco_cep = meuNavegador.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text


    linha_corrente = len(sheet_selecionada['A'])+1

    colunaA = "A"+ str(linha_corrente)
    colunaB = "B"+ str(linha_corrente)
    colunaC = "C"+ str(linha_corrente)
    colunaD = "D"+ str(linha_corrente)
    sheet_selecionada[colunaA] = endereco_rua
    sheet_selecionada[colunaB] = endereco_bairro
    sheet_selecionada[colunaC] = endereco_cidade_uf
    sheet_selecionada[colunaD] = endereco_cep
    meuNavegador.find_element(By.XPATH,'//*[@id="btn_nbusca"]').click()

planilhaCriada.save(filename=arquivo)




# planilha.write("A1","RUA")
# planilha.write("B1","BAIRRO")
# planilha.write("C1","CIDADE")
# planilha.write("D1","CEP")
# planilha.write("A2",endereco_rua)
# planilha.write("B2",endereco_bairro)
# planilha.write("C2",endereco_cidade_uf)
# planilha.write("D2",endereco_cep)
planilhaCriada.close()
