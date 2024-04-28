from selenium import webdriver
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausaComputador
from selenium.webdriver.common.by import By
import xlsxwriter
abrir_navegador = webdriver.Chrome()

meuNavegador = opcoes_selenium_aula.Chrome()
meuNavegador.get("https://www.google.com.br/?hl=pt-BR")
meuNavegador.find_element(By.NAME,'q').send_keys("Dolar hoje")
meuNavegador.find_element(By.NAME,'q').send_keys(Keys.RETURN)
valorDolarPeloGoogle = meuNavegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
print(valorDolarPeloGoogle)
tempoPausaComputador.sleep(4)
meuNavegador.find_element(By.NAME,'q').send_keys(" ")
tempoPausaComputador.sleep(4)
tempoPausaComputador.press('tab')
tempoPausaComputador.press('enter')
meuNavegador.find_element(By.NAME,'q').send_keys("euro")
meuNavegador.find_element(By.NAME,'q').send_keys(Keys.RETURN) 

valorEuroPeloGoogle = meuNavegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
print(valorEuroPeloGoogle)
tempoPausaComputador.sleep(4)


arquivo="C:\\Users\\taian\\Documents\\automacao\\dolar_euro.xlsx"

planilhaCriada = xlsxwriter.Workbook(arquivo)
planilha = planilhaCriada.add_worksheet()
planilha.write("A1","Dolar")
planilha.write("B1","Euro")
planilha.write("A2",valorDolarPeloGoogle)
planilha.write("B2",valorEuroPeloGoogle)
planilhaCriada.close()
# os.startfile(arquivo)