import xlsxwriter
import os

arquivo="C:\\Users\\taian\\Documents\\automacao\\cadastrocliente.xlsx"

planilhaCriada = xlsxwriter.Workbook(arquivo)
planilha = planilhaCriada.add_worksheet()
planilha.write("A1","NOME")
planilha.write("B1","IDADE")
planilha.write("A2","Amanda")
planilha.write("B2",28)
planilha.write("A3","Roberto")
planilha.write("B3",25)


planilhaCriada.close()

# os.startfile(arquivo)